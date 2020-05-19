def Problem1():
    t = int(input())
    for testcase in range(t):
        nk = input()
        n, k = nk.split()
        n, k = int(n), int(k)
        arr = input()
        arr = arr.split()
        A = [int(i) for i in arr]
        print(A)
        num = 0
        for i in range(n - k + 1):
            print(i)
            to_break = False
            for j in range(k):
                print('j',j)
                if A[i] != A[i + j] + j:
                    print('here')
                    to_break = True
                    break
            if not to_break:
                num += 1
        print('Case #' + str(testcase) + ': ' + str(num))



def canBuild(check,A,i):
    global memory
    if check == 0 and i > 0:
        return canBuild(check,A,i-1) + canBuild(check - A[i],A,i-1)
    if i == 0:
        if check != A[0]:
            if check ==0:
                return 1
            return 0
        return 1
    if (check,i) in memory:
        return memory[(check,i)]
    out = canBuild(check,A,i-1) + canBuild(check - A[i],A,i-1)
    memory[(check, i)] = out
    return out


def Problem3():
    t = int(input())
    global memory
    print('tttttttt',t)
    for testcase in range(t):
        memory = {}
        n = input()
        n = int(n)
        arr = input()
        arr = arr.split()
        A = [int(i) for i in arr]
        sums = -1
        for a in A:
            if a >= 0:
                if sums == -1:
                    sums = 0
                sums += a
        if sums < 0:
            print('Case #' + str(testcase+1) + ': ' + str(0))
            continue
        if sums == 0:
            zeros = A.count(0)
            print('Case #' + str(testcase+1) + ': ' + str(pow(2,zeros)-1))
            continue
        to_check = int(pow(sums,0.5))
        out = 0
        if 0 in A:
            out += 1
        for check in range(1,to_check+1):
            i = int(pow(check, 2))
            temp = canBuild(i,A,n-1)
            if temp>0:
                out+=temp
        print('Case #' + str(testcase+1) + ': ' + str(out))


def Problem5():
    t = int(input())
    for testcase in range(t):
        nb = input()
        n, b = nb.split()
        n, b = int(n), int(b)
        arr = input()
        arr = arr.split()
        A = [int(i) for i in arr]
        A.sort()
        i = 0
        while i < n and b > 0:
            b -= A[i]
            if b >= 0:
                i+=1
        print('Case #' + str(testcase) + ': ' + str(i))


mem = {}

def findMostValue(indices,plates,k,budget,n):
    global mem
    if budget == 0:
        return 0
    key = ""
    for i in range(n):
        key += str(indices[i])
    key += str(budget)
    if key in mem:
        return mem[key]
    max_val = 0
    for i in range(n):
        index = indices[i]
        if index < k-1:
            new_indices = [index for inddex in indices]
            new_indices[i] += 1
            val = plates[i][index] + findMostValue(new_indices,plates,k,budget-1,n)
            if val > max_val:
                max_val = val
    mem[key] = max_val
    return max_val


class TrieNode:
    def __init__(self,char = ''):
        self.children = {}
        self.count = 0
        self.char = char

    def add(self,string):
        assert type(string) == type(' ')
        self.count += 1
        if len(string) == 0:
            return

        char = string[0]
        if char in self.children:
            self.children[char].add(string[1:])
        else:
            self.children[char] = TrieNode()
            self.children[char].add(string[1:])

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self,string):
        self.root.add(string)

    def count_prefix(self,string):
        out = 0
        if string[0] not in self.root.children:
            return 0
        node = self.root
        while len(string) > 0 and string[0] in node.children:
            node = node.children[string[0]]
            out += node.count
            string = string[1:]
        return out


def Problem6():
    t = int(input())
    for testcase in range(t):
        nkp = input()
        n, k, p = nkp.split()
        n, k, p = int(n), int(k), int(p)
        plates = []
        for i in range(n):
            new_stack = input()
            new_stack = new_stack.split()
            for j in range(k):
                new_stack[j] = int(new_stack[j])
            plates.append(new_stack)
        indices = [0 for i in range(n)]
        out = findMostValue(indices,plates,k,p,n)
        print('Case #' + str(testcase + 1) + ': ' + str(out))


import random
class SingletonRand:
    num = None
    def __init__(self):
        if SingletonRand.num is None:
            SingletonRand.num = random.random()
    def __str__(self):
        return str(SingletonRand.num)


if __name__ == '__main__':
    x = SingletonRand()
    print(x)
    y=SingletonRand()
    print(y)
