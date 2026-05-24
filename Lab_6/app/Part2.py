INF = float("inf")


def make_adjacency_matrix(n):
    return [[INF] * n for _ in range(n)]


def set_edge_matrix(matrix, v1, v2, weight):
  
    matrix[v1][v2] = weight
    matrix[v2][v1] = weight   


def prim(n, edges, start=0):
   

    matrix = make_adjacency_matrix(n)
    for edge in edges:
        v1, v2, weight = edge["v1"], edge["v2"], edge["weight"]
        set_edge_matrix(matrix, v1, v2, weight)
      
   
    visited = [False] * n
   
    min_e = [INF] * n
    
    sel_e = [-1] * n

    
    min_e[start] = 0

    spanning_tree = []   # ребра каркасу, що накопичуємо
    total_weight  = 0    # сумарна вага
  
    for _ in range(n):
             
        u = -1
        for v in range(n):
            if not visited[v]:                        
                if u == -1 or min_e[v] < min_e[u]:   
                    u = v
        
        if u == -1 or min_e[u] == INF:
            break
       
        visited[u] = True
       
        if sel_e[u] != -1:
            spanning_tree.append({
                "v1":     sel_e[u],
                "v2":     u,
                "weight": min_e[u]
            })
            total_weight += min_e[u]
        
        for v in range(n):
            if not visited[v] and matrix[u][v] < min_e[v]:
                
                min_e[v] = matrix[u][v]   # оновлюємо мінімальну вагу
                sel_e[v] = u              # запам'ятовуємо звідки

    return spanning_tree, total_weight
