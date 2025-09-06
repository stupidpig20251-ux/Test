# Analog Clock App

This repository contains a simple desktop application that displays an analog clock using Tkinter.

## Build a Windows Executable
If you want to run the clock without invoking Python directly, you can bundle it into an `.exe` with [PyInstaller](https://pyinstaller.org/):

1. Install PyInstaller: `pip install pyinstaller`
2. Run the provided batch script:

   ```
   build_exe.bat
   ```

   This creates `dist/AnalogClock.exe`, a standalone executable.
3. Double-click `AnalogClock.exe` to launch the clock.

## Development from Source (optional)
To run the script directly during development:

```
python clock.py
```

This opens a window with a circular clock showing the current time.
The clock window is configured to stay on top of other windows so it remains visible.
