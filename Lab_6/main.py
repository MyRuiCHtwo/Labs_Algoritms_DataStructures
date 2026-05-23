from app.uii import print_result, input_int, input_graph
from app.Part1 import kruskal
from app.Part2 import prim


def main():

    print("Лабораторна робота 6: Побудова мінімального каркаса зваженого графа")
    n, edges = input_graph()  # Зчитуємо граф з консолі
    
    while True:
     
        print("\n Виберіть алгоритм для побудови мінімального каркаса: ")
        print("   1. Алгоритм Крускала")
        print("   2. Алгоритм Прима")
        print("   0. Вихід")

        choice = input_int("Ваш вибір (1 або 2)->  ")

        if choice == 1:
         
            spanning_tree, total_weight = kruskal(n, list(edges))

            
            if len(spanning_tree) < n - 1:
                print()
                print("  Знайдено лише частковий каркас.")
                print("  Граф, мабуть, не є зв'язним (є ізольовані компоненти).\n")
          
            print_result(spanning_tree, total_weight)

            input("\nНатисніть Enter, щоб продовжити...")
        elif choice == 2:
            spanning_tree, total_weight = prim(n, list(edges), start=0)

            if len(spanning_tree) < n - 1:
                print()
                print("  Знайдено лише частковий каркас.")
                print("  Граф, мабуть, не є зв'язним (є ізольовані компоненти).\n")
            
            print_result(spanning_tree, total_weight)

            input("\nНатисніть Enter, щоб продовжити...")
        
        elif choice == 0:
            print("Вихід з програми.")
            break
        else:
            print("  Невірний вибір. Спробуйте ще раз.")
            return


if __name__ == "__main__":
    main()
