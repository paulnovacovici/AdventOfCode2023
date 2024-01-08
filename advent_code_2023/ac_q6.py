def parse_file():
    lines = open("av_q6.txt", "r").readlines()
    times = map(
        lambda x: int(x),
        filter(
            lambda x: x != "",
            map(lambda t: t.strip(), lines[0].split(":")[1].strip().split(" ")),
        ),
    )
    distances = map(
        lambda x: int(x),
        filter(
            lambda x: x != "",
            map(lambda t: t.strip(), lines[1].split(":")[1].strip().split(" ")),
        ),
    )

    return (list(times), list(distances))


def calculate_distance(init_hold, time) -> int:
    return (time - init_hold) * init_hold


def calculate_button_holds(distance, time) -> int:
    l = 0
    r = time
    lhs = 0
    rhs = 0

    while l < r:
        m = l + (r - l) // 2
        dis = calculate_distance(m, time)
        prev_dis = calculate_distance(m - 1, time)

        if dis > distance and prev_dis <= distance:
            break

        if dis > distance:
            r = m
        else:
            l = m + 1

    lhs = m

    l = 0
    r = time

    while l < r:
        m = l + (r - l) // 2
        dis = calculate_distance(m, time)
        next_dis = calculate_distance(m + 1, time)

        if dis > distance and next_dis <= distance:
            break

        if calculate_distance(m, time) > distance:
            l = m
        else:
            r = m - 1

    rhs = m

    return rhs - lhs + 1


def process_races(times, distances) -> int:
    acc = 1
    for i, time in enumerate(times):
        acc *= calculate_button_holds(distances[i], time)
    print(acc)


times, distances = parse_file()
# print(times, distances)
process_races([42686985], [284100511221341])
