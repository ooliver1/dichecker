from typing import Any, Dict, List, Literal, Optional, TypedDict

from dichecker import check_hints

from typing_extensions import NotRequired


class AnotherTypedDict(TypedDict):
    another_field: str


class Check(TypedDict):
    string: str
    integer: int
    characters: str | bytes
    nullable: str | None
    old: Optional[str]
    only: Literal[1, 2, 3]
    anything: Any
    many: list[str]
    also_old: List[str]
    mapped: dict[str, int]
    many_old: Dict[str, int]
    maybe: NotRequired[str]
    complicated: AnotherTypedDict
    yes: bool
    crazy: NotRequired[Optional[str]]


pls: Check = {
    "string": "h",
    "integer": 123,
    "characters": b"abc",
    "nullable": None,
    "old": "help",
    "only": 2,
    "anything": anext,
    "many": ["a", "b", "c"],
    "also_old": ["help", "me", "pls"],
    "mapped": {"one": 1, "two": 2, "three": 3},
    "many_old": {"a": 1, "b": 2, "c": 3},
    "complicated": {"another_field": "help"},
    "yes": True,
    "crazy": "yes",
}


check_hints(Check, pls)
