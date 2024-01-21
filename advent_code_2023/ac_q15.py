def parse_file() -> list[str]:
    return open("ac_q15.txt", "r").read().split(",")


def calc_hash(s: str) -> int:
    acc = 0
    for c in s:
        acc += ord(c)
        acc *= 17
        acc %= 256
    return acc


acc = 0
for s in parse_file():
    print(s, calc_hash(s))
    acc += calc_hash(s)

print(acc)
