
def make_edge(v1, v2, weight):
    return {"v1": v1, "v2": v2, "weight": weight}


previous = []

def dsu_init(n):
   
    global previous
    previous = list(range(n))  # previous[v] = v для кожного v


def set_make(v):
   
    previous[v] = v


def set_find(v):
   
    if previous[v] == v:
        return v
    return set_find(previous[v])


def set_union(v1, v2):
  
    root1 = set_find(v1)
    root2 = set_find(v2)

    if root1 == root2:
       
        return False
    
    previous[root2] = root1
    return True




def sort_edges(edges): # Selection Sort
    n = len(edges)
    for i in range(n):
      
        min_idx = i
        for j in range(i + 1, n):
            if edges[j]["weight"] < edges[min_idx]["weight"]:
                min_idx = j
    
        edges[i], edges[min_idx] = edges[min_idx], edges[i]


def kruskal(n, edges):
  
    # Сортуємо ребра за зростанням ваги
    sort_edges(edges)

    # Ініціалізуємо DSU для n вершин 
    dsu_init(n)

    spanning_tree = []   # ребра каркасу
    total_weight = 0     # Лічильник сумарної ваги

    # Перебираємо ребра у порядку зростання ваги 
    for edge in edges:
        v1 = edge["v1"]
        v2 = edge["v2"]
        w  = edge["weight"]

        # Намагаємось об'єднати множини вершин v1 і v2.
        # set_union поверне True, якщо вершини були в різних множинах
        # (ребро не утворює циклу) — тоді додаємо ребро до каркасу.
        if set_union(v1, v2):
            spanning_tree.append(edge)
            total_weight += w

        # Якщо вже зібрали n-1 ребро — каркас повний, зупиняємось
        if len(spanning_tree) == n - 1:
            break

    return spanning_tree, total_weight
