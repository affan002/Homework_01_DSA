# DO NOT CHANGE THIS FUNCTION
# Create a basic queue
def create_queue(size: int) -> dict:
    """
    Description: Creates and initializes a basic queue with a specified size.
    Parameters: size - an integer representing the size of the queue.
    Return: A dictionary representing the initialized queue.
    """
    return {
        'data': [None] * size,  # list of elements
        'front': -1,  # index of the first element in the queue
        'rear': -1,  # index of the last element in the queue
        'n': 0,  # number of elements in the queue
        'size': size  # size of the queue
    }

# DO NOT CHANGE THIS FUNCTION
# Create a priority queue
def create_priority_queue(size: int) -> dict:
    """
    Description: Creates and initializes a priority queue with a specified size.
                 Each element in the queue is a tuple consisting of data and priority.
    Parameters: size - an integer representing the size of the priority queue.
    Return: A dictionary representing the initialized priority queue.
    """
    return {
        'data': [(None, float('inf'))] * size,  # list of elements with default priority set to infinity
        'front': -1,  # index of the first element in the queue
        'rear': -1,  # index of the last element in the queue
        'n': 0,  # number of elements in the queue
        'size': size  # size of the queue
    }

# Check if the queue is full
def is_full(queue: dict) -> bool:
    """
    Description: Checks if the given queue is full (reached its maximum capacity).
    Parameters: queue - a dictionary representing the queue.
    Return: True if the queue is full, False otherwise.
    """
    return queue['n'] == queue['size']

# Check if the queue is empty
def is_empty(queue: dict) -> bool:
    """
    Description: Checks if the given queue is empty (contains no elements).
    Parameters: queue - a dictionary representing the queue.
    Return: True if the queue is empty, False otherwise.
    """
    return queue['n'] == 0
    

# Add an element to the rear of the queue
def enqueue(queue: dict, item):
    """
    Description: Adds an element with the value 'val' to the rear of the queue.
    Parameters: queue - a dictionary representing the queue, val - the value to be added to the queue.
    """
    if is_full(queue):
        raise Exception("Queue is full")
    
    rear = queue['rear']
    queue['rear'] = (rear + 1) % queue['size']
    queue['n'] += 1 
    queue['data'][queue['rear']] = item

    if queue['n'] == 1:
        queue['front'] = queue['rear']

# Remove and return the element from the front of the queue
def dequeue(queue: dict) :
    """
    Description: Removes and returns the element from the front of the queue.
    Parameters: queue - a dictionary representing the queue.
    Return: The element from the front of the queue.
    """
    if is_empty(queue):
        raise Exception('Queue is empty')
    
    front = queue['front']
    out = queue['data'][front]
    queue['front'] = (front + 1) % queue['size']
    queue['n'] -= 1
    return out 

# Return the element at the front of the queue without removing it
def peek(queue: dict):
    """
    Description: Returns the element at the front of the queue without removing it.
    Parameters: queue - a dictionary representing the queue.
    Return: The element at the front of the queue.
    """
    return queue['data'][queue['front']]

# Add an element with priority to the priority queue
def enqueue_priority(priority_queue: dict, item, priority: int):
    """
    Description: Adds an element with the value 'val' and the specified priority to the priority queue.
    Parameters: queue - a dictionary representing the priority queue, val - the value to be added to the queue,
                priority - the priority of the element.
    """
    if is_full(priority_queue):
        raise Exception("Queue is full")
    
    rear = priority_queue['rear']
    priority_queue['rear'] = (rear + 1) % priority_queue['size']
    priority_queue['n'] += 1 
    priority_queue['data'][priority_queue['rear']] = item

    if priority_queue['n'] == 1:
        priority_queue['front'] = priority_queue['rear']

    
    

# Remove and return the element with the minimum priority from the priority queue
def dequeue_min_priority(priority_queue: dict):
    """
    Description: Removes and returns the element with the minimum priority from the priority queue.
    Parameters: queue - a dictionary representing the priority queue.
    Return: The element with the minimum priority from the priority queue.
    """
    
    
# Return the element with the minimum priority from the priority queue without removing it
def peek_min_priority(priority_queue: dict):
    """
    Description: Returns the element with the minimum priority from the priority queue without removing it.
    Parameters: queue - a dictionary representing the priority queue.
    Return: The element with the minimum priority from the priority queue.
    """
    


def CallSimulator(callQueue, agentQueue) -> dict:
    """
    Description: Simulates a call center scenario where calls are processed by agents based on their availability.
    Type: Function
    Parameters: callQueue - a dictionary representing the call queue,
                AgentQueue - a dictionary representing the agent queue.
    Return: A queue containing information about each processed call (callerName, call_start, call_end, wait_time).
    """
    # Simulation parameters
    Simulation = True
    currentTime = 0

    # Create a queue to store the call log
    callLog = create_queue(callQueue['size'])

    while Simulation:
        # provide your implementation here


        # Increment the current time for the next iteration
        currentTime += 1

    # Returning the queue containing the call log
    return callLog


def main(filename) -> list:
    """
    Description: Main function to read input data from a file, initialize agent and call queues, simulate call processing using CallSimulator, and return the call log data.
    Parameters: filename - the name of the file containing input data.
    Return: A list representing the call log data.
    """
    
    # Read input data from the file
    # First line contains the list of agents separated by spaces 
    # Second line contains the number of calls to be processed
    # Populate the call queue with call details from the remaining lines contain the call details (start time, caller name, call duration) separated by spaces

    # provide your implementation here 
    
    
    # Simulate call processing using CallSimulator
    call_log = CallSimulator(call_queue, agentQueue)

    # Return the call log data as a list
    return call_log['data']




