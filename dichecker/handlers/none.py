# SPDX-License-Identifier: MIT

from __future__ import annotations

from typing import TYPE_CHECKING

from ..errors import IncorrectType

if TYPE_CHECKING:
    from typing import Any, TypeVar

    T = TypeVar("T")

__all__ = ("handle_none",)


def handle_none(type_check: type[T], object_value: Any) -> T:
    if object_value is not None:
        raise IncorrectType(
            f"{object_value} was expected to be {type_check} "
            f"but was {type(object_value)}"
        )

    return object_value
