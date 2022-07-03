# SPDX-License-Identifier: MIT

from __future__ import annotations

from types import GenericAlias
from typing import TYPE_CHECKING, cast

from ..errors import IncorrectType

if TYPE_CHECKING:
    from typing import Any, TypeVar

    T = TypeVar("T")

__all__ = ("handle_literal",)


def handle_literal(type_check: type[T], object_value: Any) -> T:
    generic_type = cast(GenericAlias, type_check)
    if object_value not in generic_type.__args__:
        raise IncorrectType(
            f"{object_value} is not a {type_check} but was {type(object_value)}"
        )

    return object_value
