import pkg_resources

from eyebreak.app import EyeBreakApp

EyeBreakApp(
    "EyeBreak", icon=pkg_resources.resource_filename(__name__, "icon.png")
).run()
