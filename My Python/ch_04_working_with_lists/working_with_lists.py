"""
        CHAPTER 4 - WORKING WITH LISTS
"""

#########################
# Looping through Lists #
#########################

MAGICIANS = ['alice', 'david', 'carolina']

for magician in MAGICIANS:
    print(magician.title() + ", that was as great trick")

#   To show indentation matters, since this 'inside' (indented further than)
#   the for-loop it will run for each 'magician' and the one of equal
#   indentation will run after the loop exits

    print("I cant wait to see another trick, " + magician.title() + ".\n")
print("Thanks for a great show everyone")


################################
#   Making Numerical Lists     #
# - range() function explored  #
################################

# showing how the range function works, and its shortcomings
#   (ending before the end number not on the end number)

for value in range(1, 5):
    print(value, end=" ")

print()
for value in range(1, 6):
    print(value, end=" ")
print()

# range can be used to make lists simple
numbers = list(range(1, 6))
print(numbers)

# range can count by a number as wel
even_numbers = list(range(0, 11, 2))
print(even_numbers)

# combining loops, range and appending
squares = []
for number in range(1, 11):
    square = number ** 2
    squares.append(square)
print(squares)

# put much mroe concisely
squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)

# some simple stats with lists
one_to_zero = []
for i in range(1, 10):
    one_to_zero.append(i)
one_to_zero.append(0)

for number in one_to_zero:
    print(number, end=" ")
print()
print(min(one_to_zero))
print(max(one_to_zero))
print(sum(one_to_zero))

############################################################################
# list comprehension                                                       #
# - lists can be built using expressions rather than defined with external #
#   loops                                                                  #
# - remaking the one above in its absolute simplest form and using cubes   #
# instead of squares (to show they are different)would be:                 #
############################################################################

squares = [value**3 for value in range(1, 11)]
print(squares)


##################
# slicing a list #
##################
players = ['charles', 'martina', 'michael', 'florence', 'eli']

# between two points
print(players[0:3])

# to an end point
print(players[:3])

# from a starting point
print(players[1:])

# looking through a slice
print("\nYour team has ", end=" ")
for player in players[:3]:
    print(player.title(), end=" ")
print("\n")


##################
# copying a list #
##################

my_team = players[3:]
my_team.append('eric')
players = players[:3]

print(players)
print(my_team)
