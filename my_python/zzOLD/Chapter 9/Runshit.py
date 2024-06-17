##Runshit
import ExercisesNine as EN
import ExercisesNine2 as EN2

from collections import OrderedDict

chucky = EN.Restaurant ("Chuckys House of Cheese","DAIRY MOTHERFUCKER")
chucky.open_close()
chucky.description()
chucky.open_close()
chucky.set_served()
chucky.increment_served()
print()

lacy = EN.User("Lacy","Derp")
lacy.greet()
lacy.greet()
lacy.greet()
lacy.greet()
lacy.greet()
lacy.greet()
print(str(lacy.login_att_count))
lacy.reset_attempts()
print(str(lacy.login_att_count))
lacy.describe()
lacy.greet()
print(str(lacy.login_att_count))
print()

privlist = [ 'add user', 'delete user', 'delete post',
                                           'ban user', 'unban user'
                ]
greg = EN.Admin("Greg","Herman",privlist)
greg.greet()
greg.describe()
greg.privleges.show_priv()
privlist = []
greg.privleges.change_priv(privlist)
greg.privleges.show_priv()
print()

flavorlist = ['wat', 'this', 'is', 'a', 'test']
ian = EN.IceCreamStand("Ians Ice Cream","Really?")
ian.whatflavors
print()

joel = EN.IceCreamStand("Joels Jubilant Joke","ICE CREAM FUCKFACE")
joel.whatflavors()
joel.changeflavors(flavorlist)
joel.whatflavors()
print()

superoo = EN.ElectricCar("Jake","A","2020")
superoo.battery.upgrade_battery()
print()

##9-13
favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
        language.title() + ".")
print()
##9-13 End

dsix = EN2.Die()

dsix.roll(5)
dsix.saved_rolls(5)
dsix.roll_stats()
