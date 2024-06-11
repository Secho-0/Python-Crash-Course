"""
######################
#    List Basics     #
######################
"""

bikes = ['trek', 'canondale', 'cube', 'redline']
print("This is the list 'bikes:")
print(bikes)

#accessing lists 
#   - list elements start at 0 for the first and move up from there 
#     (element 0 is the first item, element 1 is the 2nd
#      element 2 the 3rd and so on)
#   - list elements can be access backwards too
#     (element -1 is the last, element -2 is the 2nd last etc)
#   - list elements can b e manipulated with methods the same way variables can

print("The first element in bikes is: " + bikes[0])
print("The first element in bikes, but Title Case is: " + bikes[0].title())


# use individual items from a list
message = "My first bike was a " + bikes[2].title() + "."
print(message)

# changing , adding and removing things from lists

#   changing
motorbikes = ['honda', 'yamaha', 'suzuki']
print("\nthis is the list of 'motorbikes': ")
print(motorbikes)
motorbikes[0]= 'ducati'
print("\nlets see if our changes work: ")
print(motorbikes)

#   adding
motorbikes.append('honda')
print("\nthis should put honda back, lets see: ")
print(motorbikes)

#   inserting
motorbikes.insert(0, 'vespa')
print("\ni inserted something lets see if its there: ")
print(motorbikes)

#   removing 
print("\njust to reiterate, this is what our list has on it: ")
print(motorbikes)
del motorbikes[0]
print("\nlets see if deleting stuff worked: ")
print(motorbikes)

popped = motorbikes.pop()
print(motorbikes)
print(popped)

popped_specific = motorbikes.pop(2)
print("did you know i have a " + popped_specific)

#you can use .remove() to remove specific elements, variables or written

print(motorbikes)
motorbikes.remove('ducati')
print(motorbikes)
last_one = 'yamaha'
motorbikes.remove(last_one)
print(motorbikes)