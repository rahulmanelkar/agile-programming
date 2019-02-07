# Python Practice - 3
# Author : Paddu Melanahalli
#
#
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

# Remember that 4.0 is a floating point number. It’s just a number with a decimal point, and you need 4.0 instead of just 4 so that it is floating point.
# Write comments above each of the variable assignments.
# Make sure you know what = is called (equals) and that its purpose is to give data (numbers, strings, etc.) names (cars_driven, passengers).
# Remember that _ is an underscore character.
# What is the difference between = (single-equal) and == (double-equal)? The = (single-equal) assigns the value on the right to a variable on the left.
# The == (double-equal) tests whether two things have the same value
