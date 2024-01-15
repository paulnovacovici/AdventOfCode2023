from enum import Enum
from queue import Queue
from sys import setrecursionlimit


class Directions(Enum):
    HORIZONTAL = 1
    VERTICAL = 2
    RIGHT_UP = 3
    LEFT_UP = 4
    LEFT_DOWN = 5
    RIGHT_DOWN = 6
    GROUND = 7
    START = 8


directions_map = {
    Directions.HORIZONTAL: [(1, 0), (-1, 0)],
    Directions.VERTICAL: [(0, 1), (0, -1)],
    Directions.RIGHT_UP: [(1, 0), (0, -1)],
    Directions.LEFT_UP: [(-1, 0), (0, -1)],
    Directions.LEFT_DOWN: [(-1, 0), (0, 1)],
    Directions.RIGHT_DOWN: [(1, 0), (0, 1)],
    Directions.START: [(1, 0), (0, -1), (-1, 0), (0, 1)],
    Directions.GROUND: [],
}


class Node:
    def __init__(self, loc, dir):
        self.loc = loc
        self.dir = dir
        self.edges = set()
        self.is_cycle = False

    def add_bidirectional_edge(self, node):
        """Add a bidirectional edge between this node and another node."""
        self.edges.add(node)
        node.edges.add(self)

    def __repr__(self):
        return f"Node({self.loc})"


def parse_file() -> list[list[Node]]:
    lines = open("ac_q10.txt", "r").read().split("\n")
    output = []

    for y, line in enumerate(lines):
        row = []
        for x, dir in enumerate(line):
            if dir == "|":
                row.append(Node((x, y), Directions.VERTICAL))
            elif dir == "-":
                row.append(Node((x, y), Directions.HORIZONTAL))
            elif dir == "L":
                row.append(Node((x, y), Directions.RIGHT_UP))
            elif dir == "J":
                row.append(Node((x, y), Directions.LEFT_UP))
            elif dir == "7":
                row.append(Node((x, y), Directions.LEFT_DOWN))
            elif dir == "F":
                row.append(Node((x, y), Directions.RIGHT_DOWN))
            elif dir == ".":
                row.append(Node((x, y), Directions.GROUND))
            elif dir == "S":
                row.append(Node((x, y), Directions.START))
            else:
                print("ERROR: Shouldn't be here")
        output.append(row)
    return output


def add_node_edges(pipes: list[list[Node]], row: int, col: int):
    node = pipes[row][col]
    dirs = directions_map[node.dir]
    for x_inc, y_inc in dirs:
        print(x_inc, y_inc)
        print(
            pipes[row + y_inc][col + x_inc],
            directions_map[pipes[row + y_inc][col + x_inc].dir],
        )
        if (
            col + x_inc < len(pipes[row])
            and col + x_inc >= 0
            and row + y_inc < len(pipes)
            and row + y_inc >= 0
            and (-x_inc, -y_inc) in directions_map[pipes[row + y_inc][col + x_inc].dir]
        ):
            node.add_bidirectional_edge(pipes[row + y_inc][col + x_inc])


def create_graph(pipes: list[list[Node]]):
    start = None
    for row in range(len(pipes)):
        for col in range(len(pipes[row])):
            node = pipes[row][col]
            dirs = directions_map[node.dir]
            if node.dir == Directions.START:
                start = node
            for x_inc, y_inc in dirs:
                if (
                    col + x_inc < len(pipes[row])
                    and col + x_inc >= 0
                    and row + y_inc < len(pipes)
                    and row + y_inc >= 0
                    and (-x_inc, -y_inc)
                    in directions_map[pipes[row + y_inc][col + x_inc].dir]
                ):
                    node.add_bidirectional_edge(pipes[row + y_inc][col + x_inc])
    return start


def cycle_detection(start: Node):
    visited = set()

    def dfs(prev: Node, node: Node):
        if node in visited:
            return False
        if node.dir == Directions.START:
            return True

        visited.add(node)

        for child in node.edges:
            if child != prev:
                ret = dfs(node, child)
                node.is_cycle = ret
                return ret

        return False

    start.is_cycle = True
    for node in start.edges:
        dfs(start, node)


def process_maze(pipes: list[list[Node]]):
    start = create_graph(pipes)
    cycle_detection(start)

    queue = Queue()
    queue.put((start, 0))
    visited = set()
    ret = 0

    while not queue.empty():
        (node, depth) = queue.get()
        if node in visited or not node.is_cycle:
            continue
        visited.add(node)
        ret = max(ret, depth)

        for edge in node.edges:
            queue.put((edge, depth + 1))
    return ret


def print_graph(pipes: list[list[Node]]):
    for i in range(len(pipes)):
        for j in range(len(pipes[i])):
            print("x" if pipes[i][j].is_cycle else ".", end="")
        print()


def process_part_2(pipes: list[list[Node]]):
    start = create_graph(pipes)
    cycle_detection(start)
    print_graph(pipes)
    within = False
    tiles = 0

    for i in range(len(pipes)):
        for j in range(len(pipes[i])):
            if pipes[i][j].is_cycle and pipes[i][j].dir in [
                Directions.LEFT_UP,
                Directions.VERTICAL,
                Directions.RIGHT_UP,
            ]:
                within = not within
            elif not pipes[i][j].is_cycle and within:
                tiles += 1
    return tiles


setrecursionlimit(30000)


pipes = parse_file()
start = process_part_2(pipes)
# add_node_edges(pipes, 2, 1)
# print(pipes[2][1].edges)

print(start)
