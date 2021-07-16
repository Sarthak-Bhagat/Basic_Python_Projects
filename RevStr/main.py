"""Reverse a string. Mostly overkill."""


def main(S: str) -> str:
    """Reverse it."""
    return S[::-1]


if __name__ == "__main__":
    inp = input("Enter a String\n")
    print(main(inp))
