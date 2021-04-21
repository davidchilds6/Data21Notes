# #  defining functions
#
# can add type hint - only a hint
def greeting(name: str):
    print(f"Hello {name}")


greeting("Dave")
greeting(3)


# addition func
#
# try to avoid print statements
def add(x, y):
    return x + y


# divisions function - expect output to be a float
def division(x: int, y: int) -> float:
    return x / y


# can set default value within a func and then when called, no arguments are required
def subtract(x=5, y=3):
    return x - y
