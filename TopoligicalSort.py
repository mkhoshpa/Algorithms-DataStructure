class Graph:
    def __init__(self, n, edges):
        self.n = n
        self.graph = [set() for i in range(self.n)]
        for edge in edges:
            self.graph[edge[1]].add(edge[0])

    def adj(self, v):
        return self.graph[v]

#Topological sort using DFS
#return [] if grapgh has a cycle
#findOrder get num: number of vertices
#and p: pairs of [v,w] representing a directed edge between w->v
#returns the topological order.
class Solution:
    def dfs(self, v):
        self.visited[v] = True
        self.curr.add(v)
        for w in self.G.adj(v):
            # print('w:',w,'curr',self.curr)
            if w in self.curr:
                self.cycle = True
            if not self.visited[w]:
                self.dfs(w)
                self.curr.remove(w)

        self.preorder.append(v)
        return 1

    def findOrder(self, num: int, p):
        self.cycle = False
        if num == 0:
            return []
        self.G = Graph(num, p)
        self.visited = [False for i in range(num)]
        self.preorder = []
        self.curr = set()
        for v in range(num):
            self.curr = set()
            if not self.visited[v]:
                self.dfs(v)
                if self.cycle:
                    return []
        output = []
        if len(self.preorder) < num:
            for i in range(num):
                if i not in self.preorder:
                    output.append(i)
        i = len(self.preorder) - 1
        while i >= 0:
            output.append(self.preorder[i])
            i -= 1
        return output


def main():
    num = 4
    pairs = [[0,1],[2,1],[3,0]]
    s = Solution()
    print('order:' ,s.findOrder(num,pairs))


if __name__ == '__main__':
    main()