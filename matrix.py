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
    k = kernel[0]
    img_rows = len(image)
    img_cols = len(image[0])
    kernel = kernel[1:]
    new_image = init_matrix(img_rows, img_cols)
    for i in range(img_rows):
        for j in range(img_cols):
            pixel = 0
            r, c = k//2, k//2
            add = 1
            for z in range(k//2):
                pixel += image[i][j] * kernel[r*k + c]
                if i + add < img_rows:
                    pixel += image[i+add][j] * kernel[c*k + (r+add)]
                if i - add >= 0:
                    pixel += image[i-add][j] * kernel[(c)*k + (r-add)]
                if j + add < img_cols:
                    pixel += image[i][j+add] * kernel[(c+add)*k + (r)]
                if j - add >= 0:
                    pixel += image[i][j-add] * kernel[(c-add)*k + (r)]
                if i+add < img_rows and j+add < img_cols:
                    pixel += image[i+add][j+add] * kernel[(c+add)*k + (r+add)]
                if i+add < img_rows and j-add >= 0:
                    pixel += image[i+add][j-add] * kernel[(c-add)*k + (r+add)]
                if i-add >=0 and j-add >=0:
                    pixel += image[i-add][j-add] * kernel[(c-add)*k + (r-add)]
                if i-add >= 0 and j+add < img_cols:
                    pixel += image[i-add][j+add] * kernel[(c+add)*k + (r-add)]
            new_image[i][j] = pixel
            add += 1     
    return new_image


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
    with open(file_name) as file:
        lines = file.readlines()

    #storing rows and cols as variable
    rows, cols = lines[0].split()
    rows, cols = int(rows), int(cols)

    # Initialize the variables, image and kernel.
    image = init_matrix(rows, cols)    
    for line_no in range(1,rows + 1):
        row = lines[line_no].split()
        image[line_no-1] = row

    
    kernel = lines[rows + 1].split()
    for i in range(len(kernel)):
        kernel[i] = int(kernel[i])


    for i in range(rows):
        for  j in range(cols):
            image[i][j] = int(image[i][j])

    # Pass those variables to filter_image(...)
    return filter_image(image, kernel)
   
    

