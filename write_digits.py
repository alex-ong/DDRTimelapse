from PIL import Image
import os
TILE_WIDTH = 100

filenames = [f"{i}.png" for i in range(10)]
DATA = {}

def init_digits():
    if len(DATA) != 0:
        return
    for i in range(10):
        file_name = os.path.join("images", str(i)+".png")
        DATA[i] = Image.open(file_name)


init_digits()

def write_digits(number, num_digits):
    """
    Creates an 100x numdigit width) by 92 size image.
    Pads the left side with blanks.
    E.g. 123, 7 will result in ___123
    """
    string = str(number)
    string = string.rjust(num_digits, " ")
    image = Image.new('RGB',(TILE_WIDTH*num_digits,92))
    for index, digit in enumerate(string):
        offset = (index*TILE_WIDTH, 0)
        if digit != " ":
            image.paste(DATA[int(digit)], offset)
    return image
        
        
if __name__ == '__main__':
    img = write_digits(12345, 7)
    img.show()