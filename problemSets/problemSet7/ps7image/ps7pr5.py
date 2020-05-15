#
# ps7pr5.py  (Problem Set 7, Problem 5)
#
# Images as 2-D lists  
#
# Computer Science 111
# 

from hmcpng import *

def create_uniform_image(height, width, pixel):
    """ creates and returns a 2-D list of pixels with height rows and
        width columns in which all of the pixels have the RGB values
        given by pixel
        inputs: height and width are non-negative integers
                pixel is a 1-D list of RBG values of the form [R,G,B],
                     where each element is an integer between 0 and 255.
    """
    pixels = []

    for r in range(height):
        row = [pixel] * width
        pixels += [row]

    return pixels

def blank_image(height, width):
    """ creates and returns a 2-D list of pixels with height rows and
        width columns in which all of the pixels are green.
        inputs: height and width are non-negative integers
    """
    all_green = create_uniform_image(height, width, [0, 255, 0])
    return all_green

def brightness(pixel):
    """ takes a pixel (an [R, G, B] list) and returns a value
        between 0 and 255 that represents the brightness of that pixel.
    """
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]
    return (21*red + 72*green + 7*blue) // 100

## put your functions below

def grayscale(pixels):
    """takes a 2d list of pixels and converts it into the grayscale of it
    input: a 2d list of pixels"""
    grid = blank_image(len(pixels), len(pixels[0]))
        
    for r in range(len(pixels)):
        for c in range(len(pixels[0])):
            bright = brightness(pixels[r][c])
            grid[r][c] = [bright, bright, bright]
            
    return grid

def fold_diag(pixels):
    """takes a 2d list of pixels and folds it diagnolly
    input: a 2d list of pixels"""
    grid = blank_image(len(pixels), len(pixels[0]))

    for r in range(len(pixels)):
        for c in range(len(pixels[0])):
            if r >c:
                grid[r][c] = [255,255,255]
            else:
                grid[r][c] = pixels[r][c]
                
    return grid

def mirror_horiz(pixels):
    """takes a 2d list of pixels and returns it mirrored horizontally down the middle
    input: a 2d list of pixels"""
    grid = blank_image(len(pixels), len(pixels[0]))
    
    for r in range(len(pixels)):
        for c in range(len(pixels[0])//2):
            grid[r][c] = pixels[r][c]
            grid[r][len(grid[0])-1-c] = pixels[r][c]
    return grid

def extract(pixels, rmin, rmax, cmin, cmax):
    """takes a list and returns a new list within the given dimensions within the parameter
    input: a 2d list of pixels followed by 4 integers"""
    grid = blank_image(rmax-rmin, cmax-cmin)
    
    for r in range(len(grid)):
        for c in range(len(grid[0])):
           grid[r][c] = pixels[r+rmin][c+cmin]    
                    
                    
    return grid