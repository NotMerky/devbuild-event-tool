# Dev Build Event Tool by Merky

This tool allows you to enable or disable specific in-game events for Dead by Daylight's Developer Build, based on the settings stored in the `events.hjson` file. The tool provides a simple user interface where you can select the event to enable or disable, or restore default event settings.

## Features

- Display the current active event.
- Enable specific events:
  - Winter2017
  - Lunar
  - Summer
  - Halloween2018
  - Winter2018
  - Lunar2019
  - Anniversary2019
- Disable all events, restoring default event settings.
- Simple console-based interface.

## Prerequisites

- **Python 3.x**: This tool requires Python 3.x to run.
- **Dead by Daylight Developer Build**: You need to have the updated Developer Build Launcher by Smirkzzy installed and configured.
- **DevServerPath.sav**: The tool reads a file located in `%localappdata%\DBD.DevBuildLauncher\DevServerPath.sav` to find the directory of the events configuration.

## Installation

1. Ensure that you have Python 3.x installed on your system.
2. Clone or download this repository to your local machine.
3. Install the required Python dependencies:
   ```bash
   pip install hjson
4. Build the .exe file (if you want a standalone version) using PyInstaller:
      ```bash
   pyinstaller --onefile --icon=your_icon.ico --name=DevBuildEventTool main.py

## Usage
1. Run the tool.
2. Choose an event to enable or disable by entering the corresponding number.
3. The tool will save your changes to the events.hjson file and display a confirmation message.

## Troubleshooting
If you encounter issues while running the tool:
1. Ensure that DevServerPath.sav exists in the specified location (%localappdata%\DBD.DevBuildLauncher).
2. Verify that the events.hjson file is correctly formatted and accessible.

## Notes
1. This tool requires Dead by Daylight's Developer Build to be set up correctly.
2. The DevServerPath.sav file should contain the path to the game’s configuration files for the Developer Build.
3. The events.hjson file is used to manage event settings.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer
This tool is for use with the Developer Build of Dead by Daylight. It is not intended for use with the public or live version of the game. Use at your own risk.

## Attribution
- [Developer Build Server by Preston159](https://github.com/Preston159/dbd-server)
- [Batch Developer Build Launcher by Smirkzzy](https://drive.google.com/file/d/1DdGhTkkgaXFxN02V2jf6xNXApLApEdoc/view?usp=drive_link) [GitHub: SmirkzzyDBD](https://github.com/SmirkzyyDBD)
- [Schedule setting icons created by Arslan Haider - Flaticon](https://www.flaticon.com/free-icons/schedule-setting)
