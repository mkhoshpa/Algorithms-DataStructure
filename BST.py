import random


class BST:
    def __init__(self,val = None):
        self.val = val

        self.left = None
        self.right = None
        if val is None:
            self.count = 0
        else:
            self.count = 1

    def insert(self,val):
        if self.val is None:
            return BST(val)
        if val > self.val:
            if self.right is None:
                self.right = BST(val)
            else:
                self.right = self.right.insert(val)
        else:
            if self.left is None:
                self.left = BST(val)
            else:
                self.left = self.left.insert(val)
        self.count += 1
        return self

    def is_in(self,val):

        if val == self.val:
            return True
        elif val > self.val:
            return self.right.is_in(val)
        else:
            return self.left.is_in(val)

    def rank(self,val):
        if val == self.val:
            if self.left is None:
                return 1
            return self.left.count + 1
        elif val > self.val:
            if self.left is None:
                return self.right.rank(val) + 1
            return self.left.count + self.right.rank(val) + 1
        else:
            return self.left.rank(val)


RED = 'red'
BLACK = 'black'


class Node:
    def __init__(self,key,val,color = BLACK):
        self.key = key
        self.val = val
        self.count = 1
        self.left, self.right = None, None
        self.color = color


def BSTInsert(key,val,root):

    if root is None:
        return Node(key,val)
    if key == root.key:
        root.val = val
        return root
    elif key > root.key:
        root.right = BSTInsert(key,val,root.right)
        root.count += 1
        return root
    else:
        root.left = BSTInsert(key, val, root.left)
        root.count += 1
        return root


def BSTFind(key,root):

    if root is None:
        return None
    if key == root.key:
        return root.val
    elif key > root.key:
        return BSTFind(key,root.right)
    else:
        return BSTFind(key,root.left)


def BSTrank(key,root):
    if root is None:
        return 0
    if key == root.key:
        return 1 + BSTrank(key, root.left)
    elif key > root.key:
        return 1 + BSTrank(key, root.left) + BSTrank(key, root.right)
    else:
        return BSTrank(key, root.left)


def BSTOrderedPrint(root):
    if root is None:
        return
    else:
        BSTOrderedPrint(root.left)
        print(root.key,root.val,sep=':',end="  ")
        BSTOrderedPrint(root.right)


def BSTAtIndex(index,root):
    if index > root.count:
        print(index)
        print(root.count)
        raise Exception
    if index == root.count:
        return str(root.key) + ':' + str(root.val)
    if root.left is None:
        return BSTAtIndex(index - 1, root.right)
    if index < root.left.count + 1:
        return BSTAtIndex(index, root.left)
    else:
        return BSTAtIndex(index - root.left.count - 1, root.right)


def BSTRangeSearch(low,high,root,output = None):
    if root is None:
        return
    if root.key >= low and root.key <= high:
        if output is None:
            print(root.key,root.val,sep=':')
        else:
            output.append(root.key)
        BSTRangeSearch(low,high,root.left,output)
        BSTRangeSearch(low,high,root.right,output)
        return
    if root.key < low:
        BSTRangeSearch(low, high, root.right, output)
        return
    if root.key > high:
        BSTRangeSearch(low, high, root.left, output)
        return
    return


def BSTDeleteMin(root):
    if root.left is None:
        if root.right is None:
            return None, root.key, root.val
        else:
            return root.right, root.key, root.val

    else:
        root.left, out_key, out_val = BSTDeleteMin(root.left)
        return root, out_key, out_val


def twoSum(nums, target):
    oldNums = [e for e in nums]
    nums.sort()
    def binarySearch(nums,target,start=0,end=len(nums)-1):
        mid = (start+end)//2
        if start > end or start < 0 :
            return -1
        if nums[mid] == target:
            #print(mid)
            #print(nums[mid])
            #print()
            return mid
        elif nums[mid] > target:
            return binarySearch(nums,target,start=start,end=mid-1)
        else:
            return binarySearch(nums,target,start=mid+1,end=end)
    for i in range(len(nums)-1):
        e = nums[i]
        #print(i,':',e,target-e)
        result = binarySearch(nums,target-e,start=i+1)
        if result != -1:
            print(nums[i],':',nums[result])
            new_i = [j for j in range(len(oldNums)) if oldNums[j] == e]
            new_i = new_i[0]
            if nums[i] == nums[result]:
                new_result = [j for j in range(new_i,len(oldNums)) if oldNums[j] == nums[result]]
                new_result = new_result[0]
            else:
                new_result = [j for j in range(len(oldNums)) if oldNums[j] == nums[result]]
                new_result = new_result[0]
            return [new_i,new_result]
    return

def main():
    arr = [random.randint(0,100) for i in range(10)]
    random.shuffle(arr)
    root = None
    for element in arr:
        root = BSTInsert(element,random.randint(0,100),root)
    BSTOrderedPrint(root)
    print()
    for i in range(10):
        root,key,val = BSTDeleteMin(root)
        print('key:',key,'val:',val)
    #BSTOrderedPrint(root)
    #print()
    #for element in arr:
    #    print(element,BSTrank(element,root),sep=':',end=' ')
    #print()
    #print(BSTAtIndex(4,root))
    #output = []
    #BSTRangeSearch(10,40,root,output = output)
    #print(output)

if __name__ == '__main__':
   main()