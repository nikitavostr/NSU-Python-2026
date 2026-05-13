def collatz(num: int) -> list[int]:
    if num <= 0:
        return []

    seq = [num]
    while num != 1:
        num = num // 2 if num % 2 == 0 else 3 * num + 1
        seq.append(num)
    return seq


def main():
    n = int(input("Enter a number: "))
    seq = collatz(n)
    print("->".join(map(str, seq)))


if __name__ == "__main__":
    main()
