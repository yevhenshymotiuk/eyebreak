import rumps
import schedule
from pync import notify


class EyeBreakApp(rumps.App):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.schedule_button = None
        self.work_time = 30
        self.time_to_next_break = self.work_time

        schedule.run_continuously()

    @rumps.clicked("Schedule")
    def schedule_break(self, sender):
        notify("Break scheduled", title="EyeBreak")
        schedule.every(self.work_time).minutes.do(
            self.send_break_notification, sender=sender
        )

        def update_schedule_button_title():
            self.time_to_next_break -= 1
            sender.title = f"Next break in {self.time_to_next_break} min."

        update_schedule_button_title()
        schedule.every().minute.do(update_schedule_button_title)
        sender.set_callback(None)

    def send_break_notification(self, sender):
        notify("Take a 10 min. break!", title="EyeBreak", sound="default")
        schedule.clear()
        self.time_to_next_break = self.work_time
        sender.set_callback(self.schedule_break)
        sender.title = "Schedule"
