# Import a function "square" from module functions.py
from functions import square
# import functions (the entire module)

for i in range(10):
    print(f"The square of {i} is {square(i)}") # If import functions then would be functions.square(i)
