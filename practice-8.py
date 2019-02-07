#Python practice 8
#
#
people = 30
cars = 40
trucks = 15


if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")

#STUDY DRILLS
#1. Try to guess what elif and else are doing.
#2. Change the numbers of cars, people, and trucks, and then trace through each if-statementto see what will be printed.
#3. Try some more complex Boolean expressions like cars > people or trucks < cars.
#4. Above each line write a comment describing what the line does.
