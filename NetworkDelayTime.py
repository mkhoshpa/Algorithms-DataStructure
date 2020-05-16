class Solution:

    def networkDelayTime(self, times, N, k):
        dists = {k: 0}
        edges = [[] for i in range(N + 1)]
        visited = {k}
        to_be_visited = []
        for time in times:
            edges[time[0]].append((time[1], time[2]))

        def visit(to_visit):
            current_time = dists[to_visit]
            for v, time in edges[to_visit]:
                if v not in visited:
                    to_be_visited.append(v)
                if v not in dists:
                    dists[v] = current_time + time
                elif current_time + time < dists[v]:
                    dists[v] = current_time + time
            print(dists)

        visit(k)
        while len(to_be_visited) > 0:
            visit(to_be_visited[0])
            visited.add(to_be_visited[0])
            del to_be_visited[0]
        maximum = -1
        for i in range(1,N+1):
            if i not in dists:
                return -1
            if dists[i] > maximum:
                maximum = dists[i]
        return maximum
if __name__ == '__main__':
    s = Solution()
    print(s.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]],4,2))