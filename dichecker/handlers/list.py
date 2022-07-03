# SPDX-License-Identifier: MIT

from __future__ import annotations

from types import GenericAlias
from typing import cast, TYPE_CHECKING

from .. import checker

if TYPE_CHECKING:
    from typing import Any, TypeVar

    T = TypeVar("T")

__all__ = ("handle_list",)


def handle_list(type_check: type[T], object_value: Any) -> T:
    generic_type = cast(GenericAlias, type_check)
    list_type = generic_type.__args__[0]

    listed = cast(list, object_value)
    for i in listed:
        checker.check_hints(list_type, i)

    return object_value
