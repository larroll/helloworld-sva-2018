# let the user know what's going on
print ("Welcome to MadLibs!")
print ("Answer the questions below to play.")
print ("-----------------------------------")

# variables containing all of your story info
year = raw_input("Name any year: ")
food = raw_input("Favorite food: ")
location1 = raw_input("City you were born: ")
name1 = raw_input("Name someone in the class: ")
name2 = raw_input("Enter your name: ")
animal = raw_input("Name an animal: ")
color = raw_input("What's your favorite color?: ")
actor = raw_input("Name an Actor you recently saw in a movie: ")

# this is the story. it is made up of strings and variables.
# the \ at the end of each line let's the computer know our string is a long one
# (a whole paragraph!) and we want to continue more code on the next line. 
# play close attention to the syntax!

story = "The year is " + year + " and the once beloved " + food + " is no longer available in " + location1 + "." \
" The only person who has access to " + food + " is the dark sorcerer, " + name1 + ". " \
"One day " + name2 + " travels to the secret floating castle of " + name1 + " with the help of a flying " + color + " " + animal + " named " + actor + " to win back " + food + " for all the land." \
" When " + name2 + " and " + actor + " arrive, there are hundreds of platters of " + food + " waiting for them." \
" Overcome with excitement about seeing " +food+ " again, they eat it immediatley without thought. \
All of a sudden they hear the evil laughter of " +name1+ " and realize, as they start to slip out of conciousness..." \
"that they have been foiled once again." \



# finally we print the story
print (story)