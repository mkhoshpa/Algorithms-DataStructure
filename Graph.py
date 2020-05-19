class Graph:
    def __init__(self):
        pass

    def adj(self, v):
        return []

    def V(self):
        try:
            return self.n
        except:
            pass

class Digraph(Graph):
    def __init__(self, n, edges):
        super().__init__()
        self.n = n
        self.graph = [list() for i in range(self.n)]
        for edge in edges:
            self.graph[edge[0]].append([edge[0],edge[1]])

    def adj(self, v):
        return self.graph[v]




class UnDirGraph(Digraph):
    def __init__(self, n, edges):
        super().__init__(n, edges)
        for edge in edges:
            self.graph[edge[1]].append([edge[1],edge[0]])



class WeightedGraph(Graph):
    #edges are accesible from adj() method. result is list of edges in the format of [start,end,weight
    _Graph: Graph = None
    def __init__(self, G, wedges):
        if not isinstance(self._Graph, UnDirGraph) or not isinstance(self._Graph,Digraph):
            raise Exception('weighted graph should be Directed graph or undirected graph')
        self._Graph = G
        if isinstance(self._Graph,UnDirGraph):
            for v in range(self._Graph.V()):
                for edge in self._Graph.adj(v):
                    edge.append(wedges[edge[0]][edge[1]])
        else:
            for v in range(self._Graph.V()):
                for edge in self._Graph.adj(v):
                    edge.append(wedges[edge[0]][edge[1]])

    def V(self):
        return self._Graph.V()

    def adj(self,v):
        return self._Graph.adj(v)





