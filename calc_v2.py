import math
import sys

print("\nWelcome! This calculator runs off three variables")

#
# check if entered value is an integer
#
def check_numeric_input(val, str):
  if (val.isnumeric()):
    return True
  else:
    print("\nValue entered for %s \"%s\" must be an integer" % (str, val))
    return False

#
# compute the squares of each variable
#
def comp_squares(a, b, c):
  in_squares = True
  ans = input("""\nWhat would you like to see?

  1 - a^2
  2 - b^2
  3 - c^2
  4 - Print All
  0 - Return to Main Menu

  > """)
  while in_squares == True:
    print("")
    if (ans == "1"): 
        print("a^2 is %.0f" % a**2)
    elif (ans == "2"):
        print("b^2 is %.0f" % b**2)
    elif (ans == "3"):
        print("c^2 is %.0f " % c**2)
    elif (ans == "4"):
        print("A^2 is %.0f\nB^2 is %.0f\nC^2 is %.0f" % (a**2,b**2,c**2))
    else:
        x = False
        print("\nOption \"%s\" is not a valid option. Returning to Main Menu" % ans)
#
# compute the square roots of each variable
#
def comp_square_roots(a, b, c):
  ans = input("""\nWhat would you like to see?

  1 - Square Root of a
  2 - Square Root of b
  3 - Square Root of c

  > """)
  print("")
  if (ans == "1"): 
    print("The Square Root of a is %.2f" % math.sqrt(a))
  elif (ans == "2"):
    print("The Square Root of b is %.2f" % math.sqrt(b))
  elif (ans == "3"):
    print("The Square Root of c is %.2f" % math.sqrt(c))
  else:
    print("\nOption \"%s\" is not a valid option. Returning to Main Menu" % ans) 
    return

def comp_exponential(a, b, c):
  ans = input("""\nWhat would you like to see?

  1 - a^a
  2 - a^b
  3 - a^c
  4 - a^d
  5 - b^a
  6 - b^b
  7 - b^c
  8 - b^d
  9 - c^a
  10 - c^b
  11 - c^c
  12 - c^d
  0 - Return to Main Menu

**Note: d is for User Input**

  > """)
  print("")
  if (ans == "1"): 
    print("a^a is %.0f " % a**a)
  elif (ans == "2"):
    print("a^b is %.0f " % a**b)
  elif (ans == "3"):
    print("a^c is %.0f " % a**c)
  elif (ans == "4"): 
    d = input("Enter desired Exponent: \n")
    print("a^d is %.0f " % a**int(d))
  elif (ans == "5"):
    print("b^a is %.0f " % b**a)
  elif (ans == "6"):
    print("b^b is %.0f " % b**b)
  elif (ans == "7"): 
    print("b^c is %.0f " % b**c)
  elif (ans == "8"): 
    d = input("Enter desired Exponent: \n")
    print("a^d is %.0f " % a**int(d))
  elif (ans == "9"):
    print("c^a is %.0f " % c**a)
  elif (ans == "10"):
    print("c^b is %.0f " % c**b)
  elif (ans == "11"): 
    print("c^c is %.0f " % c**c)
  elif (ans == "12"): 
    d = input("Enter desired Exponent: \n")
    print("a^d is %.0f " % a**int(d))
  else:
    print("\nOption \"%s\" is not a valid option. Returning to Main Menu" % ans)
    return
#
#compute the quotient of each variable
#
def comp_division(a, b, c):
  ans = input("""\nWhat would you like to see?

  1 - Quotient of a/b
  2 - Quotient of a/c
  3 - Quotient of b/a
  4 - Quotient of b/c
  5 - Quotient of c/a
  6 - Quotient of c/b

  > """)
  print("")
  if (ans == "1"): 
    print("The Quotient of a/b is %.2f" % float(a/b))
  elif (ans == "2"):
    print("The Quotient of a/c is %.2f" % float(a/c))
  elif (ans == "3"):
    print("The Quotient of b/a is %.2f" % float(b/a))
  elif (ans == "4"): 
    print("The Quotient of b/c is %.2f" % float(b/c))
  elif (ans == "5"):
    print("The Quotient of c/a is %.2f" % float(c/a))
  elif (ans == "6"):
    print("The Quotient of c/b is %.2f" % float(c/b))
  else:
    print("\nOption \"%s\" is not a valid option. Returning to Main Menu" % ans) 
    return

#
#compute the product of each variable
#
def comp_multiplication(a, b, c):
  ans = input("""\nWhat would you like to see?

  1 - Product of a*b
  2 - Product of a*c
  3 - Product of b*c


  > """)
  print("")
  if (ans == "1"): 
    print("The Product of a*b is %.0f" % float(a*b))
  elif (ans == "2"):
    print("The Product of a*c is %.0f" % float(a*c))
  elif (ans == "3"):
    print("The Product of b*c is %.0f" % float(b*c))
  else:
    print("\nOption \"%s\" is not a valid option. Returning to Main Menu" % ans) 
    return
ct = 1
while True:
  print("""\nWhat would you like to do?\n
  1 - Squares
  2 - Square Roots
  3 - Exponentials
  4 - Division
  5 - Multiplication
  6 - Subtraction
  7 - Addition

  quit (type quit)""")

  ans = input("\nEnter number corresponding to option (iteration #%d): " % ct) 
  ct += 1

  if (ans[0:1].lower() == "q"):
    print("\nQuitting!\n")
    sys.exit()
  elif (ans == ""):
    print("\nNothing entered. Continuing...\n")
    continue

  print("")
  a = input("  Enter numeric value for a: ")
  if (check_numeric_input(a, "a") == False):
    continue
  a1 = int(a) 
    
  b = input("  Enter numeric value for b: ")
  if (check_numeric_input(b, "b") == False):
    continue
  b1 = int(b) 

  c = input("  Enter numeric value for c: ")
  if (check_numeric_input(c, "c") == False):
    continue
  c1 = int(c) 

  if (ans == "1"): 
    print("\nRunning Squares for a=%d, b=%d, and c=%d" % (a1, b1, c1)) 
    comp_squares(a1, b1, c1)
  elif (ans == "2"):
    print("\nRunning Square Roots for a=%d, b=%d, and c=%d" % (a1, b1, c1)) 
    comp_square_roots(a1, b1, c1)
  elif (ans == "3"):
    print("\nRunning Exponentials for a=%d, b=%d, and c=%d" % (a1, b1, c1)) 
    comp_exponential(a1,b1,c1)
  elif (ans == "4"):
    print("\nRunning Quotients for a=%d, b=%d, and c=%d" % (a1, b1, c1))
    comp_division(a1, b1, c1)
  elif (ans == "5"):
    print("\nRunning Products for a=%d, b=%d, and c=%d" % (a1, b1, c1))
    comp_multiplication(a1, b1, c1)
    print("\netc..")
  elif (ans == "6"):
    print("\netc..")
  elif (ans == "6"):
    print("\netc..")
  elif (ans == "7"):
    print("\netc..")
  else:
    print("\nOption \"%s\" is not a valid option. Try again!" % ans) 


