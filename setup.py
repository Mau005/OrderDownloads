import sys
from cx_Freeze import setup, Executable

build_exe_options = {"excludes": ["tkinter", "Config.json"],  "optimize": 1}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="OrderDowloads 2.0",
    version="2.0",
    description="OrderDowloads",
    author = "AinhoSoft SPA",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base)],
)

