def greeting(name: str) -> str:
    return "hello " + name


def show_count(count: int, word: str) -> str:
    if count == 1:
        return f"1 {word}"
    count_str = str(count) if count else "no"
    return f"{count_str} {word}s"


if __name__ == "__main__":
    print(greeting("ali"))
    print(greeting("rizwan"))
