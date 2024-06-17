"""
                            Chapter 4 Project from Exercises


                                    PIZZA PLACE
    1) Store the name of 3 pizzas on a list and print it
        1b) Add more text than just the pizza names, give a statement about
            each pizza instead

                EXAMPLE: "pepperoni pizza" => "i really like pepperoni pizza"

        1c) Add a line outside the for loop that states how much you like pizza
            The statement should have at least 3 lines about the pizzas you
            like and a second declaration of your feelings towards pizza

    2) Create a copy of your pizza list named "friends_pizzas"
        2b) add a unique pizza to both list of pizzas
        2c) prove that they are now unique lists and print each one.
            each should say something to the effect of:

                            "my (friends) favourites are:"
"""


my_pizzas = ['pepperoni', 'sausage', 'cheese']
print("I really enjoy ", end=" ")
for pizza in my_pizzas:
    print(pizza, end=" ")
print("pizzas. They're probably my favourite\n")
print("""I really enjoy pizza.
Pepperoni is a really comfortable one
Sausage is good just cause its a bit differnt, but still protein
Cheese, is great because its the best to have with dips""")

friends_pizzas = my_pizzas[:]
my_pizzas.append("feta and onion")
friends_pizzas.append("bbq chicken")
print("My favourite pizzas are:")
for pizza in my_pizzas:
    print(pizza)

print("My friends favourite pizzas are:")
for pizza in friends_pizzas:
    print(pizza)
