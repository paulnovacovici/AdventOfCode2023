import re


def find_all_numbers(s: str) -> list[int]:
    return [m for m in re.findall(r"(\d+)", s)]


def parse_file() -> list[list[str]]:
    with open("ac_q4.txt", "r") as file:
        ret = []
        for line in file:
            line = line.strip()
            (_, output) = line.split(":")
            winning, numbers = output.split("|")
            winning = set(find_all_numbers(winning))
            numbers = set(find_all_numbers(numbers))
            ret.append((winning, numbers))
        return ret


def process_card_p1(winning: list[str], numbers: list[str]) -> int:
    winners = 0
    for num in numbers:
        if num in winning:
            winners += 1
    if winners == 0:
        return 0

    return 2 ** (winners - 1)


def process_cards_p1(cards: list[tuple[int, int]]) -> int:
    acc = 0
    for winning, nums in cards:
        acc += process_card_p1(winning, nums)
    return acc


def process_card_p2(winning: list[str], numbers: list[str]) -> int:
    winners = 0
    for num in numbers:
        if num in winning:
            winners += 1
    return winners


def process_cards_p2(cards: list[tuple[int, int]]) -> int:
    res = {}
    for i, _ in enumerate(cards):
        res[i] = 1
    for i, (winning, nums) in enumerate(cards):
        winners = process_card_p2(winning, nums)
        for j in range(winners):
            res[i + j + 1] = res.get(i + j + 1, 1) + res[i]

    acc = 0
    for _, copies in res.items():
        acc += copies
    return acc


cards = parse_file()
print(process_cards_p2(cards))
