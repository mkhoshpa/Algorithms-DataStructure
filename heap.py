import random
def swim(arr, idx):
    while idx // 2 > 0:
        p = idx // 2
        if arr[idx] < arr[p]:
            arr[idx], arr[p] = arr[p], arr[idx]
            idx = p
        else:
            return


def sink(arr, idx, length=None):
    if length is None:
        length = len(arr)
    while 2 * idx < length:
        child = 2 * idx
        if child + 1 < length:
            if arr[child + 1] < arr[child]:
                child = child + 1
        if arr[child] < arr[idx]:
            arr[child], arr[idx] = arr[idx], arr[child]
            idx = child
        else:
            break


def heap_push(arr, item):
    arr.append(item)
    swim(arr, len(arr) - 1)


def heap_pop(arr):
    out = arr[1]
    arr[1] = arr[len(arr) - 1]
    del arr[len(arr) - 1]
    sink(arr, 1)
    return out

def main():
    heap=['_']
    arr = [random.randint(0,100) for i in range(10)]
    random.shuffle(arr)
    root = None
    for element in arr:
        heap_push(heap,element)
    while len(heap)>1:
        print(heap_pop(heap))

if __name__ == '__main__':
   main()
