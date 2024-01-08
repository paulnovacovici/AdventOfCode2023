def parse_line(line: str):
    game_number_str, color_counts_str = line.split(":")

    # Extracting the game number
    game_number = int(game_number_str.split(" ")[1])

    # Splitting the color counts into separate groups
    groups = color_counts_str.split(";")

    # Parsing each group
    parsed_data = []
    for group in groups:
        # Splitting each group into color-count pairs
        color_count_pairs = group.split(",")

        # Parsing each color-count pair and storing in a dictionary
        group_dict = {}
        for pair in color_count_pairs:
            parts = pair.strip().split(" ")
            if len(parts) == 2:  # Checking if the pair is valid
                count, color = int(parts[0]), parts[1]
                group_dict[color] = count
        parsed_data.append(group_dict)
    return game_number, parsed_data


def process_game_data(picks: list[dict]):
    ret = {}

    for colors in picks:
        for color, value in colors.items():
            ret[color] = max(ret.get(color, 0), value)
    return ret


def part1():
    with open("ac_q2.txt", "r") as file:
        acc = 0
        results = {"red": 12, "green": 13, "blue": 14}
        for line in file:
            game_num, picks = parse_line(line)
            max_colors = process_game_data(picks)
            flag = True
            for color, num in results.items():
                flag &= max_colors.get(color, 0) <= num
            if flag:
                acc += game_num
            else:
                print(max_colors)
        print(acc)


def part2():
    with open("ac_q2.txt", "r") as file:
        acc = 0
        for line in file:
            game_num, picks = parse_line(line)
            max_colors = process_game_data(picks)
            power = 1
            for _, val in max_colors.items():
                power *= val
            acc += power

        print(acc)


if __name__ == "__main__":
    part2()
