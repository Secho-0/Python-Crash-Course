"""
##########################################
#               List Basics              #
# Accessing, Changing, Sorting & Lengths #
##########################################
"""


# a list
bikes = ['trek', 'canondale', 'cube', 'redline']
print("This is the list 'bikes:")
print(bikes)

###############################################################################
#                             Accessing Lists                                 #
#  - list elements start at 0 for the first and move up from there            #
#    (element 0 is the first item, element 1 is the 2nd                       #
#     element 2 the 3rd and so on)                                            #
#  - list elements can be access backwards too                                #
#    (element -1 is the last, element -2 is the 2nd last etc)                 #
# - list elements can b e manipulated with methods the same way variables can #
###############################################################################

print("The first element in bikes is: " + bikes[0])
print("The first element in bikes, but Title Case is: " + bikes[0].title())


# use individual items from a list, you can call specific elements,
#       not just the first in the list (0)
MESSAGE = "My first bike was a " + bikes[2].title() + "."
print(MESSAGE)


####################################################
# Changing Lists
# - you can specify elements and change them (similar to variable declaration)
# - using .append() you can add items to the end of a list
#           [foo.append(<inserted value>)]
# - using .insert() you can add items to a list at a specified point
#           [foo.insert(<desired index>,<inserted value>)]
# - using
####################################################

# CHANGING
print("\t\tChanging")
motorbikes = ['honda', 'yamaha', 'suzuki']
print("\nthis is the list of 'motorbikes': ")
print(motorbikes)
motorbikes[0] = 'ducati'
print("\nlets see if our changes work: ")
print(motorbikes)

# APPENDING
motorbikes.append('honda')
print("\t\tAppending")
print("\nthis should put honda back, lets see: ")
print(motorbikes)

# INSERTING
print("\t\tInserting")
motorbikes.insert(0, 'vespa')
print("\ni inserted something lets see if its there: ")
print(motorbikes)

#  REMOVING
print("\t\tRemoving from Lists")
print("\njust to reiterate, this is what our list has on it: ")
print(motorbikes)

print("Using Delete")
del motorbikes[0]
print("\nlets see if deleting stuff worked: ")
print(motorbikes)

print("Using .pop()")
popped = motorbikes.pop()
print(motorbikes)
print(popped)

print("Using .pop(<index>) to specify an element")
popped_specific = motorbikes.pop(2)
print("did you know i have a " + popped_specific)

# you can use .remove() to remove specific elements, variables or written

print("Using .remove()")
print(motorbikes)

print("Using a specific term")
motorbikes.remove('ducati')
print(motorbikes)

print("Using a variable")
LAST_ONE = 'yamaha'
motorbikes.remove(LAST_ONE)

print(motorbikes)

#################################################################
#                    Sorting Lists (& Length)                   #
# - sorted() function doesnt effect  the list                   #
# - .sort() effects the list itself, and must be used           #
#       prior to printing out the sorted list                   #
# - .reverse() works similar to .sort() but does no sorting and #
#       only reverses the current order of elements in a list   #
#################################################################

cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Original list:")
print(cars)

# using sorted() function
print("Here's a list sorted with the sorted() fucntion")
print(sorted(cars))
print("see the original list is still preserved")
print(cars)

# using .sort()
print("Here's a list sorted with .sort()")
cars.sort()
print(cars)
print("see the original list was effected if we do it this way")

# using .reverse() to reverse a list, regardless of sort-state
print("lets try using .reverse()")
cars.reverse()
print(cars)

# using len() function to get a list length

print("The length of the list 'cars' is: " + str(len(cars)))
print("The length of the list 'motorbikes' is: " + str(len(motorbikes)))
