from itertools import product
from functools import cache


def parse_file() -> list[tuple[str, list[int]]]:
    rows = open("ac_q12.txt", "r").read().split("\n")
    ret = []

    for row in rows:
        row, groups = row.split(" ")
        groups = list(map(lambda x: int(x), groups.split(",")))
        ret.append(("?".join(([row] * 5)), groups * 5))
    return ret


def all_combos(row: str) -> list[tuple]:
    p = []
    for char in row:
        if char == "?":
            p.append([".", "#"])
        else:
            p.append(char)
    return list(product(*p))


def count_combos(row: str, groups: list[int]) -> int:
    acc = 0

    for p in all_combos(row):
        ret = []
        count = 0
        for c in p:
            if c == "." and count > 0:
                ret.append(count)
                count = 0
            if c == "#":
                count += 1
        if count > 0:
            ret.append(count)
        if ret == groups:
            acc += 1
    return acc


def count_perms(row: str, groups: list[int]):
    @cache
    def helper(i: int, j: int, group_count: int) -> int:
        if i >= len(row):
            if j == len(groups) - 1 and group_count == groups[j]:
                return 1
            if j == len(groups) and group_count == 0:
                return 1
        if i >= len(row):
            return 0

        chars = [".", "#"] if row[i] == "?" else [row[i]]

        ret = 0

        for char in chars:
            if char == ".":
                if j < len(groups) and group_count > 0 and groups[j] == group_count:
                    ret += helper(i + 1, j + 1, 0)
                elif group_count == 0:
                    ret += helper(i + 1, j, 0)
            else:
                ret += helper(i + 1, j, group_count + 1)
        return ret

    return helper(0, 0, 0)


acc = 0
for row, group in parse_file():
    perms = count_perms(row, group)
    print(row, group, perms)
    acc += perms
print(acc)
