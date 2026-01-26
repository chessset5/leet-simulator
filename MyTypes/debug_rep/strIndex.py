class strIndex:
    def __init__(self, string: str, index: int) -> None:
        self.string: str = string
        self.index: int = index

    def __str__(self) -> str:
        return f"{self.index} | {self.string}"

    def __repr__(self) -> str:
        i: int = self.index
        i %= len(self.string)

        return self.string[:i] + "[" + self.string[i] + "]" + self.string[i + 1 :]
