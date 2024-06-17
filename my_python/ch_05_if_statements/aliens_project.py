"""
            Chapter 5
          ALIEN PROJECT
1) Create a list with 3 colors of alien
    1b) Write an if statement that if the color is 'Color 1', player earns 5pts
    1c) Write a test to pass, and a test to fail, the if-statement
        the pass should include the 5pts awarded,
        the fail doesnt need a print statement

2) Write an else-if-else chain that works for all colors of alien
    Color 1 - 5 Pts
    Color 2 - 10 Pts
    Color 3 - 15 Pts
"""
# using to select a random alien color each time
import random

alien_colors = ['green', 'blue', 'purple']
cur_alien_color = random.choice(alien_colors)
used_colors = []
# color 1 aliens
while len(used_colors) < 3:
    if cur_alien_color == alien_colors[0]:
        print("You shot a " + cur_alien_color + " alien, you earned 5 pts!")
        if cur_alien_color not in used_colors:
            used_colors.append(cur_alien_color)

    # color 2 aliens
    elif cur_alien_color == alien_colors[1]:
        print("You shot a " + cur_alien_color + " alien, you earned 10 pts!")
        if cur_alien_color not in used_colors:
            used_colors.append(cur_alien_color)

    # color 3 aliens
    else:
        print("You shot a " + cur_alien_color + " alien, you earned 15 pts!")
        if cur_alien_color not in used_colors:
            used_colors.append(cur_alien_color)
    cur_alien_color = random.choice(alien_colors)
print("You've shot all the aliens!")
