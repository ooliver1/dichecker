# SPDX-License-Identifier: MIT

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Any, TypeVar

    T = TypeVar("T")

__all__ = ("handle_any",)


def handle_any(type_check: type[T], object_value: Any) -> T:
    return object_value
