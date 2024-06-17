"""
        Chapter 5
      If Statements
"""

# basic if-statement demonstration
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if len(car) < 4:
        print(car.upper())
    else:
        print(car.title())

# types of numerical comparison & conditional testing
#   == for comparing equals
#   != for not equal
#   <  for less than
#   >  for more than
#   <= for less than or equal to
#   >= for greater than or equal to

age_0 = 18
age_1 = 23

if age_0 >= 18 and age_1 >= 21:
    print("You're both welcome in, only one of you can drink though.\n")


# checking whether a value is in a list

my_pizza = ['pepperoni', 'salami', 'feta']


def get_toppings():
    """ Prints a list of toppings from a pizza

    Returns:
        string: Empty string for easy concatenation
    """
    for topping in my_pizza:
        print(topping)
    return ""


removal = input("what topping would you like to remove?" + get_toppings())
my_pizza.remove(removal)
print("\nOkay your pizza has been altered" + get_toppings())
