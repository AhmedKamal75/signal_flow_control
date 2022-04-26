class Graph:
    def __init__(self, edges):
        self._edges = edges
        self._graph_dic = {}
        self._cycles = []
        self._paths = []
        for start, end in self.edges:
            if start in self.graph_dic:
                self.graph_dic[start].append(end)
            else:
                self.graph_dic[start] = [end]
            if end not in self.graph_dic:
                self.graph_dic[end] = []

    @property
    def paths(self):
        return self._paths

    @paths.setter
    def paths(self, paths):
        self._paths = paths

    @property
    def cycles(self):
        return self._cycles

    @cycles.setter
    def cycles(self, cycles):
        self._cycles = cycles

    @property
    def graph_dic(self):
        return self._graph_dic

    @graph_dic.setter
    def graph_dic(self, graph_dic):
        self._graph_dic = graph_dic

    @property
    def edges(self):
        return self._edges

    @edges.setter
    def edges(self, edges):
        self._edges = edges

    def build_paths(self):
        temp_list = list(self.graph_dic.keys())
        self.paths = self.get_paths(temp_list[0], temp_list[-1])

    def get_paths(self, start, end, path=None):
        if path is None:
            path = []
        path = path + [start]

        if start == end:
            return [path]

        if not self.graph_dic[start]:
            return []

        paths = []

        for node in self.graph_dic[start]:
            if node not in path:
                new_paths = self.get_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)
        return paths

    def remove_doublicate_cycles(self, gain_list):
        new_cycles = []
        cases = [True for _ in range(0, len(self.cycles), 1)]
        for i in range(0, len(self.cycles), 1):
            if cases[i]:
                for j in range(0, len(self.cycles), 1):
                    cycle_1 = self.cycles[i][0:-1].copy()
                    cycle_2 = self.cycles[j][0:-1].copy()
                    if (i != j) and (cases[j]) and (sorted(cycle_1) == sorted(cycle_2)) and (
                            sorted(get_gain_of(gain_list, cycle_1)) != sorted(get_gain_of(gain_list, cycle_2))):
                        cases[j] = False
        for i, case in enumerate(cases, 0):
            if case:
                new_cycles.append(self.cycles[i])
        self.cycles = new_cycles

    def build_cycles(self, gain_list):
        for node in self.graph_dic.keys():
            temp_cycles = self.get_cycles_for_node(node=node, goal=node)
            for temp_cycle in temp_cycles:
                if temp_cycle not in self.cycles:
                    self.cycles.append(temp_cycle)
        self.remove_doublicate_cycles(gain_list)

    def get_cycles_for_node(self, node, goal, path=None, temp_started=True):
        if path is None:
            path = []
        if not node:
            return []

        path = path + [node]

        if node == goal and (not temp_started):
            return [path]

        temp_started = False

        paths = []

        for new_node in self.graph_dic[node]:
            if (new_node not in path) or new_node == goal:
                new_paths = self.get_cycles_for_node(new_node, goal, path, temp_started)
                for p in new_paths:
                    if p not in paths:
                        paths.append(p)

        return paths


def run(string_links):
    gain_list = edges_transformations(string_links, True)
    edge = edges_transformations(string_links)
    temp_graph = Graph(edge)
    temp_graph.build_paths()
    temp_graph.build_cycles(gain_list)
    for i in temp_graph.paths:
        print(f"{get_gain_of(gain_list, i)} --> {i}")
    print("@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@")
    for i in temp_graph.cycles:
        print(f"{get_gain_of(gain_list, i)} --> {i}")


def edges_transformations(string_directions, with_gain=False):
    result = None
    if with_gain:
        result = {}
    else:
        result = []

    for line in string_directions.split("\n"):
        temp = line.split(",")
        if len(temp) == 3:
            temp_edge = line.split(",")
            if with_gain:
                result[(temp_edge[0], temp_edge[1])] = temp_edge[2]
            else:
                result.append((temp_edge[0], temp_edge[1]))
    return result


def get_gain_of(gains_list, path=None):
    if len(path) < 2:
        return None
    total_gain = []
    for i in range(0, len(path) - 1, 1):
        total_gain = total_gain + [gains_list[(path[i], path[i + 1])]]
    return total_gain


if __name__ == "__main__":
    # string_nodes = "x1,x2,x3,x4,x5,x6,x7,x8"
    # input_string = "x1,x2,1\n" \
    #                "x2,x3,A23\n" \
    #                "x3,x4,A34\n" \
    #                "x4,x5,A45\n" \
    #                "x5,x6,A56\n" \
    #                "x6,x7,A67\n" \
    #                "x7,x8,1\n" \
    #                "x7,x6,A76\n" \
    #                "x6,x5,A65\n" \
    #                "x5,x4,A54\n" \
    #                "x4,x3,A43\n" \
    #                "x3,x2,A32\n" \
    #                "x2,x4,A24\n" \
    #                "x7,x5,A75\n" \
    #                "x7,x7,A77\n" \
    #                "x2,x7,A27"
    input_string = "x1,x2,1\n" \
                   "x2,x3,G1G4\n" \
                   "x3,x4,G2\n" \
                   "x4,x5,1\n" \
                   "x5,x6,1\n" \
                   "x3,x2,H1\n" \
                   "x3,x4,G3\n" \
                   "x5,x2,-H2"
    # input_string = "x1,x2,1\n" \
    #                "x2,x3,G1G2\n" \
    #                "x3,x4,G4\n" \
    #                "x3,x4,"
    run(input_string)
