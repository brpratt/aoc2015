import sys


def solve_part_1(lines: list[str]) -> int:
    char_diff = 0
    for line in lines:
        l = line.strip()
        if l:
            char_diff += len(l) - len(eval(l))
    return char_diff


def solve_part_2(lines: list[str]) -> int:
    char_diff = 0
    for line in lines:
        l = line.strip()
        if l:
            encode_len = len(l) + 2 + l.count('"') + l.count("\\")
            char_diff += encode_len - len(l)
    return char_diff


if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()
        print(solve_part_1(lines))
        print(solve_part_2(lines))
