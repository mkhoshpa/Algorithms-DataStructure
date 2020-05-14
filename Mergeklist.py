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


class Solution:
    def mergeKList(self, lists):
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
    s = Solution()
    node = s.mergeKList(lists)
    printListNode(node)


if __name__ == '__main__':
    main()