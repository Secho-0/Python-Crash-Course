"""
##########################
#    Datatype Basics     #
##########################
"""


###############################
#    Characters & Strings     #
###############################

# Absolute basics
example_a = "This is a string"
example_b = " this is also a string "

print("\n" + example_a +"\n"+ example_b)

# Playing with Cases
print(example_a.title() + " | this is Title Case")
print(example_a.upper() + " | this is UPPERCASE")
print(example_a.lower() + " | this is lowercase")

# Concatenation
example_c = example_a + " | " + example_b

print(example_c + " | this is example_c")
print(example_c.title() + " | this is example_c but Title Case")

message = example_c.title()
print(message + " | you can even store the concatenated *message* as its own variable\n")

# Whitespace exercises

print("this is a newline \ndid you know that you can add tabs too?\n\tsee?\n\nA new line is added with \\n and a tab (four spaces) is added with \\t\n")

print(example_b.strip() + " an example of .strip()")
print(example_b.lstrip() + " an example of .lstrip()")
print(example_b.rstrip() + " an example of .rstrip()")


##################
#    Numbers     #
##################

# Integers

a = 2
b = 3
c = 4

print("you can add: "+ str(a+b))
print("you can subtract: " + str(a-b))
print("you can multiply: " + str(a*b))
print("you can divide: " + str(a/b))
print("you can even do exponents: " + str(a**b))
print("Python also supports Order of operations look: " + str((a+b*c)) + " | " + str(((a+b)*c)) + " see?")

# Floats 
a = a/10
b = b/10
c = c/10
print("Holy shit you can do the  same thing with floats too ")
print("you can add: "+ str(a+b))
print("you can subtract: " + str(a-b))
print("you can multiply: " + str(a*b))
print("you can divide: " + str(a/b))
print("you can even do exponents: " + str(a**b))
print("Python also supports Order of operations look: " + str((a+b*c)) + " | " + str(((a+b)*c)) + " see?")