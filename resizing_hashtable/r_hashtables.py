

# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# '''
# Fill this in
# Resizing hash table
# '''
class HashTable:
    def __init__(self, capacity):
        # max length of hash table
        self.capacity = capacity

        # underlying data structure
        self.storage = [None] * capacity

    def __len__(self):
        return self.capacity


# '''
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hash = 5381
    for x in string:
        hash = ((hash << 5) + hash) + ord(x)
    return hash % max


# Check if hash_table overloaded
def is_overloaded(hash_table):
    none_count = 0
    for item in hash_table.storage:
        if item is None:
            none_count = none_count + 1
    load_level = (len(hash_table.storage) - none_count) / len(hash_table.storage)
    if load_level >= 0.7:
        return True
    return False


# Find the next empty array slot
def find_next_empty_slot(starting_index, list):
    index = starting_index
    list_end = len(list) - 1
    while True:
        if list[index] is None:
            break
        if index == list_end:
            index = 0
            continue
        if index == starting_index - 1:
            index = None
            break
        index = index + 1
        break
    return index


# '''
# Fill this in.

# Hint: Used the LL to handle collisions
# '''
def hash_table_insert(hash_table, key, value):
    if is_overloaded(hash_table):
        hash_table_auto_resize(hash_table)
    index = hash(key, len(hash_table))
    if hash_table.storage[index] is None or hash_table.storage[index].key == key:
        hash_table.storage[index] = LinkedPair(key, value)
        return
    while hash_table.storage[index].key != key:
        if hash_table.storage[index].next is None:
            next_empty_slot = find_next_empty_slot(index, hash_table.storage)
            hash_table.storage[index].next = next_empty_slot
            hash_table.storage[next_empty_slot] = LinkedPair(key, value)
            break
        else:
            index = hash_table.storage[index].next




# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    pass


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    index = hash(key, len(hash_table))
    if hash_table.storage[index] is None:
        return None
    while hash_table.storage[index].key != key:
        if hash_table.storage[index].next is not None:
            index = hash_table.storage[index].next
        else:
            return None
    return hash_table.storage[index].value


# '''
# Fill this in
# '''
def hash_table_resize(hash_table):
    pass


def Testing():
    ht = HashTable(2)

    hash_table_insert(ht, "line_1", "Tiny hash table")
    hash_table_insert(ht, "line_2", "Filled beyond capacity")
    hash_table_insert(ht, "line_3", "Linked list saves the day!")

    print(hash_table_retrieve(ht, "line_1"))
    print(hash_table_retrieve(ht, "line_2"))
    print(hash_table_retrieve(ht, "line_3"))

    old_capacity = len(ht.storage)
    ht = hash_table_resize(ht)
    new_capacity = len(ht.storage)

    print("Resized hash table from " + str(old_capacity)
          + " to " + str(new_capacity) + ".")


Testing()
