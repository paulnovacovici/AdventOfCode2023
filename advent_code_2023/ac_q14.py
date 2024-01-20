def parse_file() -> list[str]:
    return open("ac_q14.txt", "r").read().split("\n")


def moves_north(dish: list[str]):
    moves = [[0] * len(dish[0]) for i in range(len(dish) + 1)]

    for i, row in enumerate(dish):
        for j, char in enumerate(row):
            if char == "O":
                moves[i + 1][j] = moves[i][j]
            if char == "#":
                moves[i + 1][j] = 0
            if char == ".":
                moves[i + 1][j] = moves[i][j] + 1
    return moves


def process_move_north(dish: list[str]):
    acc = 0
    moves = moves_north(dish)

    for i, row in enumerate(dish):
        for j, char in enumerate(row):
            if char == "O":
                acc += len(dish) - (i - moves[i + 1][j])
    print(acc)


moves_north(parse_file())
