from pathlib import Path

import numpy as np
from networkx import Graph, connected_components, is_connected
from scipy.spatial import distance_matrix
from tqdm import tqdm

input_file = Path(__file__).parent.parent.parent / "data" / "2025" / "day_8.txt"

lamps = np.array(
    [list(map(int, lamp.split(","))) for lamp in input_file.read_text().splitlines()]
)

# lamps = np.array(
#     [
#         list(map(int, lamp.split(",")))
#         for lamp in """162,817,812
# 57,618,57
# 906,360,560
# 592,479,940
# 352,342,300
# 466,668,158
# 542,29,236
# 431,825,988
# 739,650,466
# 52,470,668
# 216,146,977
# 819,987,18
# 117,168,530
# 805,96,715
# 346,949,466
# 970,615,88
# 941,993,340
# 862,61,35
# 984,92,344
# 425,690,689""".splitlines()
#     ]
# )

# plot_lamps()

graph = Graph()
graph.add_nodes_from(list(range(len(lamps))))

dm = distance_matrix(lamps, lamps)
np.fill_diagonal(dm, np.inf)


def find_min_xy(dm: np.ndarray) -> tuple[int, int]:
    linear_index = np.argmin(dm)
    coordinates_rc = np.unravel_index(linear_index, dm.shape)
    row, col = coordinates_rc
    return int(row), int(col)


number_of_links = 0
for i in range(1000):
    a, b = find_min_xy(dm)
    if dm[a, b] == np.inf:
        print("Stopped at", i)
        break

    graph.add_edge(a, b)
    number_of_links += 1

    dm[a, b] = np.inf
    dm[b, a] = np.inf

lengths = sorted([len(c) for c in connected_components(graph)], reverse=True)
print("Part 1:", lengths[0] * lengths[1] * lengths[2])

graph = Graph()
graph.add_nodes_from(list(range(len(lamps))))
a, b = None, None
while not is_connected(graph):
    a, b = find_min_xy(dm)

    graph.add_edge(a, b)

    dm[a, b] = np.inf
    dm[b, a] = np.inf

# print(a, b)
# print(lamps[a], lamps[b])
print("Part 2:", lamps[a][0] * lamps[b][0])
