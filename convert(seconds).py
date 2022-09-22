from time import strftime,localtime

def convert(seconds):
    return strftime('%Y-%M-%d_%H:%m:%S',localtime(seconds))

print(convert(1601901810))