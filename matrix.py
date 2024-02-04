def init_matrix(rows: int, cols: int) -> list[list[int]]:
    """
    Creates a 2D array (matrix) based on the input rows and columns.

    Parameter(s):
    - rows (int): Specifies the rows of the 2D array to be created.
    - cols (int): Specifies the columns of the 2D array to be created.

    Returns:
    - 2D array (int): This is the 2D array that is created using the input rows and cols.
    """
    return [[None for _ in range(cols)] for _ in range(rows)]


def filter_image(image: list[list[int]], kernel: list[int]) -> list[list[int]]:
    """
    Perform the convolution operation by applying the kernel over the input image.

    Parameter(s):
    - 2D array (int): This is the image on which you have to apply the kernel/filter and perform convolution. 
    - 1D array (int): The first entry in this array is the width of the kernel and the remaining entries are the values of the kernel.

    Returns:
    - 2D array (int): This is the matrix that is obtained after performing convolution.
    """
    pass

def main(file_name: str) -> list[list[int]]:
    """
    The main driver function that will run the entire program. 
    It should extract the image and the kernel from the file and pass them to filter_image(...).

    Parameter(s):
    - file_name (.txt file): Path to a text file that contains the image (2D array) and the kernel (1D array).

    Returns:
    - 2D array (int): This is the matrix that is obtained after executing filter_image(...)
    """

    # processing inputs
    with open(f"{file_name}.txt") as file:
        lines = file.readlines()
        rows, cols = lines[0].split
        image = init_matrix
    # Initialize the variables, image and kernel.
        ind = 1    
        while len(lines[ind]) == cols:
            row = lines[ind].split()

    # Pass those variables to filter_image(...)
    # return filter_image(image, kernel)
   
    
    

main("file_name")