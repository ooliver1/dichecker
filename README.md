# dichecker

A runtime checker for modern TypedDicts

## Supported Typings

- `Any`
- `dict`
- `Dict`
- `List`
- `list`
- `Literal`
- `NotRequired`
- `None`
- `Optional`
- `T | ...`
- `TypedDict`
- `Union`
- `str` (and all other normal classes)

## How To Use

### Install

```bash
pip install dichecker
# or
poetry add dichecker
```

### Add To Code

```py
from typing import Any, Optional, TypedDict

from typing_extensions import NotRequired

from dichecker import check_hints


class MyCoolType(TypedDict):
    anything: NotRequired[You]
    want: Optional[Really]
    this: IsJust | An | Example


def function(not_verified_dict: Any) -> MyCoolType:
    return check_hints(MyCoolType, not_verified_dict)
```
