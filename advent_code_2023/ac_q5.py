from collections import namedtuple
import re
import sys

MapRange = namedtuple("MapRange", ["dest", "src", "range"])


def update_seeds(seed_id: int, seeds: list[int], new_seeds: [int], map: MapRange):
    if seed_id >= map.src and seed_id < map.src + map.range:
        new_seeds.append(map.dest + (seed_id - map.src))
    else:
        seeds.insert(0, seed_id)


def merge_dicts(d1: dict, d2: dict) -> dict:
    d = {}
    for k, v in d1.items():
        d[k] = v
    for k, v in d2.items():
        d[k] = v
    return d


def create_map_range_from_line(line: str) -> MapRange:
    dest, src, range = line.split(" ")
    return MapRange(int(dest), int(src), int(range))


def parse_file2() -> tuple[list[int], list[list[MapRange]]]:
    lines = open("av_q5.txt", "r").read()
    segments = lines.split("\n\n")
    _, seed_ids = segments[0].split(":")
    seeds = [int(seed.strip()) for seed in seed_ids.strip().split(" ")]

    groups = []

    for batch in segments[1::]:
        lines = batch.split("\n")
        # removing desc
        batch = lines[1::]
        maps = []
        for map in batch:
            maps.append(create_map_range_from_line(map))
        groups.append(maps)

    return seeds, groups


def parse_file() -> dict[int, int]:
    with open("av_q5.txt", "r") as file:
        ret = {}
        seeds = file.readline()
        _, seed_ids = seeds.split(":")
        for seed in seed_ids.strip().split(" "):
            seed = seed.strip()
            ret[int(seed)] = int(seed)

        line = file.readline()
        while line != "":
            if re.match(r"^\w", line):
                line = file.readline()
                new_map = {}
                while re.match(r"^\d", line):
                    map_range = create_map_range_from_line(line)
                    new_map = merge_dicts(new_map, get_new_seed_map(ret, map_range))
                    line = file.readline()
                ret = merge_dicts(ret, new_map)

            line = file.readline()

        return ret


def process_p1() -> int:
    seeds, groups = parse_file2()

    for group in groups:
        new_seeds = []
        for map in group:
            i = 0
            length = len(seeds)
            while i < length:
                seed = seeds.pop()
                update_seeds(seed, seeds, new_seeds, map)
                i += 1
        seeds.extend(new_seeds)

    acc = sys.maxsize
    for value in seeds:
        acc = min(acc, value)
    print(acc)


# mappings = parse_file()
# ret = sys.maxsize

# for _, value in mappings.items():
#     ret = min(ret, value)
# print(ret)

process_p1()
