"""Find every text the app shows, so the translations can be checked against it."""

from __future__ import annotations

import ast
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def all_messages() -> set[str]:
    found = set()
    for path in (ROOT / "osu_cursor").glob("*.py"):
        for node in ast.walk(ast.parse(path.read_text(encoding="utf-8"), str(path))):
            if (
                isinstance(node, ast.Call)
                and isinstance(node.func, ast.Name)
                and node.func.id == "_"
                and node.args
                and isinstance(node.args[0], ast.Constant)
                and isinstance(node.args[0].value, str)
            ):
                found.add(node.args[0].value)
    return found
