# SPDX-License-Identifier: MIT


class KeyNotFound(KeyError):
    """Raised if the input does not have a key in a TypedDict"""


class IncorrectType(TypeError):
    """Raised if the input's type is incompatible with the type defined"""
