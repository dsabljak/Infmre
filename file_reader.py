"""
    Class for reading data from .txt file
"""
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
