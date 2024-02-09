import list_adt as listadt

def create_alien(first_S) -> dict:
    """
    Creates an 'alien' dictionary with a list to store messages.
    You can add other attributes if required

    Returns:
    A dictionary representing an 'alien' with a list to store messages:
    {
        'messages': listadt.create_list(100)    # List to store messages with a maximum capacity of 100
    }
    """
    return {"messages": listadt.create_list(100),
    # provide other required implementation here
            "min_S": first_S,
             "max_S": first_S,
             "last_ind": 1}

def add(seq: int, msg: str, alienList: dict):
    """
    Parameters:
    - seq: The sequence number of the message.
    - msg: The message to be added.
    - alienList: The 'alien' dictionary containing the messages list.
    """

    # provide implementation here
    if seq >= alienList["max_S"]:
        listadt.insert_last(msg, alienList["messages"])
        alienList["max_S"] = seq
        alienList["last_ind"] = 1
    elif seq <= alienList["min_S"]:
        listadt.insert_first(msg, alienList["messages"])
        alienList["min_S"] = seq
        alienList["last_ind"] = -1
    

def delete(seq: int, msg: str, alienList: dict):
    """

    Parameters:
    - seq: The sequence number of the message to be deleted.
    - msg: The message to be deleted.
    - alienList: The 'alien' dictionary containing the messages list.
    """

    # provide implementation here
    if alienList["last_ind"] == 1:
        listadt.remove_last(alienList["messages"])    
    else:
        listadt.remove_first(alienList["messages"])
def get_messages(alienList: dict) -> list[str]:
    """

    Parameters:
    - alienList: The 'alien' dictionary containing the messages list.

    Returns:
    A list of all messages in the conversation.
    """

    # provide implementation here
    n = alienList["messages"]["n"]
    new_lst = [None for i in range(n)]
    for i in range(n):
        element = listadt.remove_first(alienList["messages"])
        new_lst[i] = element

    return new_lst


def main(filename) -> list[str]:
    """
    Reads data from a file, processes it, and returns the conversation as a list.

    Data is provided in the following format:
    There can be multiple lines in the file, each line containing an integer and an optional string separated by a space. The integer represents the sequence number of the message, and the string represents the message itself. If the string is not provided, it is assumed to be an empty string. The sequence number 0 indicates the end of the conversation.

    Process the data as follows:
    - If the sequence number is 0, stop processing the file.
    - If the sequence number is positive, add the message to the conversation.
    - If the sequence number is negative, delete the message from the conversation.
    
    Parameters:
    - filename: The name of the file to read data from.

    Returns:
    A list representing the conversation obtained from the file.
    """

    # Provide your implementation here

    # reading the txt file
    with open(filename) as file:
        lines = file.readlines()

    first_lst = lines[0].split()
    
    messages = create_alien(int(first_lst[0]))

    add(int(first_lst[0]), first_lst[1], messages)
    for i in range(1, len(lines)):
        row_lst = lines[i].split()
        S = int(row_lst[0])
        if len(row_lst) == 2:
            M = row_lst[1]
        else:
            M = ""

        if S > 0:
            add(S, M, messages)

        elif S < 0:
            delete(S, M, messages)

        else:
            break
        
    out_lst = get_messages(messages)
    output = ""
    for i in out_lst:
        output += (i + " ")
    return(output[:-1])

# print(main("alien02.txt"))