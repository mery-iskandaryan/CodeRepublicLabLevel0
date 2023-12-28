class Vertex:
    def __init__(self, key):
        self.key = key
        self.neighbors = []

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def remove_neighbor(self, neighbor):
        self.neighbors.remove(neighbor)


class Graph:
    def __init__(self):
        self.vertex_dict = {}
        self.size = 0

    def add_vertex(self, key):
        self.size += 1
        vertex = Vertex(key)
        self.vertex_dict[key] = vertex

    def add_edges(self, key1, key2):

        if key1 not in self.vertex_dict or key2 not in self.vertex_dict:
            raise ValueError("Key is not present...")
        self.vertex_dict.get(key1).add_neighbor(key2)
        self.vertex_dict.get(key2).add_neighbor(key1)

    def remove_vertex(self, key):
        self.size -= 1
        if key not in self.vertex_dict:
            raise ValueError("Key is not present...")
        self.vertex_dict.pop(key)
        for v in self.vertex_dict:
            if key in self.vertex_dict[v].neighbors:
                self.vertex_dict[v].remove_neighbor(key)

    def remove_edge(self, key1, key2):
        if key1 not in self.vertex_dict or key2 not in self.vertex_dict:
            raise ValueError("Key is not present...")
        self.vertex_dict.get(key1).remove_neighbor(key2)
        self.vertex_dict.get(key2).remove_neighbor(key1)

    def has_vertex(self, key):
        return True if key in self.vertex_dict else False

    def has_edge(self, key1, key2):
        if key2 not in self.vertex_dict[key1].neighbors and key1 not in self.vertex_dict[key2].neighbors:
            return False
        return True

    def n_vertex(self):
        return len(self.vertex_dict)

    def n_edge(self):
        res = 0
        for key in self.vertex_dict:
            res += len(self.vertex_dict[key].neighbors)
        return res // 2

    def get_neighbors(self, key):
        return self.vertex_dict[key].neighbors

    def connected_components_bfs(self):
        visited = set()
        components = []

        for vertex in self.vertex_dict:
            if vertex not in visited:
                component = self._bfs(vertex, visited)
                components.append(component)

        return components

    def _bfs(self, start_vertex, visited):
        component = []
        queue = [start_vertex]

        while queue:
            current_vertex = queue.pop(0)

            if current_vertex not in visited:
                visited.add(current_vertex)
                component.append(current_vertex)
                queue.extend(
                    neighbor for neighbor in self.vertex_dict[current_vertex].neighbors if neighbor not in visited)

        return component

    def connected_components_dfs(self):
        visited = set()
        components = []

        for vertex in self.vertex_dict:
            if vertex not in visited:
                component = self._dfs(vertex, visited)
                components.append(component)
        return components

    def _dfs(self, start_vertex, visited):
        component_ = []
        stack = [start_vertex]

        while stack:
            current_vertex = stack.pop()
            if current_vertex not in visited:
                visited.add(current_vertex)
                component_.append(current_vertex)
                stack.extend(
                    neighbor for neighbor in self.vertex_dict[current_vertex].neighbors if neighbor not in visited)
        return component_

    def has_cycle_dfs(self):
        visited = set()
        for vertex in self.vertex_dict:
            if vertex not in visited:
                if self._has_cycle_dfs(vertex, visited, parent=None):
                    return True

        return False

    def _has_cycle_dfs(self, current_vertex, visited, parent):
        visited.add(current_vertex)

        for neighbor in self.vertex_dict[current_vertex].neighbors:
            if neighbor not in visited:
                if self._has_cycle_dfs(neighbor, visited, current_vertex):
                    return True
            elif neighbor != parent:
                return True

        return False



    def display(self):
        for el in self.vertex_dict:
            print(f"{el}: {self.vertex_dict[el].neighbors} ")


g = Graph()
g.add_vertex(1)
g.add_vertex(4)
g.add_vertex(6)
g.add_vertex(7)
g.add_vertex(8)
g.add_vertex(16)
g.add_vertex(22)

g.add_edges(16, 22)
g.add_edges(1, 4)
g.add_edges(6, 4)
g.add_edges(1, 6)
g.add_edges(7, 6)
g.add_edges(6, 8)
g.remove_edge(1, 6)
# print(g.get_neighbors(6))
# print(g.has_edge(1, 4))
g.display()

print()
print(g.connected_components_bfs())
print(g.connected_components_dfs())
# print(g.n_edge())
# g.remove_edge(1, 4)
# print(g.has_edge(4, 1))
# print(g.n_vertex())
# g.remove_vertex(6)
# # print(g.has_vertex(7))
# g.display()
# print(g.n_vertex())

def BFS_SP(graph, start, goal):
    visited = []
    queue = [[start]]
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in visited:
            neighbours = graph.vertex_dict[node].neighbors
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                if neighbour == goal:
                    print("Shortest path = ", new_path)
                    return
            visited.append(node)
    print("No exist")
    return

print(BFS_SP(g, 1, 8))
