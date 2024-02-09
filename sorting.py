import json
import math
import ast 

def initialize_matrix(n: int) -> list[list[int]]:
    """
    A  function that takes an integer n as an argument and returns a 2D array of size n x n with each cell containing None values.
    """
    return [[None for i in range(n)] for j in range(n)]


def length(arr: list[int]) -> int:
    """
    A function that takes a single-dimensional array, arr, as an argument and returns the count of valid data items in it, i.e., the non-None values.
    """
    len = 0
    for i in arr:
        if i == None:
            break
        len+=1
    
    
    return len



def get_maximum(arr: list[int]) -> int:
    """
    A function that takes an array as an argument, and WITHOUT using the built-in functions, returns the maximum value of the array.
    """
    max = arr[0]
    for i in range(1, length(arr)):
        if arr[i] > max:
            max = arr[i]
    return max



def insertion_sort(arr: list[int]) -> None:
    """
    A void function that takes a single-dimensional array arr as an argument and applies insertion sort on the valid data items in the array, i.e., the non-None values. This is an in-place function, meaning the original array that was passed as a reference will be updated with the sorted values.
     
    The function should not return anything.
    """
    len = length(arr)
    for i in range(1, len):
        temp = arr[i]
        j = i-1
        while j>=0 and arr[j] > temp:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = temp


def partition_and_prevail(arr: list[list[int]]) -> None:
    """
    A void function that takes the array to be sorted as an argument
    and applies the “Partition and Prevail” algorithm to sort the valid
    data items in the array, as explained in the assignment.

    The function should not return anything.
    """
    n = len(arr)
    # initialize a 2D array
    new_matrix = initialize_matrix(n)

    # calculating group size
    max_element = get_maximum(arr)
    group_size = math.ceil((max_element + 1)/n)

    # adding elements into the matrix 
    #iterating over the arr
    for i in range(length(arr)):
        row_no = math.floor(arr[i]/group_size)
        # putting each element into the resulting row_no
        new_matrix[row_no][length(new_matrix[row_no])] = arr[i]

    arr_ind = 0
    for row in new_matrix:
        insertion_sort(row)
        ind = 0
        while row[ind] != None:
            arr[arr_ind] = row[ind]
            arr_ind += 1
            ind += 1

def main(filename) -> list[list[int]]:
    """
    - Take input from the given filename one line at a time
    - Apply partition_and_prevail sorting algorithm to get the sorted arrays and returns the output as a two dimensional array.
    """

    # processing inputs by readin the txt file
    with open(filename) as file:
        lines = file.readlines()
        arr = ast.literal_eval(lines[0])

    # check if the arr is empty
    if length(arr) == 0:
        return arr
    
    partition_and_prevail(arr)

    return arr

# print(main("sorting01.txt"))

    