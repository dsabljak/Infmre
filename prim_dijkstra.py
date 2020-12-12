class FileReader:

    def __init__(self, path):
        self.file = open(path, 'r')
        self.nodes = set()
        self.edges = []
        self.edge_cost = dict()

        self.parse()

    """
        Data is written in .txt file like:
        begin_node, end_node, cost, direction;
        This method parses all rows of file and saves data
    """
    def parse(self):
        data = self.file.readlines()

        for row in data:
            begin_node = row.split(',')[0]
            end_node = row.split(', ')[1]
            edge = begin_node + end_node
            cost = int(row.split(', ')[2])
            direct = row.split(', ')[3].split(';')[0]
            self.nodes.add(begin_node)
            self.nodes.add(end_node)
            self.edges.append(edge)

            # If cost is 0, ignore it
            # Maybe not the best way?
            if cost != 0:
                self.edge_cost[edge] = cost

            # If direction is not directed, then create simetric edge
            # For example AB -> BA
            if direct == 'n':
                self.edge_cost[edge[::-1]] = cost

        print(self.nodes)
        print(self.edges)
        print(self.edge_cost)

# Function for getting all possible combinations for edges by nodes
# For example [a, b] returns set {bb, aa, ab, ba} (using set to avoid redundancy)
def get_all(nodes):
    return set([x + y for x in nodes for y in nodes] + [y + x for x in nodes for y in nodes])

path = input("Insert path to file with data:")
data = FileReader(path)

nodes = data.nodes
edges = data.edges
edge_cost = data.edge_cost

used_nodes = []
used_edges = []

current_node = nodes.pop()
used_nodes.append(current_node)
print(f"Odabrani početak: {current_node}")

total_cost = 0
temp_edge_cost = dict()     # on class this is "dist" in table
while len(nodes) != 0:
    print(f"Neobiđeni vrhovi: {nodes}")
    for edge in edge_cost.keys():
        if current_node == edge[0]:
            if edge[1] not in used_nodes:   # if watched node is already in used nodes, we do not need it
                print(f"Rub koji razmatram: {edge}")
                print(f"Vrh koji razmatram: {edge[1]}")
                print(f"Obiđeni vrhovi: {used_nodes}")
                temp_edge_cost[edge] = edge_cost[edge]

    print(f"Ovo su privremeni vrhovi i udaljenosti: {temp_edge_cost}")
    min_edge = min(temp_edge_cost, key=temp_edge_cost.get)
    print(f"Minimalnu udaljenost ima: {min_edge} s udaljenosti {edge_cost[min_edge]}")

    print(f"Ovo su iskorišteni bridovi: {used_edges}")
    if min_edge not in used_edges or min_edge[::-1] not in used_edges:      # checking edge witch is being added and it's simetric also, if not used already, add it
        print(f"{min_edge} i {min_edge[::-1]} nije u {used_edges} pa ga dodajem")
        used_edges.append(min_edge)
        print(f"Sada iskoristeni bridovi zgledaju ovako: {used_edges}")

    print(f"Nema smisla cuvati {min_edge} i {min_edge[::-1]} u privremenim udaljenostima: {temp_edge_cost} pa ga izbacujem")
    temp_edge_cost.pop(min_edge)        #need to delete that edge from "dist" column to avoid using it again later
    try:
        temp_edge_cost.pop(min_edge[::-1])
    except:
        pass

    print(f"Sada izgledaju ovako: {temp_edge_cost}")
    total_cost += int(edge_cost[min_edge])

    current_node = min_edge[1]
    print(f"Trenutni vrh je: {current_node}")

    used_nodes.append(current_node)
    print(f"Iskorišteni vrhovi su sada: {used_nodes}")

    edges_for_deletion = set(get_all(list(used_nodes)))     # combining all used nodes to get edges which need to be deleted so they don't get used again later
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
