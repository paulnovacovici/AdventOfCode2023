def print_graph(graph: list[list[str]]):
    for _, row in enumerate(graph):
        for _, char in enumerate(row):
            print(char, end="")
        print()


def parse_file() -> list[list[str]]:
    graph = open("ac_q11.txt", "r").read().split("\n")
    empty_rows = set()
    empty_cols = set()

    for i, row in enumerate(graph):
        if all(map(lambda x: x == ".", row)):
            empty_rows.add(i)

    for col in range(len(graph[0])):
        empty = True
        for row in range(len(graph)):
            if graph[row][col] != ".":
                empty = False
        if empty:
            empty_cols.add(col)
    return graph, empty_cols, empty_rows


def find_all_shortest_paths(
    graph: list[list[str]], empty_cols: set[int], empty_rows: set[int], scale: int = 1
) -> int:
    galxies = set()
    distances = {}

    for y, row in enumerate(graph):
        for x, char in enumerate(row):
            if char == "#":
                x_gaps = len([empty_col for empty_col in empty_cols if empty_col < x])
                y_gaps = len([empty_row for empty_row in empty_rows if empty_row < y])
                galxies.add((x + x_gaps * scale, y + y_gaps * scale))

    for g1 in galxies:
        for g2 in galxies:
            if (g2, g1) not in distances and g1 != g2:
                distances[(g1, g2)] = abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])
    return sum(distances.values())


print(find_all_shortest_paths(*parse_file(), 1000000 - 1))
