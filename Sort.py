import math, random


# linear
def find_min(arr, start=0, end=None):

    if end is None:
        end = len(arr)
    assert start < end
    minimum = math.inf
    minimum_index = None
    for i in range(start, end):
        if arr[i] < minimum:
            minimum = arr[i]
            minimum_index = i
    return minimum_index


# N2
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = find_min(arr, start=i, end=len(arr))
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


# N2
def insertion_sort(arr):
    for i in range(len(arr)):
        unsorted_element = i
        for j in range(i):
            idx = i - j - 1
            if arr[unsorted_element] < arr[idx]:
                arr[idx], arr[unsorted_element] = arr[unsorted_element], arr[idx]
                unsorted_element = idx
    return arr


# O(N2), ~ unknown
def shell_sort(arr):
    h = 1
    n = len(arr)
    while h < n // 3:
        h = 3 * h + 1
    while h >= 1:
        for i in range(h, len(arr)):
            unsorted_element = i
            for j in range(0, i, h):
                idx = i - j - 1
                if arr[unsorted_element] < arr[idx]:
                    arr[idx], arr[unsorted_element] = arr[unsorted_element], arr[idx]
                    unsorted_element = idx
        h = h // 3
    return arr


# linear
def uniformly_shuffle(arr):
    for i in range(len(arr)):
        r = random.randint(0, i)
        arr[i], arr[r] = arr[r], arr[i]
    return arr


def merge(arr, low, mid, high):
    aux = [i for i in arr]
    idx = low
    mid_idx = mid
    for i in range(low, high):
        if idx == mid:
            arr[i] = aux[mid_idx]
            mid_idx += 1
        elif mid_idx == high:
            arr[i] = aux[idx]
            idx += 1
        elif aux[idx] <= aux[mid_idx]:
            arr[i] = aux[idx]
            idx += 1
        else:
            arr[i] = aux[mid_idx]
            mid_idx += 1


def merge_sort(arr, lo, high):
    mid = (lo + high-1) // 2
    if lo < mid:
        merge_sort(arr, lo, mid+1)
        merge_sort(arr, mid+1, high)
    merge(arr, lo, mid+1 , high)


def partition(arr, low,high):
    if low + 1 == high:
        if arr[low]> arr[high]:
            arr[low],arr[high] = arr[high],arr[low]
            return high
        return low
    else:
        k = low
        i = low
        j = high
        while True:
            while arr[i] <= arr[k]:
                i += 1
                if i == high:
                    break

            while arr[j] >= arr[k]:
                j -= 1
                if j == low:
                    break
            if i >= j:
                break
            arr[i], arr[j] = arr[j],arr[i]
        arr[k], arr[j] = arr[j], arr[k]
        return j


def three_way_partition(arr,low,high):
    lt = low
    gt = high
    i = low
    value = arr[low]
    while i <= gt:
        if arr[i] > value:
            arr[i] , arr[gt] = arr[gt], arr[i]
            gt -= 1
        elif arr[i]< value:
            arr[i], arr[lt] = arr[lt], arr[i]
            i += 1
            lt += 1
        else:
            i += 1
    return lt, gt


def three_way_quick_sort(arr,low,high):
    if high <= low:
        return
    lt,gt = three_way_partition(arr,low,high)
    three_way_quick_sort(arr,low,lt-1)
    three_way_quick_sort(arr,gt+1,high)


#worscase quadradic
#average case NlgN
def quick_sort(arr,low,high):
    if(high <= low):
        return
    k = partition(arr,low,high)
    quick_sort(arr,low,k-1)
    quick_sort(arr, k+1, high)


def quick_select(arr,low,high,i):
    k = partition(arr,low,high)
    if k == i:
        return arr[k]
    if k < i:
        return quick_select(arr,k+1,high,i)
    return quick_select(arr,low,k - 1 ,i)


def swim(arr,idx):
    while idx // 2>0:
        p = idx //2
        if arr[idx]> arr[p]:
            arr[idx],arr[p] = arr[p],arr[idx]
            idx = p
        else:
            return


def sink(arr, idx, length=None):
    if length is None:
        length = len(arr)
    while 2*idx < length:
        child = 2*idx
        if child + 1 < length:
            if arr[child + 1 ] > arr[child]:
                child = child + 1
        if arr[child] > arr[idx]:
            arr[child],arr[idx]=arr[idx], arr[child]
            idx = child
        else:
            break




# worstcase NlgN
# bestcase NlgN
def heap_sort(arr):
    k = len(arr)//2
    while k > 0:
        sink(arr, k)
        k -= 1
    i = len(arr) - 1
    while i > 0:
        arr[i],arr[1] = arr[1],arr[i]
        i -= 1
        sink(arr,1,i)

def floor(nums, element, low, high):
        if element > nums[high]:
            return high
        if element <= nums[low]:
            return low - 1
        if low == high:
            return low
        mid = (low + high) // 2
        if element ==  nums[mid]:
            return mid
        if element > nums[mid]:
            return floor(nums, element, mid+1, high)
        return floor(nums, element, low, mid - 1)

class KthLargest:

    def __init__(self, k: int, nums):
        self.k = k
        nums.sort()
        self.nums = nums

    def add(self, val: int) -> int:
        def floor(nums, element, low, high):
            if element > nums[high]:
                return high
            if element <= nums[low]:
                return low - 1
            if low == high:
                return low
            mid = (low + high) // 2
            if element ==  nums[mid]:
                return mid
            if element > nums[mid]:
                return floor(nums, element, mid+1, high)
            return floor(nums, element, low, mid - 1)
        index = floor(self.nums,val,0,len(self.nums)-1)
        self.nums.insert(index+1,val)
        return self.nums[self.k-1]

from decimal import *
if __name__ == '__main__':
    getcontext().prec = 6
    print(Decimal(1/7) / Decimal(7))
