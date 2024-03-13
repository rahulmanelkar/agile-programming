# Example #1
x = "Assert Testing"
assert x == "Assert Testing"

# Example #2
x= 10
assert x > 0
print("x is a integer")

# Example #3
def square (x):
    assert x >= 0, ' positive number is allowed'
    return x*x

try :
    n = square (-2)
except AssertionError as msg:
    print(msg)

# Example #4
def avg(marks):
    assert len(marks) != 0, "List is Empty"
    return sum(marks)/len(marks)

mark2 = [20, 21,22,23,24,25]
print ("Ave of mark2: ", avg(mark2))

mark1 = []
print ("Ave of mark1: ", avg(mark1))
