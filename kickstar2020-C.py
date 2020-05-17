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
    for testcase in range(t):
        memory = {}
        n = input()
        n = int(n)
        arr = input()
        arr = arr.split()
        A = [int(i) for i in arr]
        sums = sum(A)
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


if __name__ == '__main__':
    memory = {}
    Problem3()