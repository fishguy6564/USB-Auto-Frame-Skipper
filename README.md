# USB-Auto-Frame-Skipper

USB Auto Frame Skipper is an automatic day skipper for Nintendo Switch. This is intended to be used for shiny hunting in Pokemon Sword and Shield. USB Auto Frame Skipper relies on USB-botbase, which can be downloaded [here](https://github.com/fishguy6564/USB-Botbase).

## Requirements
- A hacked Switch with Atmosphere CFW installed.
- Python3 must be installed in order to use Lanturn.
- A usb-c to usb-a cable is required to connect your PC to your Nintendo Switch.
- Pyusb is necessary in order to communicate to the Nintendo Switch. You can install Pyusb by using the following pip command.
```bash
pip install pyusb
```
- A usb backend is necessary. Please use [Zadig](http://www.unitrunker.com/zadig.html) and install the libusbk driver to your Nintendo Switch by plugging it in while running the sys-module.
- Install libusb with [this](http://www.mediafire.com/file/wdx5lu4c37sm1cv/libusb-win32-devel-filter-1.2.6.0.exe/file).

## Installation
Once you have installed all the requirements listed above, click "Clone or download" and then click "Download ZIP". 
- Extract the contents in the ZIP to a folder.
- Run the run.bat for the date format you have.
- Input the amount of frames you want to skip. (The bot is adjusted to subtract 1 from the frame count given by seed checker bots)
- Input the date on your switch in the format it requires.
- Watch the magic unfold!
