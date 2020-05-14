class UF():
    def __init__(self,n):
        self.id = [i for i in range(n)]

    def connected(self,p,q):
        return self.id[p] == self.id[q]

    def union(self,p,q):
        for i in range(len(self.id)):
            if self.id[i] == self.id[q]:
                self.id[i] = self.id[p]