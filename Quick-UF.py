import random


class QuickUF:
    def __init__(self, n):
        self.id = [i for i in range(n)]

    def root(self, p):
        while p != self.id[p]:
            p = self.id[p]
        return p

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        self.id[self.root(q)] = self.id[self.root(p)]


class WeightedQuickUF(QuickUF):
    def __init__(self, n):
        super().__init__(n)
        self.sz = [1 for i in range(n)]

    def union(self, i, j):
        p = self.root(i)
        q = self.root(j)

        if self.sz[p] > self.sz[q]:
            self.id[q] = self.id[p]
            self.sz[p] += self.sz[q]
        else:
            self.id[p] = self.id[q]
            self.sz[q] += self.sz[p]


def find_neghbors(total, index):
    squared = int(pow(total, 0.5))
    x, y = index % squared, index // squared
    neighbors = []
    if x > 0:
        neighbors.append(index - 1)
    if x < squared - 1:
        neighbors.append(index + 1)
    if y > 0:
        neighbors.append(index - squared)
    if y < squared - 1:
        neighbors.append(index + squared)
    return neighbors


class Percolation():
    def __init__(self, n):
        assert int(pow(n, 0.5)) == pow(n, 0.5)
        self.n = n

    def init_wquf(self):
        n = self.n
        wquf = WeightedQuickUF(n + 2)
        for i in range(int(pow(n, 0.5))):
            wquf.union(i, n)
            wquf.union(n - i - 1, n + 1)
        return wquf

    def roll_once(self):
        wquf = self.init_wquf()
        number_of_free = 0
        blocked = [i for i in range(self.n)]
        while not wquf.connected(self.n, self.n + 1):
            number_of_free += 1
            selected = random.sample(range(len(blocked)), 1)
            neighbors = find_neghbors(self.n, blocked[selected[0]])

            for neighbor in neighbors:
                if neighbor not in blocked:
                    wquf.union(neighbor, blocked[selected[0]])
            del blocked[selected[0]]
        return number_of_free

    def roll(self, tries):
        number_of_free = 0
        for i in range(tries):
            number_of_free += self.roll_once()
        return (number_of_free / tries) / self.n


if __name__ == '__main__':
    list_of_sizes = [4, 9, 16, 25, 36, 49, 64, 81, 100, 121]
    for size in list_of_sizes:
        percolation = Percolation(size)
        print(percolation.roll(10000))
