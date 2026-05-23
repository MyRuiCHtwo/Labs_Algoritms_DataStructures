

from app.Part1 import hash_function_division


def hash_liner_study(key, i, table_size):
    return (hash_function_division(key, table_size) + i) % table_size


def hash_quadratic_study(key, i, table_size):
    return (hash_function_division(key, table_size) + i * i) % table_size


def hash_double_study(key, i, table_size):
    return (hash_function_division(key, table_size) + i * hash_function_division(key, table_size - 1)) % table_size


def hash_insert_open_addressing(hash_table, key, value, study_method=hash_liner_study):
    table_size = len(hash_table)

    for i in range(table_size):
        index = study_method(key, i, table_size)
        if hash_table[index] is None or hash_table[index] == "Deleted":
            hash_table[index] = (key, value)
            return f"Key {key} inserted at index {index}."
        elif hash_table[index][0] == key:
            hash_table[index] = (key, value)
            return f"Key {key} updated at index {index}."
    return "Hash table is full. Cannot insert new key."


def hash_search_open_addressing(hash_table, key, study_method=hash_liner_study):
    table_size = len(hash_table)

    for i in range(table_size):
        index = study_method(key, i, table_size)
        if hash_table[index] is None:
            return f"Key {key} not found."
        elif hash_table[index] != "Deleted" and hash_table[index][0] == key:
            return f"Key {key} found at index {index} with value {hash_table[index][1]}."
    return f"Key {key} not found."


def hash_delete_open_addressing(hash_table, key, study_method=hash_liner_study):
    table_size = len(hash_table)

    for i in range(table_size):
        index = study_method(key, i, table_size)
        if hash_table[index] is None:
            return f"Key {key} not found."
        elif hash_table[index] != "Deleted" and hash_table[index][0] == key:
            hash_table[index] = "Deleted"
            return f"Key {key} Deleted from index {index}."
    return f"Key {key} not found."


def hash_show_open_addressing(hash_table):
    result = "Hash Table:\n"
    for index, item in enumerate(hash_table):
        if item is None:
            result += f"Index {index}: Empty\n"
        elif item == "Deleted":
            result += f"Index {index}: Deleted\n"
        else:
            result += f"Index {index}: Key {item[0]}, Value {item[1]}\n"
    return result


