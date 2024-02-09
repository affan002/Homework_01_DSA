def create_list(size):
    """
    Creates a deque-like data structure with a fixed-size list.

    Parameters:
    - size: The fixed size of the deque.

    Returns:
    A dictionary representing the deque:
    {
        'size': size,    # Fixed size of the deque
        'data': [None] * size,    # List to store elements
        'n': 0,    # Number of elements in the deque
        'i': 0    # Index for circular storage of elements
    }
    """
    return {
        "size": size,
        "data": [None]*size,
        "n":0,
        "i":0
    }

def is_empty(listADT):
    """
    Checks if the deque is empty.

    Parameters:
    - listADT: The deque data structure.

    Returns:
    True if the deque is empty, False otherwise.
    """
    return listADT["n"] == 0

def is_full(listADT):
    """
    Checks if the deque is full.

    Parameters:
    - listADT: The deque data structure.

    Returns:
    True if the deque is full, False otherwise.
    """
    return listADT["n"] == listADT["size"]

def get(i, listADT):
    """
    Gets the element at the specified index in the deque.

    Parameters:
    - i: The index of the element to retrieve.
    - listADT: The deque data structure.

    Returns:
    The element at the specified index.
    """
    return listADT["data"][i]

def set(i, e, listADT):
    """
    Sets the element at the specified index in the deque.

    Parameters:
    - i: The index of the element to set.
    - e: The element to be set.
    - listADT: The deque data structure.
    """
    listADT['data'][i] = e

def length(listADT):
    """
    Gets the number of elements in the deque.

    Parameters:
    - listADT: The deque data structure.

    Returns:
    The number of elements in the deque.
    """
    return listADT["n"]

def add(i, e, listADT):
    """
    Adds an element at the specified index in the deque.

    Parameters:
    - i: The index at which to add the element.
    - e: The element to be added.
    - listADT: The deque data structure.
    """
    if is_full(listADT):
        return "list is full"
    
    for j in range(listADT["n"], i, -1):
        listADT["data"][j] = listADT["data"][j-1]

    listADT["data"][i] = e
    listADT["n"] += 1

def remove(i, listADT):
    """
    Removes the element at the specified index in the deque.

    Parameters:
    - i: The index of the element to remove.
    - listADT: The deque data structure.
    """
    if is_empty(listADT):
        return "list is empty"
    
    out = get(i, listADT)
    for j in range(i, listADT["n"]-1):
        listADT["data"][j] = listADT["data"][j+1]

    listADT["data"][listADT["n"]-1] = None
    listADT["n"] -= 1

    return out


def insert_last(e, listADT):
    """
    Inserts an element at the last position in the deque.

    Parameters:
    - e: The element to be inserted.
    - listADT: The deque data structure.
    """
    if is_full(listADT):
        return "list is full"
    
    i = listADT["i"]
    len = listADT["n"]
    size = listADT["size"]
    
    listADT["data"][(i + len) % size] = e
    listADT["n"] += 1

def remove_last(listADT):
    """
    Removes the last element from the deque.

    Parameters:
    - listADT: The deque data structure.
    """
    if is_empty(listADT):
        return "list is empty"
    
    i = listADT["i"]
    len = listADT["n"]
    size = listADT["size"]
    
    out = listADT["data"][((i + len) % size) - 1]
    listADT["data"][((i + len) % size) - 1] = None
    listADT["n"] -= 1
    return out


def insert_first(e, listADT):
    """
    Inserts an element at the first position in the deque.

    Parameters:
    - e: The element to be inserted.
    - listADT: The deque data structure.
    """
    if is_full(listADT):
        return "list is full"
    
    i = listADT["i"]
    size = listADT["size"]
    if i-1 < 0:
        listADT["i"] = size-1
    else:
        listADT["i"] = i-1
    listADT["data"][listADT["i"]] = e
    listADT["n"] += 1
        

def remove_first(listADT):
    """
    Removes the first element from the deque.

    Parameters:
    - listADT: The deque data structure.
    """
    if is_empty(listADT):
        return "list is empty"
    
    i = listADT["i"]
    size = listADT["size"]
    
    out = listADT["data"][i]
    listADT["i"] = (i+1) % size
    listADT["n"] -= 1
    return out


def get_first(listADT):
    """
    Gets the first element from the deque.

    Parameters:
    - listADT: The deque data structure.

    Returns:
    The first element in the deque.
    """
    i = listADT["i"]
    return listADT["data"][i]

def get_last(listADT):
    """
    Gets the last element from the deque.

    Parameters:
    - listADT: The deque data structure.

    Returns:
    The last element in the deque.
    """
    i = listADT["i"]
    s = listADT["size"]
    len = listADT["n"]
    return get(((i+len)%s)-1,listADT)
