from collections import defaultdict, deque
import heapq
# define a weighted graph data structure with the following methods:


class Node:
    def __init__(self, key):
        self.key = key
        self.neighbors = {}

    def add_nbr(self, nbr, weight=0):
        if type(nbr) != Node:
            raise TypeError('Argument must be a Node instance')
        self.neighbors[nbr] = weight


class Graph:
    def __init__(self, number_of_vertices=0):
        self.list = defaultdict(list)
        # self.matrix = [[0]*number_of_vertices]*number_of_vertices
        self.len = number_of_vertices
        # define the graph as either an adjacency list or adjacency matrix
        # we’ll use an adjacency list

    def get_len(self):
        return self.len
    # method returns the number of vertices in the graph

    def set_edge(self, node1, node2, weight=None):
        if not weight:
            if node2 in self.list[node1]:
                del self.list[node1][node2]
        else:
            self.list[node1][node2] = weight
            # method adds an edge of weight w between vertices v and u when w is a number;
            #  if the edge already exists, its weight is updated to w. If w is None then the edge, if it exists, is removed, and if absent remains absent.

    def get_edge(self, node1, node2):
        if node1 in self.list and node2 in self.list[node1]:
            return self.list[node1][node2]
        return -1
    # method returns the weight of the edge between vertices u and v

    def get_adjacent_vertices(self, node):
        if node in self.list:
            return self.list[node]
        return []

# method returns a list of all vertices that are directly connected to node
    def get_all_edges(self, node):
        edges = []
        for src in self.list:
            for dest, cost in self.list[node]:
                edges.append([src, dest])
        return edges

# method returns a list of all edges in the graph, in unspecified order. For each edge in the graph, it includes only one direction in the list.
    def sssp(self, node1, node2):
        def bell_ford():
            # slower than dijkstra's but handles negative weights(not cycles)
            # time: 0(EV)
            in_que = set()
            distance = defaultdict(lambda: float('inf'))
            parent = defaultdict(None)
            distance[node1] = 0
            parent[node1] = None
            for v in range(len(self.list)):
                for node in self.list:
                    for edge, weight in self.list[node]:
                        if distance[edge] > distance[node] + weight:
                            distance[edge] = distance[node] + weight
                            parent[edge] = node

            return distance  # , parent

        def dijksta():
            visited = set()
            distance = defaultdict(lambda: float('inf'))
            parent = defaultdict(None)  # keep path if necessary
            distance[node1] = 0

            heap = []
            heapq.heappush(heap, (0, node1))
            while len(heap) > 0:
                (dist, curr_node) = heapq.heappop(heap)
                if curr_node in visited:
                    continue
                visited.add(curr_node)

                for node, weight in self.list[curr_node]:
                    if node not in visited:
                        new_weight = min(dist + weight, distance[node])
                        if new_weight < distance[node]:
                            distance[node] = new_weight
                        heapq.heappush(heap, (new_weight, node))

            return distance
        return bell_ford() == dijksta()

    def mst(self, start_node):
        def prims():
            # Time: 0(Elog V) --> we go through all the edges(E) and only add to heaps V vertices(log V)....
            # not too sure(0(ElogE)possible) since heap may initially have all edges assuming the start node is connected to everything else
            # Space: 0(max(V,E)), we may have all edges in our heap
            mst_cost = 0
            que = []  # deque()
            heap = []
            visited = set()

            # push node into min priority heap
            heapq.heappush(heap, (0, start_node))
            while len(heap) > 0:
                # get the vertex with least cost, and delete it from heap
                (cost, node) = heapq.heappop(heap)

                if node not in visited:  # if not in mst tree, add it
                    mst_cost += cost
                    visited.add(node)
                    que.append((node, cost))

                # for vertices adjacent to popped vertex, add them to heap if not already in mst tree
                for key, cost in graph.list[node]:
                    if key in visited:
                        continue
                    heapq.heappush(heap, (cost, key))
                # if we have added all vertices to our mst, no need to explore the rest of the queue
                if len(visited) == self.len:
                    return (que, mst_cost)

            return (que, mst_cost)

        def kruskals():
            # sort all edges by weight(use heap)
            # pull out in order of increasing weight and add to mst if adding doesn't create a cycle otherwise continue
            # use union find to check for cycles

            # union find
            parent = {}

            def find(key):  # find parent
                if parent[key] == key:
                    return key
                return find(parent[key])

            def union(v, w):
                root_v = find(v)
                root_w = find(w)
                parent[root_v] = root_w  # could keep rank to optimize.

            heap = []
            que = deque()
            visited = set()
            que.append(start_node)
            while que:
                node = que.pop()
                parent[node] = node
                visited.add(node)
                for (key, cost) in self.list[node]:
                    if key not in visited:
                        heapq.heappush(heap, (cost, key, node))
                        que.append(key)

            mst = []
            mst_cost = 0
            while len(mst) < len(visited)-1:
                (cost, From, To) = heapq.heappop(heap)
                p_from = find(From)
                p_to = find(To)
                if p_from != p_to:
                    mst.append((From, cost))
                    mst_cost += cost
                    union(p_from, p_to)
            return (mst, mst_cost)

        return prims() == kruskals()

    '''
    Say we have a garden where 1’s rep trees and 0’s rep grass. We assured that the boxes next to edges are always filled with grass

    [[0,0,0,0,0,0,0,0]
    [0,1,1,1,0,0,0,0]
    [0,1,0,1,0,0,0,0]
    [0,1,0,0,0,0,0,0]
    [0,0,0,0,0,0,0,0]]

    1 forest

    Return how many forests we have in our garden. We define forests as adjacent trees vertically or horizontally. 
    '''

    def num_forests(self, arr):
        visited = set()
        forests = 0
        m, n = len(arr), len(arr[0])

        def dfs(r, c, count):
            if (r, c) in visited or arr[r][c] != 1:
                return
            count += 1
            visited.add((r, c))
            for i, j in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                n_r, n_c = r+i, c + j
                if n_r < m and n_c < n and n_r >= 0 and n_c >= 0 and arr[n_r][n_c] == 1 and (n_r, n_c) not in visited:
                    dfs(n_r, n_c, count)
            return count
        for i in range(m):
            for j in range(n):
                if arr[i][j] == 1 and (i, j) not in visited:
                    count = dfs(i, j, 0)
                    if count > 0:
                        forests += 1

        return forests


if __name__ == '__main__':
    graph = Graph()  # undirected graph for mst problems
    directed_graph = Graph()  # directed graph for sssp problems

    nodes = [[5, 3, 17], [5, 4, 18], [5, 12, 6], [12, 4, 2], [12, 10, 3], [
        4, 10, 19], [4, 3, 16], [3, 6, 30], [4, 6, 88], [6, 10, 8]]
    for a, b, weight in nodes:
        graph.len += 1
        graph.list[a].append((b, weight))
        graph.list[b].append((a, weight))
        directed_graph.list[a].append((b, weight))
    # Test Node class
    node1 = Node(4)
    node2 = Node(5)
    node1.add_nbr(node2)
    print(node1)

    # Test MST algorithms
    print(graph.mst(3))

    # Test SSSP algorithms
    print(directed_graph.sssp(5, 6))

    # For the number of forests problem
    arr_a = [[0, 0, 0, 0, 0, 0, 0, 0],
             [0, 1, 1, 1, 0, 0, 0, 0],
             [0, 1, 0, 1, 0, 0, 0, 0],
             [0, 1, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0]]
    arr_b = [[0, 0, 0, 0],
             [1, 1, 0, 1], [
        1, 0, 1, 0],
        [0, 0, 1, 1]]
    arr_c = [[0, 0, 0, 0, 0, 0, 0, 0],
             [0, 1, 1, 1, 0, 0, 0, 0],
             [0, 1, 0, 1, 0, 1, 0, 0],
             [0, 1, 0, 0, 0, 1, 0, 0],
             [0, 0, 1, 0, 0, 0, 0, 1]]
    print(graph.num_forests(arr_c))
