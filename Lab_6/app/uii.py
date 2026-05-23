from app.Part1 import make_edge


def input_int(prompt):
    """
    Допоміжна функція: зчитує ціле число з консолі.
    Повторює запит, поки користувач не введе коректне значення.
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("  [!] Помилка: введіть ціле число.")


def input_graph():
    """
    Зчитує з консолі опис графа:
      1. Кількість вершин n
      2. Кількість ребер m
      3. Для кожного ребра — дві вершини та вага

    Вершини нумеруються з 1 (як у методичці), але всередині
    програми зберігаються з 0 (стандарт для масивів/списків).

    Повертає: (n, edges) — кількість вершин і список ребер.
    """
    print("=" * 50)
    print("     Введення графа (список ребер)")
    print("=" * 50)

    # Кількість вершин
    n = input_int("Введіть кількість вершин: ")
    while n < 2:
        print("  [!] Граф повинен мати не менше 2 вершин.")
        n = input_int("Введіть кількість вершин: ")

    # Кількість ребер
    m = input_int("Введіть кількість ребер: ")
    while m < 1:
        print("  [!] Граф повинен мати хоча б одне ребро.")
        m = input_int("Введіть кількість ребер: ")

    edges = []  # Список ребер (масив структур, як в методичці)

    print(f"\nВведіть {m} ребер у форматі:  v1  v2  вага")
    print(f"(Вершини нумеруються від 1 до {n})")
    print("-" * 50)

    for i in range(m):
        while True:
            try:
                raw = input(f"  Ребро {i + 1}: ").split()
                if len(raw) != 3:
                    raise ValueError
                v1     = int(raw[0])
                v2     = int(raw[1])
                weight = int(raw[2])

                # Перевіряємо, що вершини в допустимому діапазоні
                if not (1 <= v1 <= n and 1 <= v2 <= n):
                    print(f"  [!] Вершини повинні бути від 1 до {n}.")
                    continue
                if v1 == v2:
                    print("  [!] Петлі не допускаються (v1 ≠ v2).")
                    continue
                if weight < 0:
                    print("  [!] Вага не може бути від'ємною.")
                    continue

                # Переводимо номери вершин до індексів 0..n-1
                # (всередині алгоритму вершини 0-based)
                edges.append(make_edge(v1 - 1, v2 - 1, weight))
                break

            except (ValueError, IndexError):
                print("  [!] Формат: v1 v2 вага  (три цілих числа)")

    return n, edges


def print_result(spanning_tree, total_weight):
    """
    Виводить на екран ребра мінімального каркасу та їх сумарну вагу.
    Номери вершин відображаються з 1 (як у методичці).
    """
    print()
    print("=" * 50)
    print("     Мінімальний каркас (алгоритм Краскала)")
    print("=" * 50)

    if not spanning_tree:
        print("  [!] Каркас не побудовано. Граф, можливо, незв'язний.")
        return

    print(f"  {'Ребро':^12}  {'Вага':>6}")
    print("  " + "-" * 20)

    for edge in spanning_tree:
        # Переводимо назад з 0-based до 1-based для відображення
        v1 = edge["v1"] + 1
        v2 = edge["v2"] + 1
        w  = edge["weight"]
        print(f"  v{v1}  --  v{v2}      {w:>4}")

    print("  " + "-" * 20)
    print(f"  Сумарна вага каркасу: {total_weight}")
    print("=" * 50)

