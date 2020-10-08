from file_reader import FileReader

# recursive function for checking whether the loop has occurred
# uses edge we want to add split to beginning_node and end_node
# and list of all used edges
# it tries to connect all edges and looks if the beginning_node will be the
# end node at some point. If yes, then it's a loop.
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
        if i[0] == end_node:            # if current beginning node is same as previous end node then check if current edge is in loop
            print(f"Beg_node: {beginning_node}")
            print(f"End_node: {end_node}")
            print(i)
            avoid_loop_edges_copy = avoid_loop_edges[::-1]
            avoid_loop_edges_copy.remove(i)         # removing edge because of infinite loop
            try:
                avoid_loop_edges.remove(i[::-1])
            except:
                pass

            if loop(beginning_node, i[1], avoid_loop_edges_copy):  # if the loop occurres at some point, return with that info
                return True

    return False

data = FileReader('test_data1')

nodes = data.nodes
edges = data.edges
edge_cost = data.edge_cost
sorted_edges = {k: v for k, v in sorted(edge_cost.items(), key=lambda item: item[1])}  # sorting edges by cost
print(sorted_edges)
print(sorted_edges.keys())
used_edges = []
total_cost = 0

for edge in list(sorted_edges.keys()):          # going through sorted edges and adding them to used if they are not in loop

    if edge[::-1] in used_edges:
        continue

    if not loop(edge[0], edge[1], used_edges[::]):
        used_edges.append(edge)
        used_edges.append(edge[::-1])
        total_cost += sorted_edges[edge]

    else:
        print(f"Nisam dodao {edge} jer stvara petlju")

for i in used_edges:        # remove simetric edges
    if i[::-1] in used_edges:
        used_edges.remove(i[::-1])

print(used_edges)
print(total_cost)
