def find_factors(num):
    factors = []
    for i in range(1,num+1):
        if num%i==0:
            factors.append(i)
    return factors

number = 24
print(f"The factors of {number} is {find_factors(number)}")