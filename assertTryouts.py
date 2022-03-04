x = "Assert Testing"

assert x == "Assert Testing"

x= 10
assert x > 0
print("x is a integer")

def square (x):
    assert x >= 0, ' positive number is allowed'
    return x*x

try :
    n = square (-2)
except AssertionError as msg:
    print(msg)
