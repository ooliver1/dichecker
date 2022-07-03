# SPDX-License-Identifier: MIT

from __future__ import annotations

from typing import TYPE_CHECKING

from ..errors import IncorrectType

if TYPE_CHECKING:
    from typing import Any, TypeVar

    T = TypeVar("T")

__all__ = ("handle_object",)


def handle_object(type_check: type[T], object_value: Any) -> T:
    if not isinstance(object_value, type_check):
        raise IncorrectType(
            f"{object_value} was expected to be {type_check} "
            f"but was {type(object_value)}"
        )

    return object_value
