"""Implementations of some sorting"""
import random
import ArrayList

def linear_search(a : ArrayList.ArrayList, x):
    # todo
    for i in range(a.size()):
        if a[i] == x:
            return i
    return -100

def binary_search(a : ArrayList.ArrayList, x):
    # todo
    l = 0
    r = len(a) - 1
    while l <= r:
        m = (l + r) // 2
        if a[m] == x:
            return m
        elif x < a[m]:
            #print(f"{x} is less than {a[m]}")
            r = m - 1
        else:
            #print(f"{x} is greater than {a[m]}")
            l = m + 1
    return -100

def _merge(a0 : ArrayList.ArrayList, a1 : ArrayList.ArrayList, a : ArrayList.ArrayList):
    # todo
    i0 = 0
    i1 = 0
    for i in range(0, a.size()):
        if i0 >= a0.size():
            a.set(i, a1.get(i1))
            i1 += 1
        elif i1 >= a1.size():
            a.set(i, a0.get(i0))
            i0 += 1
        elif a0.get(i0) <= a1.get(i1):
            a.set(i, a0.get(i0))
            i0 += 1
        elif a1.get(i1) <= a0.get(i0):
            a.set(i, a1.get(i1))
            i1 += 1
    return

def merge_sort(a : ArrayList.ArrayList):
    # todo
    if a.size() <= 1:
        return a
    m = a.size() // 2
    a0 = ArrayList.ArrayList()
    a1 = ArrayList.ArrayList()
    for i in range(0, m):
        a0.append(a.get(i))
    for i in range(m, a.size()):
        a1.append(a.get(i))
    merge_sort(a0)
    merge_sort(a1)
    _merge(a0, a1, a)

def _quick_sort_f(a : ArrayList.ArrayList, start, end):
    # todo
    if start < end:
        p = _partition(a, start, end)
        _quick_sort_r(a, start, p - 1)
        _quick_sort_r(a, p + 1, end)



def _quick_sort_r(a : ArrayList.ArrayList, start, end):
    pass
    '''
    pivot random
    pick random and make it first, then continue with quick sort
    # todo
    x = a[start + random.randint(0, n-1)]
    if start < end:
        p = _partition(a, start, end)
        _quick_sort_r(a, start, p - 1)
        _quick_sort_r(a, p + 1, end)
    '''
    if start < end:
        p = _partition(a, start, end)
        _quick_sort_r(a, start, p - 1)
        _quick_sort_r(a, p + 1, end)
    #return a


def _partition(a, start, end):
    # todo
    pivot = a[start]
    l = start + 1
    r = end
    crossed = False
    while not crossed:
        while l <= r and a[l] <= pivot:
            l += 1
        while r >= l and a[r] >= pivot:
            r -= 1
        if r < l:
            crossed = True
        else:
            temp = a[l]
            a[l] = a[r]
            a[r] = temp
    temp2 = a[start]
    a[start] = a[r]
    a[r] = temp2
    return r

def quick_sort(a : ArrayList.ArrayList, p=True):
    """
    sorts an ArrayList a using the quick sort algorithm.
    If parameter p is True, the quick sort algorithm uses a randomly chosen element from a as pivot.
    Otherwise, the quick sort algorithm uses the first element as pivot.
    """
    if p:
        _quick_sort_r(a, 0, a.size()-1)
    else:
        _quick_sort_f(a, 0, a.size()-1)


    
