def parse_file():
    lines = open("ac_q9.txt", "r").read().split("\n")

    return list(
        map(lambda line: list(map(lambda x: int(x), line.strip().split(" "))), lines)
    )


def process_game(seq: list[str]) -> int:
    is_equal = False
    first_num = []

    while not is_equal:
        first_num.append(seq[0])
        print(seq)
        i = 0
        new_seq = []
        while i < len(seq) - 1:
            new_seq.append(seq[i + 1] - seq[i])
            i += 1
        is_equal = all(map(lambda x: x == 0, new_seq))
        seq = new_seq
    acc = 0
    for num in first_num[::-1]:
        acc = num - acc
    return acc


seqs = parse_file()
acc = 0
for game in seqs:
    acc += process_game(game)
print(acc)
