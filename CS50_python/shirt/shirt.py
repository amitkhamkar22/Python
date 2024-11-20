'''
In a file called shirt.py, implement a program that expects exactly two command-line arguments:
    in sys.argv[1], the name (or path) of a JPEG or PNG to read (i.e., open) as input
    in sys.argv[2], the name (or path) of a JPEG or PNG to write (i.e., save) as output

The program should then overlay shirt.png (which has a transparent background) on the input after
resizing and cropping the input to be the same size, saving the result as its output.
Open the input with Image.open, per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open,
resize and crop the input with ImageOps.fit, per pillow.readthedocs.io/en/stable/reference/ImageOps.html#PIL.ImageOps.fit,
using default values for method, bleed, and centering, overlay the shirt with Image.paste,
per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.paste, and save the result
with Image.save, per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save.

The program should instead exit via sys.exit:
    if the user does not specify exactly two command-line arguments,
    if the input’s and output’s names do not end in .jpg, .jpeg, or .png, case-insensitively,
    if the input’s name does not have the same extension as the output’s name, or
    if the specified input does not exist.
Assume that the input will be a photo of someone posing in just the right way, like these demos,
so that, when they’re resized and cropped, the shirt appears to fit perfectly.
'''
from PIL import Image
from PIL import ImageOps
import sys
import os

def main():
    #check correctness of command-line arguments
    if len(sys.argv) == 3:

        _, ext1 = os.path.splitext(sys.argv[1])
        _, ext2 = os.path.splitext(sys.argv[2])

        match = extension_check(ext1,ext2)

    else:
        if len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")
        else:
            sys.exit("Too many command-line arguments")

    if match:

       overlay_image(sys.argv[1], sys.argv[2])

    else:
        sys.exit("Incorrect image arguments")

#return True if command-line arguments meet checks else return False
def extension_check(ext1,ext2):
    ext1 = ext1.lower()
    ext2 = ext2.lower()

    #Input/Output command-line arguments have same file extensions
    if ext1 == ext2:
        #extensions are either 'jpg' or 'jpeg' or 'png'
        if ext1 == ".jpg" or ext1 == ".jpeg" or ext1 == ".png":
            return True
        else:
            print("Invalid inputs")
            return False
    else:
        print("Input and output have different extensions")
        return False

#take image provided in command-line argument_1, size the crop the image
#Overlay shirt image on the image provided in the argument_1.
#Save the resulting image in the file name provided in the argument_2
def overlay_image(image1, image2):

    try:
        img1 = Image.open(image1)
        shirt = Image.open("shirt.png")

        #box = (215, 10, 815, 610)
        #img = img1.crop(box)

        siz = shirt.size
        img = ImageOps.fit(img1, siz)
        img.paste(shirt,shirt)
        img.save(image2)

    except FileNotFoundError:
        sys.exit("Input does not exist")

if __name__ == "__main__":
    main()