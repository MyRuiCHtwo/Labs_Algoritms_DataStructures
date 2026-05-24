from app.Part1 import chained_hash_delete, chained_hash_insert, chained_hash_search, chained_hash_show
from app.Part2 import hash_delete_open_addressing, hash_insert_open_addressing, hash_search_open_addressing, hash_show_open_addressing, hash_liner_study, hash_quadratic_study, hash_double_study
from app.ui_output import int_input, int_input_bigSize, int_exit_input


def main():
    while True:
        print("================ Welcome to the Hash Table Program! ===========================")
        print("\nPlease, first chose the type of hash table you want to use: ")
        print("   1. Chained Hash Table")
        print("   2. Open Addressing Hash Table")
        print("   0. Exit")

        t_choice = int_exit_input("\nPlease enter your choice (1-2): ")
        if t_choice is None:
            return
        
        if t_choice == 1:
            hash_table_size = int_input_bigSize("\nPlease enter the size of the hash table (1-1000): ")
            if hash_table_size is None:
                return
            
            hash_table = [None] * hash_table_size

            while True:
                print("\n================ Menu =================")
                print("1. Insert a key-value pair")
                print("2. Search for a key")
                print("3. Delete a key")
                print("4. Show hash table")
                print("5. Return to main menu")

                choice = int_input("\nPlease enter your choice (1-5): ")
                if choice is None:
                    continue

                if choice == 1:
                    key = int_input("Enter the key to insert: ")
                    value = int_input("Enter the value to insert: ")
                    print("\nChoose the collision resolution method:")
                    print("1. Linear Probing")
                    print("2. Quadratic Probing")
                    print("3. Double Hashing")
                    method_choice = int_input("\nPlease enter your choice (1-3): ")
                    if method_choice is None:
                        continue
                    if method_choice == 1:
                        study_method  = hash_liner_study
                    elif method_choice == 2:
                        study_method  = hash_quadratic_study
                    elif method_choice == 3:
                        study_method  = hash_double_study
                    
                    result = chained_hash_insert(hash_table, key, value, study_method)
                    print(result)
                    input("\nPress Enter to continue...")
                elif choice == 2:
                    key = int_input("Enter the key to search: ")
                    result = chained_hash_search(hash_table, key)
                    print(result)
                    input("\nPress Enter to continue...")
                elif choice == 3:
                    key = int_input("Enter the key to delete: ")
                    result = chained_hash_delete(hash_table, key)
                    print(result)
                    input("\nPress Enter to continue...")
                elif choice == 4:
                    result = chained_hash_show(hash_table)
                    print(result)
                    input("\nPress Enter to continue...")
                elif choice == 5:
                    print("Returning to main menu...")
                    break
                
                else:
                    print("Invalid choice. Please enter a number between 1 and 5.")

        elif t_choice == 2:
            hash_table_size = int_input_bigSize("\nPlease enter the size of the hash table (1-1000): ")
            if hash_table_size is None:
                return
            
            hash_table = [None] * hash_table_size

            while True:
                print("\n================ Menu =================")
                print("1. Insert a key-value pair")
                print("2. Search for a key")
                print("3. Delete a key")
                print("4. Show hash table")
                print("5. Return to main menu")

                choice = int_input("\nPlease enter your choice (1-5): ")
                if choice is None:
                    continue

                if choice == 1:
                    key = int_input("Enter the key to insert: ")
                    value = int_input("Enter the value to insert: ")
                    result = hash_insert_open_addressing(hash_table, key, value)
                    print(result)
                    input("\nPress Enter to continue...")
                elif choice == 2:
                    key = int_input("Enter the key to search: ")
                    result = hash_search_open_addressing(hash_table, key)
                    print(result)
                    input("\nPress Enter to continue...")
                elif choice == 3:
                    key = int_input("Enter the key to delete: ")
                    result = hash_delete_open_addressing(hash_table, key)
                    print(result)
                    input("\nPress Enter to continue...")
                elif choice == 4:
                    result = hash_show_open_addressing(hash_table)
                    print(result)
                    input("\nPress Enter to continue...")
                elif choice == 5:
                    print("Returning to main menu...")
                    break
                
                else:
                    print("Invalid choice. Please enter a number between 1 and 5.")

        elif t_choice == 0:
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 0 and 2.")
 

if __name__ == "__main__":
    main()


    

    
