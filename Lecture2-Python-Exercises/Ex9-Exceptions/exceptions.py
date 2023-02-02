import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error: Invalid input.")
    sys.exit(1)

try:
    result = x / y
except ZeroDivisionError:                   # Exception handler
    print("Error: Cannot divide by 0.")
    sys.exit(1)                             # 1 means something went wrong



print(f"{x} / {y} = {result}")