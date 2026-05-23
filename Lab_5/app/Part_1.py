
def get_parent(i):
   
    if i <= 0:
        return None
    return (i - 1) // 2


def get_left(i, heap_size):
   
    left = 2 * i + 1
    return left if left < heap_size else None


def get_right(i, heap_size):
   
    right = 2 * i + 2
    return right if right < heap_size else None


def max_heapify(A, n, i):
    larg = i
    left = get_left(i, n)
    right = get_right(i, n)

    
    if left is not None and A[left] > A[larg] and left < n:
        larg = left
    
   
    if right is not None and A[right] > A[larg] and right < n:
        larg = right

  
    if larg != i:
        A[i], A[larg] = A[larg], A[i]  
       
        max_heapify(A, n, larg)


def min_heapify(A, n, i):
    small = i
    left = get_left(i, n)
    right = get_right(i, n)

   
    if left is not None and A[left] < A[small] and left < n:
        small = left
    
   
    if right is not None and A[right] < A[small] and right < n:
        small = right

   
    if small != i:
            A[i], A[small] = A[small], A[i]  
           
            min_heapify(A, n, small)


def build_max_heap(A):
    n = len(A)

    for i in range(n // 2 - 1, -1, -1):
        max_heapify(A, n, i)
    
    return A
    
    
def build_min_heap(A):
    n = len(A)

    for i in range(n // 2 - 1, -1, -1):
        min_heapify(A, n, i)

    return A

def HeapSort(A, choice):
    n = len(A)

    if choice in [1, "max"]:
        A_max = build_max_heap(A)

        for i in range(n-1, 0, -1):
            A_max[0], A_max[i] = A_max[i], A_max[0]  
            max_heapify(A_max, i, 0)
        return A_max
    
    elif choice in [2, "min"]:
        A_min = build_min_heap(A)

        for i in range(n-1, 0, -1):
            A_min[0], A_min[i] = A_min[i], A_min[0] 
            min_heapify(A_min, i, 0)
        return A_min
    else:
        raise ValueError("Невірний вибір типу сортування. Виберіть 1 для max-heap або 2 для min-heap.")
   

    



   

