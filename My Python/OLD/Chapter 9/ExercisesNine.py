##Chapter 9 Exercises

class Restaurant():
    """Open a Restaurant"""

    def __init__(self,name,specialty):
        """Set a name and specialty food"""
        self.name = name
        self.specialty = specialty
        self.status = False
        self.served = 0


    def description(self):
        """Describe the establishment"""
        print('Here at ' + self.name.title() + ' we specialize in ' + self.specialty + '.')

    def open_close(self):
        """Open or Close your doors"""
        if self.status == True:
            self.status = False
            print('We are now Closed.')
        else:
            self.status = True
            print('We are now Open.')
            
## End 9-1 
## Start 9-4
    def set_served(self):
        servedamt = input("How many people have been served? ")
        servedamt = servedamt.strip()
        self.served = int(servedamt)
        print(str(self.served))
            
    def increment_served(self):
        DAY = 300
        WEEK = 2100
        MONTH = 8400
        YEAR = 100800

        select = input('how long has passed?')
        print(select)
        select = select.strip()
        print(select)
        select = select.lower()
        print(select)

        if select.startswith('d'):
            self.served += DAY
            print(str(self.served))
        elif select.startswith('w'):
            self.served += WEEK
            print(str(self.served))
        elif select.startswith('m'):
            self.served += MONTH
            print(str(self.served))
        elif select.startswith('y'):
            self.served += YEAR
            print(str(self.served))
##Start 9-6
class IceCreamStand(Restaurant):

    def __init__(self,name,specialty):
            super().__init__(name,specialty)
            self.flavors = ['vanilla', 'chocolate', 'neopolitian',
                                        'vanilla berry', 'rocky road', 'chocolate fudge'
                                        ]

    def whatflavors(self):
        print("We currently have:")
        for flavor in self.flavors:
            print("\t-" + flavor.title())

    def changeflavors(self,flavorlist):
        self.flavors = flavorlist
        
##End 9-6


class User():
    """Setup a User"""

    def __init__(self,first,last):
        """Gather Basic User Data"""
        self.fullname = first.title() + ' ' + last.title()
        self.firstname = first
        self. lastname = last
        self.uname = first[:2]+last
        self.login_att_count = 0

    def describe(self):
        print('Username: ' + self.uname + '\n'
                  + 'First Name: ' + self.firstname + '\n'
                  + 'Last Name: ' + self.lastname + '\n')

    def greet(self):
        self.login_attempt();
        print('Whatup ' + self.uname + '!')
## End 9-3
## Start 9-5
    def login_attempt(self):
        self.login_att_count += 1

    def reset_attempts(self):
        self.login_att_count = 0
## End 9-5
## Start 9-7 & 8

class Admin(User):

    def __init__(self, first, last, privlist):
        super().__init__(first,last)
        self.privleges =  Privleges(privlist)

class Privleges():

    def __init__(self,privlist):
        self.privleges = privlist

    def show_priv(self):
        if len(self.privleges) >= 1:
            print("User has access to the following privleges: ")
            for privlege in self.privleges:
                print("\t- " + privlege.title())
        else:
            print("User has no privleges")
            
    def change_priv(self,privleges):
        self.privleges = privleges
## End 9-7 & 8

## Star 9-9
## Imports from Python Crash Course Resources here to consolidate upon looking back

## import car.py
"""A class that can be used to represent a car."""

class Car():
    """A simple attempt to represent a car."""

    def __init__(self, manufacturer, model, year):
        """Initialize attributes to describe a car."""
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.manufacturer + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
        
    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

##Import electric_car.py
"""A set of classes that can be used to represent electric cars."""

class Battery():
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=60):
        """Initialize the batteery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")  
        
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 60:
            range = 140
        elif self.battery_size == 85:
            range = 185
            
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

#9-9 Start
    def upgrade_battery(self):
        if self.battery_size < 85:
            self.get_range()
            self.battery_size = 85
            print("Battey size set to 85!")
            self.get_range()
        else:
            print("Battery size is already 85!")
#9-9 End
        
class ElectricCar(Car):
    """Models aspects of a car, specific to electric vehicles."""

    def __init__(self, manufacturer, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(manufacturer, model, year)
        self.battery = Battery()

