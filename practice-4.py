# Python practice #4
# A string is usually a bit of text you want to display to someone or “export” out of the program you are writing.
# Python knows you want something to be a string when you put either " (double-quotes) or '(single-quotes) around the text.
# You also see that I have to use a special type of string to “format”; it’s called an “f-string”
#
#
types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)


print("Mary had a little lamb.")
print("Its fleece was white as {}.".format('snow'))
print("And everywhere that Mary went.")
print("." * 10) # what'd that do?

#1. Go through this program and write a comment above each line explaining it.
#2. Find all the places where a string is put inside a string. There are four places.
#3. Are you sure there are only four places? How do you know? Maybe I like lying.
#4. Explain why adding the two strings w and e with + makes a longer string.
