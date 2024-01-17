def parse_file() -> list[list[str]]:
    puzzles = open("ac_q13.txt", "r").read().split("\n\n")
    ret: list[list[str]] = []

    for puzzle in puzzles:
        ret.append(puzzle.split("\n"))

    return ret


def check_col_reflection(puzzle: list[str], col: int, smudges=0) -> bool:
    i = 0
    count_smudges = 0

    while col + i < len(puzzle[0]) and col - i - 1 >= 0:
        left_col = col - i - 1
        right_col = col + i

        for row in puzzle:
            if row[left_col] != row[right_col]:
                count_smudges += 1
        i += 1

    return count_smudges == smudges


def check_row_reflection(puzzle: list[str], row_ref: int, smudges=0) -> bool:
    i = 0
    count_smudges = 0

    while row_ref + i < len(puzzle) and row_ref - i - 1 >= 0:
        top_row = row_ref - i - 1
        bottom_row = row_ref + i

        for col in range(len(puzzle[0])):
            if puzzle[top_row][col] != puzzle[bottom_row][col]:
                count_smudges += 1
        i += 1

    return count_smudges == smudges


puzzles = parse_file()
acc = 0
cols = 0
rows = 0

for puzzle_idx, puzzle in enumerate(puzzles):
    for i in range(1, len(puzzle)):
        if check_row_reflection(puzzle, i, 1):
            print(puzzle_idx, f"row {i}")
            rows += i
    for i in range(1, len(puzzle[0])):
        if check_col_reflection(puzzle, i, 1):
            print(puzzle_idx, f"col {i}")
            cols += i

print(cols + 100 * rows)
