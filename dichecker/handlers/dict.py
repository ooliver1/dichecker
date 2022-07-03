# SPDX-License-Identifier: MIT

from __future__ import annotations

from types import GenericAlias
from typing import TYPE_CHECKING, cast

from .. import checker

if TYPE_CHECKING:
    from typing import Any, TypeVar

    T = TypeVar("T")

__all__ = ("handle_dict",)


def handle_dict(type_check: type[T], object_value: Any) -> T:
    generic_type = cast(GenericAlias, type_check)
    key_type, value_type = generic_type.__args__

    dictionary = cast(dict, object_value)
    for k, v in dictionary.items():
        checker.check_hints(key_type, k)
        checker.check_hints(value_type, v)

    return object_value
