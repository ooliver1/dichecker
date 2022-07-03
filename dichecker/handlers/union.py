# SPDX-License-Identifier: MIT

from __future__ import annotations

from types import GenericAlias
from typing import TYPE_CHECKING, cast

from .. import checker
from ..errors import IncorrectType

if TYPE_CHECKING:
    from typing import Any, TypeVar

    T = TypeVar("T")

__all__ = ("handle_union",)


def handle_union(type_check: type[T], object_value: Any) -> T:
    generic_type = cast(GenericAlias, type_check)

    for t in generic_type.__args__:
        try:
            checker.check_hints(t, object_value)
        except IncorrectType:
            continue
        else:
            break
    else:
        raise IncorrectType(
            f"{object_value} is not a {type_check} but was {type(object_value)}"
        )

    return object_value
