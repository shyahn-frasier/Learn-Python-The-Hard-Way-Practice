# Number of cars available
cars = 100
# How much space is in each car
space_in_a_car = 4.0
# How many drivers are available
drivers = 30
# How many passengers need to be transported
passengers = 90
# How many cars do not need to be driven
cars_not_driven = cars - drivers
# How many cars will be driven
cars_driven = drivers
# How many people can be transported
carpool_capacity = cars_driven * space_in_a_car
# The average amount of passengers that will be put in each car
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today")
print("We need to put about", average_passengers_per_car, "in each car.")