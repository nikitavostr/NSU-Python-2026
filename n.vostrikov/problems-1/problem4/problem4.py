def sing_the_song() -> list[str]:
    names: list[str] = [
        "no",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "ten",
    ]
    lines: list[str] = []

    for n in range(10, 0, -1):
        label: str = names[n].capitalize()
        unit: str = "bottle" if n == 1 else "bottles"
        refrain: str = f"{label} green {unit} hanging on the wall,"
        left: int = n - 1
        tail: str = "bottle" if left == 1 else "bottles"
        prefix: str = "If that" if n == 1 else "And if"
        lines.extend((
            refrain,
            refrain,
            f"{prefix} one green bottle should accidentally fall,",
            f"There'll be {names[left]} green {tail} hanging on the wall.",
        ))

    return lines


if __name__ == "__main__":
    song = sing_the_song()
    for line in song:
        print(line)
