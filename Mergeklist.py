# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.count = 1
        self.left, self.right = None, None


def BSTInsert(key, val, root):
    if root is None:
        return Node(key, val)

    if key > root.key:
        root.right = BSTInsert(key, val, root.right)
        root.count += 1
        return root
    else:
        root.left = BSTInsert(key, val, root.left)
        root.count += 1
        return root


def BSTFind(key, root):
    if root is None:
        return None
    if key == root.key:
        return root.val
    elif key > root.key:
        return BSTFind(key, root.right)
    else:
        return BSTFind(key, root.left)


def BSTOrderedPrint(root):
    if root is None:
        return
    else:
        BSTOrderedPrint(root.left)
        print(root.key,root.val,sep=':',end="  ")
        BSTOrderedPrint(root.right)


def BSTDeleteMin(root, out=[]):
    if root.left is None:
        out.append((root.key, root.val))
        if root.right is None:
            return None
        else:
            return root.right

    else:
        root.left = BSTDeleteMin(root.left, out)
        return root



def BSTMergeKList( lists):
    output_start = None
    output_end = None
    current_pool = None
    for i, node in enumerate(lists):
        if node is not None:
            current_pool = BSTInsert(node.val, i, current_pool)
    while current_pool is not None:
        out = []
        current_pool = BSTDeleteMin(current_pool, out)
        minimum_val, minimum_idx = out[0]
        if output_start is None:
            output_start = ListNode(minimum_val)
            output_end = output_start
        else:
            output_end.next = ListNode(minimum_val)
            output_end = output_end.next
        if lists[minimum_idx].next is not None:
            lists[minimum_idx] = lists[minimum_idx].next
            current_pool = BSTInsert(lists[minimum_idx].val, minimum_idx, current_pool)
    return output_start


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



def heapMergeKLists(lists):
        output_start = None
        output_end = None
        current_pool = ['_']
        for i, node in enumerate(lists):
            if node is not None:
                heap_push(current_pool, (node.val, i))
        while len(current_pool) > 1:

            minimum_val, minimum_idx = heap_pop(current_pool)

            if output_start is None:
                output_start = ListNode(minimum_val)
                output_end = output_start
            else:
                output_end.next = ListNode(minimum_val)
                output_end = output_end.next
            if lists[minimum_idx].next is not None:
                lists[minimum_idx] = lists[minimum_idx].next
                # current_pool = BSTInsert(lists[minimum_idx].val,minimum_idx, current_pool)
                heap_push(current_pool, (lists[minimum_idx].val, minimum_idx))
        return output_start

def printListNode(listnode):
    while listnode is not None:
        print(listnode.val,end=', ')
        listnode = listnode.next


def main():
    ls = [[0,2,5]]
    lists = []
    for l in ls:
        output_start = None
        output_end = None
        for element in l:
            if output_start is None:
                output_start = ListNode(element)
                output_end = output_start
            else:
                output_end.next = ListNode(element)
                output_end = output_end.next
        lists.append(output_start)
    node = heapMergeKLists(lists)
    printListNode(node)


if __name__ == '__main__':
    main()