# Decorator = Create a function that modifies another function and gives back an output

def announce(f):
    def wrapper():
        print("about to run the function...")
        f()
        print("Done with the function.")
    return wrapper


# Example adding a decorator announce wiht "@":
@announce
def hello():
    print("Hello, world!")

hello()