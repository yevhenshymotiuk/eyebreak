import rumps
import schedule
from pync import notify


class EyeBreakApp(rumps.App):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.scheduled = False
        schedule.run_continuously()
        self.schedule_button = None

    @rumps.clicked("Schedule")
    def schedule_break(self, _):
        if not self.schedule_button:
            self.schedule_button = self.menu["Schedule"]

        notify("Break scheduled", title="EyeBreak")
        schedule.every(30).minutes.do(self.send_break_notification)
        self.schedule_button.set_callback(None)

    def send_break_notification(self):
        notify("Take a 10 min. break!", title="EyeBreak", sound="default")
        schedule.clear()
        self.schedule_button.set_callback(self.schedule_break)
