from app.Part_1 import max_heapify, min_heapify, get_parent


def heap_max(A):
    return A[0]

def heap_min(A):
    return A[0]

def heap_extra_max(A):
    if len(A) < 1:
        raise Exception("Черга порожня")
    
    max_val = heap_max(A)
    A[0] = A.pop()

    if len(A) > 0:
        max_heapify(A, len(A), 0)
        
    return max_val

def heap_extra_min(A):
    if len(A) < 1:
        raise Exception("Черга порожня")
    
    min_val = heap_min(A)
    A[0] = A.pop()

    if len(A) > 0:
        min_heapify(A, len(A), 0)
        
    return min_val


def heap_increse_key(A, i, key):
    if key < A[i]:
        raise Exception("Нове ключове значення повинно бути більшим за поточне")
    
    A[i] = key
    
    while i > 0 and A[(i - 1) // 2] < A[i]:
        parent = get_parent(i)
        A[i], A[parent] = A[parent], A[i]
        i = parent

def heap_decrese_key(A, i, key):
    if key > A[i]:
        raise Exception("Нове ключове значення повинно бути меншим за поточне")
    
    A[i] = key
    while i > 0 and A[(i - 1) // 2] > A[i]:
        parent = get_parent(i)
        A[i], A[parent] = A[parent], A[i]
        i = parent


def max_heap_insert(A, key):
    A.append(float("-inf")) 

    heap_increse_key(A, len(A) - 1, key)
    
def min_heap_insert(A, key):
    A.append(float("inf"))

    heap_decrese_key(A, len(A) - 1, key)




