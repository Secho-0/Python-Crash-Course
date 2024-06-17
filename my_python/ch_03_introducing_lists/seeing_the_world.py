"""
                        INSTRUCTIONS FOR CHAPTER 3
                            Seeing The World

        1) Store 5 locations you'd like to visit in a list
            1b) Print the list (raw python list is fine)
        2) user sorted() to print your list in order w/o modifying the original
            2b) print both sorted() and original list
        3) use .reverse() to reverse the original order
            3b) print reversed list
            3c) repeat 4 and 4b to restore the original order
        4) use .sort() to sort it alphabetically
            4b) print the sorted list
            4c) rinse and repeat, but reverse the search order
"""

PLACES_TO_VISIT = ['Kinsale', 'Berlin', 'London', 'Athens', 'Tokyo']

print("Here's the places I'd like to visit:")
print(PLACES_TO_VISIT)

print("or rather, sorted:")
print(sorted(PLACES_TO_VISIT))
print("Don't worry our original list is still intact tho")
print(PLACES_TO_VISIT)

PLACES_TO_VISIT.reverse()
print("look i swapped the order!")
print(PLACES_TO_VISIT)
PLACES_TO_VISIT.reverse()
print("ok ok, i swapped them back")
print(PLACES_TO_VISIT)

PLACES_TO_VISIT.sort()
print("I sorted them again, but permanently this time")
print(PLACES_TO_VISIT)

PLACES_TO_VISIT.sort(reverse=True)
print("aaand i reversed it")
print(PLACES_TO_VISIT)
