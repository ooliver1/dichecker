# SPDX-License-Identifier: MIT

from __future__ import annotations

from collections import OrderedDict
from types import UnionType
from typing import TYPE_CHECKING, Any, Literal, Union, get_origin

from typing_extensions import is_typeddict

from .handlers.any import handle_any
from .handlers.dict import handle_dict
from .handlers.list import handle_list
from .handlers.literal import handle_literal
from .handlers.typed_dict import handle_typed_dict
from .handlers.union import handle_union
from .handlers.none import handle_none
from .handlers.object import handle_object

if TYPE_CHECKING:
    from typing import TypeVar

    T = TypeVar("T")


__all__ = ("check_hints",)


handlers = OrderedDict(
    {
        (lambda t: is_typeddict(t)): handle_typed_dict,
        (lambda t: get_origin(t) is dict): handle_dict,
        (lambda t: get_origin(t) is list): handle_list,
        (lambda t: get_origin(t) in (Union, UnionType)): handle_union,
        (lambda t: get_origin(t) is Literal): handle_literal,
        (lambda t: t is Any): handle_any,
        (lambda t: t is None): handle_none,
        (lambda _: True): handle_object,
    }
)


def check_hints(type_check: type[T], object_value: Any) -> T:
    for condition, checker in handlers.items():
        if condition(type_check):
            return checker(type_check, object_value)

    raise RuntimeError(f"No handler found for type {type_check}")
