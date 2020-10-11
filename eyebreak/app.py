import rumps
import schedule
from pync import notify


class EyeBreakApp(rumps.App):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.schedule_button = None
        self.work_time = 30
        self.time_to_next_break = self.work_time
        self.schedule_button = None

        schedule.run_continuously()

    @rumps.clicked("Schedule")
    def schedule_break(self, sender):
        if not self.schedule_button:
            self.schedule_button = sender

        sender.set_callback(None)

        def update_schedule_button_title():
            if sender.callback is None and self.time_to_next_break != 0:
                self.time_to_next_break -= 1
                sender.title = f"Next break in {self.time_to_next_break} min."

        update_schedule_button_title()

        schedule.every(self.work_time).minutes.do(
            self.send_break_notification, sender=sender
        )
        schedule.every().minute.do(update_schedule_button_title)

    def send_break_notification(self, sender):
        notify("Take a 10 min. break!", title="EyeBreak", sound="default")
        self.stop_scheduling(sender)

    def stop_scheduling(self, sender):
        schedule.clear()

        sender.title = "Schedule"
        sender.set_callback(self.schedule_break)

        self.time_to_next_break = self.work_time

    @rumps.clicked("Stop")
    def stop(self, _):
        self.stop_scheduling(self.schedule_button)
