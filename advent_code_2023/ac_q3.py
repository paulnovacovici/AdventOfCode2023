from functools import reduce


def parse_file() -> list[list[str]]:
    with open("av_q3.txt", "r") as file:
        ret = []
        for line in file:
            line = line.strip()
            chars = []
            for char in line:
                chars.append(char)
            ret.append(chars)
        return ret


def is_symbol(char: str) -> bool:
    return (char < "0" or char > "9") and char != "."


def is_digit(char: str) -> bool:
    return char >= "0" and char <= "9"


def is_gear_ratio(char: str) -> bool:
    return char == "*"


def sum_neighbors(schematic: list[list[str]], x: int, y: int, visited: set[int]) -> int:
    pos = [-1, 0, 1]
    acc = 0
    for inc_x in pos:
        for inc_y in pos:
            if inc_x == 0 and inc_y == 0:
                continue
            new_pos = ((y + inc_y), (x + inc_x))
            if new_pos in visited:
                continue

            if is_digit(schematic[new_pos[0]][new_pos[1]]):
                # iterate to beginning of number
                i = new_pos[1] - 1
                while i >= 0 and is_digit(schematic[new_pos[0]][i]):
                    i -= 1
                i += 1
                number = ""
                while i < len(schematic[new_pos[0]]) and is_digit(
                    schematic[new_pos[0]][i]
                ):
                    number += schematic[new_pos[0]][i]
                    i += 1
                    visited.add((new_pos[0], i))
                acc += int(number)
            visited.add(new_pos)
    return acc


def sum_gear_ratios_neighbors(
    schematic: list[list[str]], x: int, y: int, visited: set[int]
) -> int:
    pos = [-1, 0, 1]
    product_set = []
    for inc_x in pos:
        for inc_y in pos:
            if inc_x == 0 and inc_y == 0:
                continue
            new_pos = ((y + inc_y), (x + inc_x))
            if new_pos in visited:
                continue

            if is_digit(schematic[new_pos[0]][new_pos[1]]):
                # iterate to beginning of number
                i = new_pos[1] - 1
                while i >= 0 and is_digit(schematic[new_pos[0]][i]):
                    i -= 1
                i += 1
                number = ""
                while i < len(schematic[new_pos[0]]) and is_digit(
                    schematic[new_pos[0]][i]
                ):
                    number += schematic[new_pos[0]][i]
                    i += 1
                    visited.add((new_pos[0], i))
                product_set.append(int(number))
            visited.add(new_pos)
    if len(product_set) > 1:
        return reduce(lambda x, y: x * y, product_set)
    return 0


def traverse_schematic_q1(schematic: list[list[str]]):
    acc = 0
    visited = set()
    for y, row in enumerate(schematic):
        for x, char in enumerate(row):
            if is_symbol(char):
                val = sum_neighbors(schematic, x, y, visited)
                acc += val
    print(acc)


def traverse_schematic_q2(schematic: list[list[str]]):
    acc = 0
    visited = set()
    for y, row in enumerate(schematic):
        for x, char in enumerate(row):
            if is_gear_ratio(char):
                val = sum_gear_ratios_neighbors(schematic, x, y, visited)
                acc += val
    print(acc)


schematic = parse_file()
traverse_schematic_q2(schematic)
