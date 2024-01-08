from functools import reduce
from math import lcm


def parse_file():
    lines = open("av_q8.txt", "r").readlines()
    inst = lines[0].strip()
    graph = {}

    for line in lines[2::]:
        node, rest = line.strip().split("=")
        left, right = rest.replace("(", "").replace(")", "").split(",")
        graph[node.strip()] = (left.strip(), right.strip())
    return inst, graph


def is_terminal(curs: list[str]) -> bool:
    for cur in curs:
        if not cur.endswith("Z"):
            return False
    return True


def next_node(
    node: str, graph: dict[str, tuple[str, str]], inst: list[str], i: int
) -> str:
    next_dir = inst[i % len(inst)]
    if next_dir == "L":
        node = graph[node][0]
    else:
        node = graph[node][1]
    return node


def find_cycle(node: str, graph: dict[str, tuple[str, str]], inst: list[str]) -> int:
    i = 0
    start_node = node

    while True:
        if node.endswith("Z"):
            print(
                next_node(start_node, graph, inst, 1), next_node(node, graph, inst, i)
            )
            return i
        next_dir = inst[i % len(inst)]
        if next_dir == "L":
            node = graph[node][0]
        else:
            node = graph[node][1]
        i += 1


def traverse_graph(inst, graph: dict[str, tuple[str, str]]) -> int:
    cur_nodes = list(
        filter(lambda node: node.endswith("A"), [key for key, _ in graph.items()])
    )
    cycles = []

    for node in cur_nodes:
        cycles.append(find_cycle(node, graph, inst))
    print(cur_nodes)
    print(cycles)
    print(reduce(lcm, cycles))


traverse_graph(*parse_file())
