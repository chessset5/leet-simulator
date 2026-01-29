"""
Docstring for MyTypes.debug_rep.vis_index

Visual Index of a value and its selected index
"""


class StrIndex:
    """
    visually shows off index of a string
    """

    def __init__(self, string: str, index: int) -> None:
        self.string: str = string
        self.index: int = index

    def __str__(self) -> str:
        return f"{self.index} | {self.string}"

    def __repr__(self) -> str:
        i: int = self.index
        i %= len(self.string)

        return self.string[:i] + "[" + self.string[i] + "]" + self.string[i + 1 :]


class BinIntIndex(StrIndex):
    """
    visually shows off index of a binary string
    """

    def __init__(self, integer: int, index: int) -> None:
        val: str = bin(integer)
        if index >= len(val) - 2:
            raise IndexError("Index outside of bit selection")
        super().__init__(val, index + 2)
