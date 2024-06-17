# really basic input
print("<basic input demo>")
message = input("Tell me something to secho back~:\n\t")
# print(message)

print("<basic concatenation w/ input>")
print("You said: " + message)

# demosntrating types of while loops

print("\n<numerical whileloop>")
num = 1
while num <= 5:  # numerical while
    print(num, end=" ")
    num += 1

print("\n<input based while>")
while message != 'quit':  # input based while
    message = input("gief msg:  ")
    print(message)

print("\n<flag based while>")
active = True
while active:  # while, using a flag
    message = input("gief another:  ")
    if message == 'quit':
        active = False
    else:
        print(message)

print("\n<break based while>")
while True:  # while, using a break statement
    message = input("last msg , gief:  ")
    if message == 'quit':
        break
    else:
        print(message)

# introducing the continue statement
print("\n<introducing the continue statment>")
num = 0
while num < 10:
    num += 1
    if num % 2 == 0:
        continue  # skips rest of the loop
    print(num, end=" ")

# using while loops with a list
print("\n\n<using while with lists>")
unverified = ['sandra', 'dave', 'larry']
verified = []
while unverified:
    user = unverified.pop()
    print("Verifying: " + user.title())

    verified.append(user)
    print(user.title() + " has been verified.")

print("\n<using while to remove elements from a list>")
pets = ['cat', 'dog', 'gerbil', 'dog',
        'python', 'mouse', 'scorpion', 'jellyfish']
print(pets)

while 'dog' in pets:
    pets.remove('dog')
print(pets)


# using while & input to create a dictionary
print("\n<using while & input to create a dictionary>")
polling = True
responses = {}
while polling:
    # get name and favourite game
    name = input("What should we call you?\t")
    response = input("what is your favourite video game?\t")

    # store name as key, with repsonse as value
    responses[name] = response
    # print(responses) (TEST)
    repeat = input("Would you like to record another response? (Y)es/(N)o\t")
    if repeat.startswith('N'):
        polling = False

for name, response in responses.items():
    print("\n" + name + " enjoys playing " + response)
