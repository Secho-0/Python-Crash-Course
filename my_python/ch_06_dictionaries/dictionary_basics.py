"""
      Chapter 6
    DICTIONARIES
"""

import random as r

# dictionaries are storage for key-value pairs
# <key>: <value>
# keys and values can both be a variety of data types,
# typically
alien_0 = {'color': 'green', 'points': 5}
new_points = 0

# you can call on individual key's from a dictionary

print("\n<calling individual keys>\nThe alien is " +
      alien_0['color'].title() + " and is worth " +
      str(alien_0['points']) + " points.\n")


# adding new key:value pairs is as simple as declaring them
print("<adding new unique key's w/ associated values>")
alien_0['x pos'] = 0
alien_0['y pos'] = 25

print(alien_0)
print("\n<changing a key's value>")
# changing / modifying a key, is as simple as declaring the new value
alien_0['color'] = 'purple'
print(alien_0['color'] + '\n')

# move alien to the right
alien_0['speed'] = 'medium'
x_increment = 0

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
elif alien_0['speed'] == 'fast':
    x_increment = 3
else:
    print("Alien speed set incorrectly.")

print("<showing we can increment w/ a variable, specific value, etc.>")
alien_0['x pos'] += x_increment
print(alien_0)
print()

# removing keyvalue pairs is similar to lists, and as a reminder remains
# permanent

# looping through a dictionary

print("\n<getting keys and values>\nKey:Value")
for key, value in alien_0.items():
    print(key + ": " + str(value))
print("\n<getting just keys>")
# using key specifically
for key in alien_0.keys():
    print(key)
print("\n<getting just values>")
# using values specifically
for value in alien_0.values():
    print(value)
print()

# nesting dictionaries

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'blue', 'points': 10}
alien_2 = {'color': 'purple', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

print("<printing a list of dictionaries to demosntrate nesting>")
for alien in aliens:
    print(alien)


# reset aliens
aliens = []

# make 25 aliens
for i in range(25):
    colors = {'green': 5, 'blue': 10, 'purple': 15}
    speeds = {'slow': 1, 'medium': 2, 'fast': 3}

    new_alien = {
        'color': '',
        'points': 0,
        'speed': 'medium',
        'x_incr': 2,
        'x_pos': 0,
        'y_pos': 25
    }
    new_alien['color'] = r.choice(list(colors.keys()))
    new_alien['points'] = colors[new_alien['color']]

    new_alien['speed'] = r.choice(list(speeds.keys()))
    new_alien['x_incr'] = speeds[new_alien['speed']]
    aliens.append(new_alien)
print()

# print the new aliens
i = 0
while i < len(aliens):
    for alien in aliens:
        if i % 5 == 0:
            print()
        print(alien)
        i += 1
print("\nThere's now " + str(len(aliens)) + " aliens! Look out!!\n")
