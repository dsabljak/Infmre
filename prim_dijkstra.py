from file_reader import FileReader

def get_all(nodes):
    return [x + y for x in nodes for y in nodes] + [y + x for x in nodes for y in nodes]

data = FileReader('test_data1')

nodes = data.nodes
edges = data.edges
edge_cost = data.edge_cost

used_nodes = []
used_edges = []

current_node = nodes.pop()
used_nodes.append(current_node)
print(f"Odabrani početak: {current_node}")

total_cost = 0
temp_edge_cost = dict()
while len(nodes) != 0:
    print(f"Neobiđeni vrhovi: {nodes}")
    for edge in edge_cost.keys():
        if current_node == edge[0]:
            if edge[1] not in used_nodes:
                print(f"Rub koji razmatram: {edge}")
                print(f"Vrh koji razmatram: {edge[1]}")
                print(f"Obiđeni vrhovi: {used_nodes}")
                temp_edge_cost[edge] = edge_cost[edge]

    print(f"Ovo su privremeni vrhovi i udaljenosti: {temp_edge_cost}")
    min_edge = min(temp_edge_cost, key=temp_edge_cost.get)
    print(f"Minimalnu udaljenost ima: {min_edge} s udaljenosti {edge_cost[min_edge]}")

    print(f"Ovo su iskorišteni bridovi: {used_edges}")
    if min_edge not in used_edges or min_edge[::-1] not in used_edges:
        print(f"{min_edge} i {min_edge[::-1]} nije u {used_edges} pa ga dodajem")
        used_edges.append(min_edge)
        print(f"Sada iskoristeni bridovi zgledaju ovako: {used_edges}")

    print(f"Nema smisla cuvati {min_edge} i {min_edge[::-1]} u privremenim udaljenostima: {temp_edge_cost} pa ga izbacujem")
    temp_edge_cost.pop(min_edge)
    try:
        temp_edge_cost.pop(min_edge[::-1])
    except:
        pass

    print(f"Sada izgledaju ovako: {temp_edge_cost}")
    total_cost += int(edge_cost[min_edge])


    current_node = min_edge[1]
    print(f"Trenutni vrh je: {current_node}")
    ##+pobristati veze

    used_nodes.append(current_node)
    print(f"Iskorišteni vrhovi su sada: {used_nodes}")

    edges_for_deletion = set(get_all(list(used_nodes)))
    print(f"Treba pobrisati: {edges_for_deletion}")
    for edge_for_deletion in edges_for_deletion:
        try:
            temp_edge_cost.pop(edge_for_deletion)
        except:
            pass
    print(f"Nakon brisanja: {temp_edge_cost}")
    nodes.remove(current_node)

print(used_edges)
print(total_cost)