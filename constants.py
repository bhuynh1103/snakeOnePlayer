# Cause I need colors all the time and I am too lazy to keep on creating variables

# Creates all gray-scale colors with one argument
def gray(x):
    return x, x, x


red = (255, 0, 0)
orange = (255, 128, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
purple = (127, 0, 255)
pink = (255, 0, 255)
black = gray(0)
white = gray(255)

# Constants
width = 800
height = 800

# Scale controls the size of all components of the game except the window size
# Scale should be divisible by screen width and screen height
scale = 50