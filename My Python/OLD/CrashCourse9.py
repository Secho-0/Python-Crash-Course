##"""Crash Course Chapter 9"""
##
##class Dog():
##    """MAKE A DOG"""
##
##    def __init__(self,name,age):
##        """Name and Age of Dog"""
##        self.name = name
##        self.age = age
##
##    def sit(self):
##        """Tell the Dog to Sit"""
##        print(self.name.title() + " is now sitting.")
##
##    def roll_over(self):
##        """Tell the Dog to Rollover"""
##        print(self.name.title() + " rolled over!")
##
##charlie = Dog("Charlie",3)
##
##print("My dogs name is " + charlie.name + " he is " + str(charlie.age) + " years old.")
##charlie.sit()
##charlie.roll_over()
##print()
##lucy = Dog("Lucy", 5)
##
##print("My dogs name is " + lucy.name + " he is " + str(lucy.age) + " years old.")
##lucy.sit()
##lucy.roll_over()

class Resteraunt():
    """Open A Resteraunt, witha specialty cuisine, name and waitlist"""
    status = False
    def __init__(self,name,specialty,capacity):
        """Set the name , specialty and seating capacity"""
        self.name = name
        self.specialty = specialty
        self.capacity = capacity

    def describe_resteraunt(self):
        print(self.name.title() + " is a resteraunt specializing in " +  self.specialty + "cuisine." )

    def open_close(self):
        if self.status == False:
            self.status = True
            print("Bills is now open!")
            print(self.status)
            return
        
        else:
            self.status = False
            print("Bills is closed . C'ya tomorrow!")
            print(self.status)
            return


##Testing

bills = Resteraunt("Bills House of Chicken", "Southern", 120)

bills.describe_resteraunt()
bills.open_close()
bills.open_close()

lukes = Resteraunt("Luke's House of Lard", "LARD", 120)
lukes.describe_resteraunt()

mabels = Resteraunt("Mabel's House of Pancakes", "Breakfast", 120)
mabels.describe_resteraunt()
