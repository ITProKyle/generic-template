"""Import classes."""
from typing import Callable

import sys

import pygments.styles

from .one_dark import OneDark  # noqa


def pygments_patch_style(mod_name: str, cls: Callable) -> None:
    """Add a custom style class to pygments for use with sphinx."""
    cls_name = cls.__name__
    mod = type(__import__("os"))(mod_name)
    setattr(mod, cls_name, cls)
    setattr(pygments.styles, mod_name, mod)
    sys.modules["pygments.styles." + mod_name] = mod
    from pygments.styles import STYLE_MAP
    STYLE_MAP[mod_name] = mod_name + "::" + cls_name
