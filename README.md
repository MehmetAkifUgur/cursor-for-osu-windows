# Cursor for osu! — Windows

Use the cursor and trail from an osu! skin on your Windows desktop.

## Download and use

1. Download **CursorForOsu-windows-x64.zip** from [Releases](https://github.com/MehmetAkifUgur/cursor-for-osu-windows/releases/latest). Requires Windows 11 x64.
2. Extract the entire ZIP and open **CursorForOsu.exe**. Keep the `_internal` folder beside it.
3. Add an `.osk` file or a skin folder and click its card to apply it. Use **Trail** and **Trail density** to adjust the effect.

Closing the window keeps the trail running. Use the notification area icon to reopen or quit the app. Choose **Go back to the previous cursor** to restore your Windows pointer scheme. Skin copies and settings are stored in `%LOCALAPPDATA%\CursorForOsu`.

## Build from source

Run these PowerShell commands from the repository folder with 64-bit Python 3.11.

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r packaging/windows/requirements.txt
.\.venv\Scripts\python.exe packaging/windows/build.py
```

The portable ZIP is written to `build/windows/CursorForOsu-windows-x64.zip`.

Based on [Egehan Kara’s Cursor for osu!](https://github.com/egehankara/cursor-for-osu). This fan project is independent of ppy and osu!. [MIT license](LICENSE) · [Third-party notices](THIRD-PARTY-NOTICES).
