def intro():
    print("This is a calculator")
    print("Enter 'q' to quit")
    print("Enter 1 for addition")
    print("Enter 2 for subtraction")
    print("Enter 3 for multiplication")
    print("Enter 4 for division")

class Calculator:
    def __init__(self):
        self.results = []

    def add(self, a, b):
        result= int(a) + int(b)
        self.results.append(result)
        return result

    def sub(self, a, b):
        result= int(a) - int(b)
        self.results.append(result)
        return result

    def mul(self, a, b):
        result= int(a) * int(b)
        self.results.append(result)
        return result

    def div(self, a, b):
        result= int(a) / int(b)
        self.results.append(result)
        return result

def main():
    print("Welcome to the calculator!")
    while True:
        intro()
        print("Enter your choice:",end=' ')
        choice = input()
        calculator = Calculator()
        choices = [calculator.add, calculator.sub, calculator.mul, calculator.div
                   ]
        if choice == 'q':
            break
        else:
            print("Enter first number:",end=' ')
            num1 = input()
            print("Enter second number:",end=' ')
            num2 = input()
            result = choices[int(choice)-1](num1,num2)
            print("Result of the operation:",result)



if __name__ == "__main__":
    main()
