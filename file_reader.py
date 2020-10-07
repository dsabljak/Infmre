
class FileReader:

    def __init__(self, path):
        self.file = open(path, 'r')
        self.nodes = set()
        self.edges = []
        self.edge_cost = dict()

        self.parse()

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
            if cost != 0:
                self.edge_cost[edge] = cost

            if direct == 'n':
                self.edge_cost[edge[::-1]] = cost

        print(self.nodes)
        print(self.edges)
        print(self.edge_cost)
