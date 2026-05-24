class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


def hash_function_division(key, size):
    return hash(key) % size


def hash_function_multiplication(key, size):
    A = (5 ** 0.5 - 1) / 2
    return int(size * ((hash(key) * A) % 1))


def chained_hash_insert(hash_table, key, value):
    index = hash_function_division(key, len(hash_table))
       
    cur = hash_table[index]
    while cur:
        if cur.key == key:
            cur.value = value
            return f"Successfully updated key: {key}"
        cur = cur.next
         
    new_node = Node(key, value)
    new_node.next = hash_table[index] 
    hash_table[index] = new_node      
    
    return f"Successfully inserted key: {key}"


def chained_hash_search(hash_table, key):
    index = hash_function_division(key, len(hash_table))
    cur = hash_table[index]

    while cur:
        if cur.key == key:
            return f"Found key: {key}, value: {cur.value}"
        cur = cur.next

    return f"Key: {key} not found"


def chained_hash_delete(hash_table, key):
    index = hash_function_division(key, len(hash_table))
    cur = hash_table[index]

    if cur is None:
        return f"Key: {key} not found"
    elif cur.key == key:
        hash_table[index] = cur.next
        return f"Deleted key: {key} with value: {cur.value}"
    else:
        prev = cur
        cur = cur.next
        while cur:
            if cur.key == key:
                prev.next = cur.next
                return f"Deleted key: {key}, with value: {cur.value}"
            prev = cur
            cur = cur.next
        return f"Key: {key} not found"
    

def chained_hash_show(hash_table):
    if hash_table is None:
        return "Hash table is not initialized"
    
    result = []
    for i, node in enumerate(hash_table):
        chain = []
        cur = node
        while cur:
            chain.append(f"{cur.key}: {cur.value}")
            cur = cur.next

        if chain:
            chain_str = " -> ".join(chain) + " -> None"
        else:
            chain_str = "None"

        result.append(f"Index {i}: {chain_str}")
        
    return "\n".join(result)


