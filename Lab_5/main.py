from app.Part_1 import get_parent, get_left, get_right, max_heapify, min_heapify, build_max_heap, build_min_heap, HeapSort
from app.Part_2 import heap_min, heap_max, heap_decrese_key, heap_extra_max, heap_extra_min, heap_increse_key, max_heap_insert, max_heapify, min_heap_insert, min_heapify


def main():
    try:
        user_input = input("Введіть елементи масиву через пробіл: ").strip()
        A = list(map(int, user_input.split()))
    
    except ValueError:
        print("Помилка: Введіть лише цілі числа, розділені пробілом.")
        return
    
    while True:
        print("\nВиберіть дію:")
        print("---------- Перша частина ----------")
        print("1.  Індекс лівого нащадка для заданого індексу")
        print("2.  Індекс правого нащадка для заданого індексу")
        print("3.  Індекс батька для заданого індексу")
        print("4.  Побудувати max-heap")
        print("5.  Побудувати min-heap")
        print("6.  Відсортувати піраміду за допомогою HeapSort")
        print("---------- Друга частина ----------")
        print("7.  Вивести мінімальний елемент з min-heap")
        print("8.  Вивести максимальний елемент з max-heap")
        print("9.  Вивести мінімальний елемент з min-heap та видалити його")
        print("10.  Вивести максимальний елемент з max-heap та видалити його")
        print("11.  Зменшити ключ в min-heap")
        print("12.  Збільшити ключ в max-heap")
        print("13.  Вставити елемент в max-heap")
        print("14.  Вставити елемент в min-heap")

        print("0.    Вихід")

        print("\nПочатковий масив:", A, end="\n")
        
        command = input("\nВаш вибір: ").strip()
        
        if command == '1':
            try:
                index = int(input("\nВведіть індекс для пошуку лівого нащадка: ").strip())
                left_index = get_left(index, len(A))
                if left_index is not None:
                    print(f"Індекс лівого нащадка для індексу {index}: {left_index} (значення: {A[left_index]})")
                else:
                    print(f"Лівий нащадок для індексу {index} не існує.")
            except ValueError:
                print("\nПомилка: Введіть ціле число для індексу.")
            
            input("\nНатисніть Enter, щоб продовжити...")

        if command == '2':
            try:
                index = int(input("\nВведіть індекс для пошуку правого нащадка: ").strip())
                right_index = get_right(index, len(A))
                if right_index is not None:
                    print(f"Індекс правого нащадка для індексу {index}: {right_index} (значення: {A[right_index]})")
                else:
                    print(f"Правий нащадок для індексу {index} не існує.")
            except ValueError:
                print("\nПомилка: Введіть ціле число для індексу.")
                
            input("\nНатисніть Enter, щоб продовжити...")

        if command == '3':
            try:
                index = int(input("\nВведіть індекс для пошуку батька: ").strip())
                parent_index = get_parent(index)
                if parent_index is not None:
                    print(f"Індекс батька для індексу {index}: {parent_index} (значення: {A[parent_index]})")
                else:
                    print(f"Батько для індексу {index} не існує.")
            except ValueError:
                print("\nПомилка: Введіть ціле число для індексу.") 

            input("\nНатисніть Enter, щоб продовжити...")

        if command == '4':
            A_max = build_max_heap(A.copy())
            print("\n Побудований max-heap:", A_max)

            input("\nНатисніть Enter, щоб продовжити...")
        
        elif command == '5':
            A_min = build_min_heap(A.copy())
            print("\n Побудований min-heap:", A_min)

            input("\nНатисніть Enter, щоб продовжити...")
        
        elif command == '6':
            try:
                choice = int(input("\n Виберіть тип сортування (1 - max-heap, 2 - min-heap): "))
            except ValueError:
                print("\n Помилка: Введіть 1 або 2.")
                continue
            
            sorted_A = HeapSort(A.copy(), choice)
            print("\n Відсортований масив:", sorted_A)

            input("\nНатисніть Enter, щоб продовжити...")

        elif command == '7':
            try:
                A_min = build_min_heap(A.copy())
                print(f"\nНайменший елемент з min-heap: {heap_min(A_min)}")
            except NameError:
                print("\nСпочатку побудуйте min-heap (опція 5).")

            input("\nНатисніть Enter, щоб продовжити...")

        elif command == '8':
            try:
                A_max = build_max_heap(A.copy())
                print(f"\nНайбільший елемент з max-heap: {heap_max(A_max)}")
            except NameError:
                print("\nСпочатку побудуйте max-heap (опція 4).")

            input("\nНатисніть Enter, щоб продовжити...")

        elif command == '9':
            try:
                A_min = build_min_heap(A.copy())
                min_val = heap_extra_min(A_min)
                print(f"\nВидалений мінімальний елемент: {min_val}")
                print(f"Min-heap після видалення: {A_min}")
            except NameError:
                print("\nСпочатку побудуйте min-heap (опція 5).")
            except Exception as e:
                print(f"\nПомилка: {e}")

            input("\nНатисніть Enter, щоб продовжити...")

        elif command == '10':
            try:
                A_max = build_max_heap(A.copy())
                max_val = heap_extra_max(A_max)
                print(f"\nВидалений максимальний елемент: {max_val}")
                print(f"Max-heap після видалення: {A_max}")
            except NameError:
                print("\nСпочатку побудуйте max-heap (опція 4).")
            except Exception as e:
                print(f"\nПомилка: {e}")

            input("\nНатисніть Enter, щоб продовжити...")

        elif command == '11':
            try:
                A_min = build_min_heap(A.copy())
                i = int(input("\nВведіть індекс елемента для зменшення ключа: ").strip())
                new_key = int(input("Введіть нове значення ключа (менше за поточне): ").strip())
                heap_decrese_key(A_min, i, new_key)
                print(f"\nMin-heap після зменшення ключа: {A_min}")
            except NameError:
                print("\nСпочатку побудуйте min-heap (опція 5).")
            except ValueError:
                print("\nПомилка: Введіть цілі числа для індексу та ключа.")
            except Exception as e:
                print(f"\nПомилка: {e}")

            input("\nНатисніть Enter, щоб продовжити...")

        elif command == '12':
            try:
                A_max = build_max_heap(A.copy())
                i = int(input("\nВведіть індекс елемента для збільшення ключа: ").strip())
                new_key = int(input("Введіть нове значення ключа (більше за поточне): ").strip())
                heap_increse_key(A_max, i, new_key)
                print(f"\nMax-heap після збільшення ключа: {A_max}")
            except NameError:
                print("\nСпочатку побудуйте max-heap (опція 4).")
            except ValueError:
                print("\nПомилка: Введіть цілі числа для індексу та ключа.")
            except Exception as e:
                print(f"\nПомилка: {e}")

            input("\nНатисніть Enter, щоб продовжити...")

        elif command == '13':
            try:
                A_max = build_max_heap(A.copy())
                key = int(input("\nВведіть елемент для вставки в max-heap: ").strip())
                max_heap_insert(A_max, key)
                print(f"\nMax-heap після вставки: {A_max}")
            except NameError:
                print("\nСпочатку побудуйте max-heap (опція 4).")
            except ValueError:
                print("\nПомилка: Введіть ціле число для елемента.")
            except Exception as e:
                print(f"\nПомилка: {e}")

            input("\nНатисніть Enter, щоб продовжити...")

        elif command == '14':
            try:
                A_min = build_min_heap(A.copy())
                key = int(input("\nВведіть елемент для вставки в min-heap: ").strip())
                min_heap_insert(A_min, key)
                print(f"\nMin-heap після вставки: {A_min}")
            except NameError:
                print("\nСпочатку побудуйте min-heap (опція 5).")
            except ValueError:
                print("\nПомилка: Введіть ціле число для елемента.")
            except Exception as e:
                print(f"\nПомилка: {e}")

            input("\nНатисніть Enter, щоб продовжити...")

        elif command == '0':
            print("\n Вихід з програми.")
            break
        
        else:
            print("\n Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()

