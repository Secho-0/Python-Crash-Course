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

            Chapter 6
1) create a dictionary named <alien_0> that contains the keys:
    - color
    - points
    - speed
    - x position
    - y position

"""
# using to select a random alien color each time
import random as r

# user info
user_points = 0
aliens_killed = 0

# alien info
aliens = []
colors = {'green': 5, 'blue': 10, 'purple': 15}
speeds = {'slow': 1, 'medium': 2, 'fast': 3}

# create aliens
for i in range(25):
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
    # print(new_alien)
print("\n\t\t\tThere's " + str(len(aliens)) + " aliens! Look out!!\n")

# simulated 25 alien game
while aliens_killed < 25:
    # check & set speeds
    for alien in aliens:
        if alien['speed'] == 'slow':
            alien['x_incr'] = r.randint(-1, 1)
        elif alien['speed'] == 'medium':
            alien['x_incr'] = r.randint(-2, 2)
        elif alien['speed'] == 'fast':
            alien['x_incr'] = r.randint(-3, 3)
        else:  # show error if not listed above
            print("Alien speed set incorrectly.")

    alien = r.choice(aliens)
    # color 1 aliens
    if alien['color'] == list(colors.keys())[0]:
        print("You shot a " + alien['color'] + " alien, you earned 5 pts!")
        alien['points'] = 5
        user_points += alien['points']
        # alien['x_pos'] += alien['x_incr']

    # color 2 aliens
    elif alien['color'] == list(colors.keys())[1]:
        print("You shot a " + alien['color'] + " alien, you earned 10 pts!")
        alien['points'] = 10
        user_points += alien['points']
        # alien['x_pos'] += alien['x_incr']

    # color 3 aliens
    else:
        print("You shot a " + alien['color'] + " alien, you earned 15 pts!")
        alien['points'] = 15
        user_points += alien['points']
        # alien['x_pos'] += alien['x_incr']

    aliens_killed += 1
    aliens.remove(alien)

print("\n\t\t\tYou've shot " + str(aliens_killed) +
      " of the aliens!\n\t\t\t\tYou earned " +
      str(user_points) + " points!\n")
