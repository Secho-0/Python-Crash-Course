"""
                Chapter 4
    - Introduction to and working with tuples
"""

# starting with tuples
dims = (200, 50)

print(dims[0])
print(dims[1])

# notice how trying toc hange a specific element in the tuple isnt allowed
# dims[0] = 1

# in order to change a tuple you have to simply define a new one with the same
# name
print(dims)
dims = (400, 100)
print(dims)
