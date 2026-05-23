INF = float("inf")


def make_adjacency_matrix(n):
    return [[INF] * n for _ in range(n)] # Створюємо матрицю n x n, заповнену INF (немає ребра)


def set_edge_matrix(matrix, v1, v2, weight):
  
    matrix[v1][v2] = weight
    matrix[v2][v1] = weight   # симетрія — незорієнтований граф


def prim(n, edges, start=0):
   
    # Конвертуємо список ребер у матрицю суміжності
    matrix = make_adjacency_matrix(n)
    for edge in edges:
        v1, v2, weight = edge["v1"], edge["v2"], edge["weight"]
        set_edge_matrix(matrix, v1, v2, weight)

   
    # ініціалізація масивів


    # visited[v] = True, якщо вершина v вже занесена в множину U
    visited = [False] * n

    # min_e[v] — найменша відома вага ребра від v до множини U.
    # Спочатку INF для всіх (жодна вершина ще не в U).
    min_e = [INF] * n

    # sel_e[v] — яка вершина з U дає це мінімальне ребро до v.
    # -1 означає «ще не визначено».
    sel_e = [-1] * n

    # Стартову вершину підключаємо з вагою 0 —
    # стандартний прийом, щоб вона була обрана першою.
    min_e[start] = 0

    spanning_tree = []   # ребра каркасу, що накопичуємо
    total_weight  = 0    # сумарна вага

    # Виконуємо рівно n ітерацій — по одній на кожну вершину
    for _ in range(n):

       
        # Знайти вершину u з V\U з найменшим min_e[u].
        # Це найближча до поточного каркасу вершина.

        u = -1
        for v in range(n):
            if not visited[v]:                        # v ще не в U
                if u == -1 or min_e[v] < min_e[u]:   # кращий кандидат
                    u = v

        # Якщо не знайшли жодної досяжної вершини — граф незв'язний
        if u == -1 or min_e[u] == INF:
            break

        # Заносимо вершину u в множину U
        visited[u] = True

        # Якщо u не стартова вершина — ребро (sel_e[u], u) входить
        # до каркасу, зберігаємо його
        if sel_e[u] != -1:
            spanning_tree.append({
                "v1":     sel_e[u],
                "v2":     u,
                "weight": min_e[u]
            })
            total_weight += min_e[u]

        #  оновлення sel_e та min_e.
        # Для кожної ще не відвіданої вершини v перевіряємо:
        # чи є ребро (u, v) коротше за поточне min_e[v].
        for v in range(n):
            if not visited[v] and matrix[u][v] < min_e[v]:
                # Через нову вершину u знайшли коротший шлях до v
                min_e[v] = matrix[u][v]   # оновлюємо мінімальну вагу
                sel_e[v] = u              # запам'ятовуємо звідки

    return spanning_tree, total_weight
