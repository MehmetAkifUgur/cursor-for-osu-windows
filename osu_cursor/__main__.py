"""Command line entry point. Without arguments it opens the window."""

from __future__ import annotations

import argparse
import sys

from . import windows as desktop

from .library import Result
from .i18n import _
from .skin import SkinError


def _report(result: Result) -> None:
    print(_("Applied: {name} ({size} px)").format(name=result.skin_name, size=result.size_px))


def main() -> int:
    # A packaged process may already have its DPI context set by the manifest.
    desktop.win32.set_dpi_context(-4)  # DPI_AWARENESS_CONTEXT_PER_MONITOR_AWARE_V2
    parser = argparse.ArgumentParser(prog="cursor-for-osu")
    commands = parser.add_subparsers(dest="command")
    apply_parser = commands.add_parser("apply", help=_("apply a skin"))
    apply_parser.add_argument("skin", help=_(".osk file or skin folder"))
    apply_parser.add_argument(
        "--size",
        type=float,
        help=_("cursor size from 0.1 to 2.0 (default: the last one set, or your osu!lazer setting)"),
    )
    size_parser = commands.add_parser("size", help=_("change the cursor size"))
    size_parser.add_argument("value", type=float, help=_("from 0.1 to 2.0, like in the game"))
    commands.add_parser("reset", help=_("go back to the previous cursor"))
    commands.add_parser("status", help=_("show the applied skin"))
    arguments = parser.parse_args()
    if arguments.command is None:
        from .windows_gui import run

        return run()

    try:
        if arguments.command == "apply":
            _report(desktop.apply_skin(arguments.skin, arguments.size))
        elif arguments.command == "size":
            result = desktop.set_cursor_size(arguments.value)
            if result:
                _report(result)
            else:
                print(_("Size saved: {size}").format(size=f"{arguments.value:.2f}"))
        elif arguments.command == "reset":
            desktop.reset()
            print(_("Back to the previous cursor"))
        else:
            print(_("Skin: {name}").format(name=desktop.active().get("name") or _("none")))
            print(_("Size: {size}").format(size=f"{desktop.cursor_size():.2f}"))
    except (SkinError, OSError) as error:
        print(error, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
