import rumps
import schedule
from pync import notify


class EyeBreakApp(rumps.App):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.scheduled = False
        schedule.run_continuously()

    @rumps.clicked("Schedule")
    def schedule_break(self, _):
        if self.scheduled:
            rumps.alert("Break is already scheduled")
        else:
            notify("Break scheduled", title="EyeBreak")
            schedule.every(30).minutes.do(self.send_break_notification)
            self.scheduled = True

    def send_break_notification(self):
        notify("Take a 10 min. break!", title="EyeBreak", sound="default")
        schedule.clear()
        self.scheduled = False
