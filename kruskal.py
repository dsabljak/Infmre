from file_reader import FileReader

def loop(beginning_node, end_node, avoid_loop_edges):
    print(f"Kruskal avoid: {avoid_loop_edges}")
    print(f"{beginning_node + end_node}")
    if len(avoid_loop_edges) == 0:
        return False

    if beginning_node == end_node:
        return True

    for i in avoid_loop_edges:
        print(f"Trenutni avoid: {avoid_loop_edges}")
        print(f"Ovo je i: {i}")
        if i[0] == end_node:
            print(f"Beg_node: {beginning_node}")
            print(f"End_node: {end_node}")
            print(i)
            avoid_loop_edges_copy = avoid_loop_edges[::-1]
            avoid_loop_edges_copy.remove(i)
            try:
                avoid_loop_edges.remove(i[::-1])
            except:
                pass

            if loop(beginning_node, i[1], avoid_loop_edges_copy):
                return True

    return False

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
    print("NOVI")

    if edge[::-1] in used_edges:
        continue

    if edge[0] not in used_nodes or edge[1] not in used_nodes:
        used_nodes.add(edge[0])
        used_nodes.add(edge[1])
        used_edges.append(edge)
        used_edges.append(edge[::-1])
        total_cost += sorted_edges[edge]
        print(f"Iskoristeni : {used_edges}")

    elif not loop(edge[0], edge[1], used_edges[::]):
        used_nodes.add(edge[0])
        used_nodes.add(edge[1])
        used_edges.append(edge)
        used_edges.append(edge[::-1])
        total_cost += sorted_edges[edge]

    else:
        print(f"Nisam dodao {edge} jer stvara petlju")

for i in used_edges:
    if i[::-1] in used_edges:
        used_edges.remove(i[::-1])

print(used_nodes)
print(used_edges)
print(total_cost)