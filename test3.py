"""
Third Python Dabble
- If Statments
- While Statements
- Variable conversion
- User Input
"""

def python3(d,e,f):
    x = d
    y = e
    z = f
    a = int(input('Enter a Number: '))
    iteration = 0
    total = 0

    while iteration < a:
        total = total + x + y + z
        iteration = iteration + 1
    if total < ((x + y + z)*5):
        print('You scored below 50!')
        score = str(total)
        msg = 'Your score was: '

        return print(msg + score)
    else:
        print('You scored above 50!')
        score = str(total)
        msg = 'Your score was: '

        return print(msg + score)

print(str(python3(54,16,10)) + '. Hope Roulette went well.')
