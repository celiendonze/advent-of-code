from pathlib import Path

import networkx as nx

input_path = Path(__file__).parent.parent.parent / "data/2025/day_11.txt"

lines = input_path.read_text().splitlines()

graph = nx.DiGraph()
for line in lines:
    input_node, output_nodes = line.split(":")
    input_node = input_node.strip()
    output_nodes = [n.strip() for n in output_nodes.split(" ") if n.strip()]
    for output_node in output_nodes:
        graph.add_edge(input_node, output_node)


print("Part 1:", len(list(nx.all_simple_paths(graph, "you", "out"))))

print("Is Directed Acyclic Graph:", nx.is_directed_acyclic_graph(graph))


def count_paths_dag(graph: nx.DiGraph, source: str, target: str) -> int:
    topo_order = list(nx.topological_sort(graph))
    forward_reachable = nx.descendants(graph, source)
    forward_reachable.add(source)
    backward_reachable = nx.ancestors(graph, target)
    backward_reachable.add(target)
    reachable_nodes = forward_reachable.intersection(backward_reachable)
    topo_order = [n for n in topo_order if n in reachable_nodes]

    path_counts = {node: 0 for node in graph.nodes()}
    path_counts[source] = 1
    for node in topo_order:
        if path_counts[node] > 0:
            for neighbor in graph.successors(node):
                path_counts[neighbor] += path_counts[node]
    return path_counts[target]


total_2 = (
    count_paths_dag(graph, "svr", "fft")
    * count_paths_dag(graph, "fft", "dac")
    * count_paths_dag(graph, "dac", "out")
) + (
    count_paths_dag(graph, "svr", "dac")
    * count_paths_dag(graph, "dac", "fft")
    * count_paths_dag(graph, "fft", "out")
)
print("Part 2:", total_2)
