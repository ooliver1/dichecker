# SPDX-License-Identifier: MIT

from __future__ import annotations

from types import GenericAlias
from typing import TYPE_CHECKING, cast, get_origin, get_type_hints

from typing_extensions import NotRequired

from .. import checker
from ..errors import KeyNotFound

if TYPE_CHECKING:
    from typing import Any, TypeVar

    T = TypeVar("T")

__all__ = ("handle_typed_dict",)


def handle_typed_dict(type_check: type[T], object_value: Any) -> T:
    for h, thing in get_type_hints(type_check).items():
        origin = get_origin(thing)

        if h not in object_value:
            if origin in type_check.__optional_keys__ or origin is NotRequired:  # type: ignore
                # this does exist but importing _TypedDictMeta is not understood either
                continue
            else:
                raise KeyNotFound(f"{h} is not in {object_value}")

        if origin is NotRequired:
            generic_type = cast(GenericAlias, thing)
            checker.check_hints(generic_type.__args__[0], object_value[h])
        else:
            checker.check_hints(thing, object_value[h])

    return object_value
