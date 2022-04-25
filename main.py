string_nodes = "x1,x2,x3,x4,x5,x6,x7,x8"

string_links = "x1,x2,1\n" \
               "x2,x3,A23\n" \
               "x3,x4,A34\n" \
               "x4,x5,A45\n" \
               "x5,x6,A56\n" \
               "x6,x7,A67\n" \
               "x7,x8,1\n" \
               "x7,x6,A76\n" \
               "x6,x5,A65\n" \
               "x5,x4,A54\n" \
               "x4,x3,A43\n" \
               "x3,x2,A32\n" \
               "x2,x4,A24\n" \
               "x7,x5,A75\n" \
               "x7,x7,A77\n" \
               "x2,x7,A27"


def get_path(temp_graph, start, end, temp_path=None):
    if temp_path is None:
        temp_path = []
    temp_path = temp_path + [start]
    if start.__eq__(end):
        return temp_path
    if start not in graph:
        return None
    for node in temp_graph[start]:
        if node not in temp_path:
            new_path = get_path(temp_graph, node, end, temp_path)
            if new_path is not None:
                return new_path
    return None


def find_all_paths(temp_graph, start, end, temp_path=None):
    global new_paths
    if temp_path is None:
        temp_path = []

    temp_path = temp_path + [start]
    if start.__eq__(end):
        return [temp_path]
    if start not in graph:
        return None

    paths = []
    for node in temp_graph[start]:
        if node not in temp_path:
            new_paths = find_all_paths(temp_graph, node, end, temp_path)
        for new_path in new_paths:
            if new_path not in paths:
                paths.append(new_path)
    return paths


def build_graph(links, temp_nodes):
    temp_graph = {}
    for node in temp_nodes:
        temp_graph[node] = []
    for x, y, z in links:
        temp_graph[x].append(y)
    return temp_graph


def str_to_list(string_directions):
    directions_as_list = []
    for line in string_directions.split("\n"):
        temp = line.split(",")
        if len(temp) == 3:
            directions_as_list.append(line.split(","))
    return directions_as_list


def find_all_cycles(temp_graph):
    pass


def find_cycle(temp_graph, node, temp_path=None):
    if node is None:
        return None
    if temp_path is None:
        temp_path = []

    if node in temp_path:
        if node.__eq__(temp_path[0]):
            return temp_path.append(node)

    temp_path.append(node)

    if len(temp_graph[node]) == 0:
        return None

    for child in temp_graph[node]:
        new_path = find_cycle(temp_graph, child, temp_path)
        if new_path is not None:
            return new_path

def find_cyclic(graph, node):
    paths = []
    current_path = []
    visited = []
    queue = []
    visited.append(node)
    queue.append(node)

    while (queue):
        m = queue.pop(0)
        print(m, end=" ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
            else:
                if visited[0].__eq__(neighbour):
                    paths.append(visited)




if __name__ == '__main__':
    nodes = string_nodes.split(",")
    directions = str_to_list(string_links)
    graph = build_graph(directions, nodes)
    # for i in graph:
    #     print(f"{i} --> {graph[i]}")
    # print("@@@@@@@@@@@@@@@")
    # print(get_path(graph, nodes[0], nodes[7]))
    # print("@@@@@@@@@@@@@@@")
    print(find_cycle(graph, nodes[3]))
