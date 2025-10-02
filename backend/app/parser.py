from dataclasses import dataclass
from typing import runtime_checkable, Protocol

class UpperLetter(str):
    def __new__(cls, token) -> "UpperLetter":
        tkn_str = super().__new__(cls, str(token).upper())
        if not len(tkn_str) == 1:
            raise SyntaxError(f"Letter has to be of length 1, but has {len(tkn_str)}")
        return tkn_str

@dataclass
class BkKey:
    row: int
    user_id: UpperLetter
    num: int
    suffix: None|str

def parse_key(key: str) -> tuple[bool, BkKey]:
    return
