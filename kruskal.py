from file_reader import FileReader



data = FileReader('test_data1')

nodes = data.nodes
edges = data.edges
edge_cost = data.edge_cost
sorted_edges = {k: v for k, v in sorted(edge_cost.items(), key=lambda item: item[1])}
print(sorted_edges)
print(sorted_edges.keys())
used_nodes = set()
used_edges = []
total_cost = 0
for edge in list(sorted_edges.keys()):

    if edge[0] not in used_nodes or edge[1] not in used_nodes:
        used_nodes.add(edge[0])
        used_nodes.add(edge[1])
        used_edges.append(edge)
        total_cost += sorted_edges[edge]
    else:
        if not loop(edge[0], edge[1], used_edges):
            used_nodes.add(edge[0])
            used_nodes.add(edge[1])
            used_edges.append(edge)
            total_cost += sorted_edges[edge]

print(used_nodes)
print(used_edges)
print(total_cost)