##
# Mad Lib - A MORNING OF MISHAPS
#
# @author Jerry Zeng
# @course ICS3UC
# @date 2023/02/17 - LastModified
##

###*** DEFINITIONS ***#

# Gets a value POLITELY for each prompt.
def askFor(thing):
  result = None
  while True:
    #typed(f"Please provide {thing}: ", speed=0.005, ending='')
    result = input("Please provide " + thing + ": ")
    if result.strip() == '':
      print("\tERROR: please provide a valid input.")
    else:
      return result.strip()

# Returns proper pronoun for each case.
def pronoun(id, subject):
  if id == "m":
    return ["he", "him", "his"][subject]
  elif id == "f":
    return ["she", "her", "her(s)"][subject]
  else:
    return ["they", "them", "their(s)"][subject]

# Prompts user to continue running the program by pressing enter.
def pause():
  input("[PRESS ENTER]")

#*** INTRODUCTION ***#
print("Welcome to an exciting game of...")
print("MAD LIBS!!!")
print()

pause()
print()

print("The rules of this game are simple: provide the words that I ", end="")
print("ask for and I will generate a very random story for you to read!")
print()

print("Are you ready? Let\'s begin!")
print()

pause()
print()

#*** INPUT ***#
print('Following this message, provide input according to what the ', end='')
print("prompt demands.")
print("————————————————————")

name = askFor("your name")

# This loop continues looping until the user provides their gender.
while True:
  gender = askFor("your gender - male [m], female [f], other [nb]")
  if gender not in ["m", "f", "nb"]:
    print("\tERROR: invalid input, please try again.")
  else:
    break
  
celeb = askFor("the name of a famous person")
month = askFor("a month")
day = askFor("a day [number]")
place = askFor("a place")
action1 = askFor("an action verb [past tense]")
action2 = askFor("an action verb [ending with \"-ing\"]")
adjective = askFor("an adjective")
emergency = askFor("an emergency service")
food = askFor("a food")
phone = askFor("an object")
ride = askFor("any moving noun")
obstacles = askFor("a noun [plural]")
animals = askFor("an animal [plural]")
event = askFor("an event (the...)")
punishment = askFor("punishment [verb] (had to...)")

#*** OUTPUT ***#
print()
print("Generating story.........")
print("DONE.")
print()

pause()
print()

# Title Heading
print("\n\n\n\n\nA MORNING OF MISHAPS")
print("————————————————————\n")

# The comments before each section of print statements are the output.

# "The morning of {month} {day}, little {name} was walking to {place}."
print("The morning of", month, day + ",", "little", name, end='')
print(" was walking to", place + ".")
print()

# "It was a nice sunny day and so {he/she} smiled to {him/her}self pleasantly.
# The air was warm with a nice crisp breeze that lightly wisped {name}'s hair."
print("It was a nice sunny day and so", pronoun(gender, 0), "smiled", end="")
print(" to", pronoun(gender, 1) + "self", "pleasantly. The air was ", end="")
print("warm with a nice crisp breeze that lightly wisped", name + "'s hair.")
print()

pause()
print()

# "On the way to {place}, {name} saw {celebrity name} lying on the street.
# What happened to poor {celebrity name}? It seems that they may have been
# {action verb | past tense} in the middle of the street. Oh dear!"
print("On the way to", place + ",", name, "saw", celeb, "lying ", end="")
print("on the street. What happened to poor " + celeb + "? It seems ", end="")
print("that they may have been", action1, "in the middle of the ", end="")
print("street. Oh dear!")
print()

# "{celebrity name} screams for help just as {name} starts walking 
# towards them."
print(celeb, "screams for help just as", name, "starts walking towards them.")
print()

# "{name} helps by {action verb | -ing} them and calling the {emergency 
# service} before continuing on {his/her} way to {place}."
print(name, "helps by", action2, "them and calling the", emergency, end="")
print(" before continuing on", pronoun(gender, 2), "way to", place + ".")
print()

pause()
print()

# "Walking to {place} is quite tiring for {him/her}. 'What should I eat for
# breakfast,' says {name}, who forgot to eat breakfast this morning. Maybe
# if {name} stocked up on energy, {he/she} would be able to continue on."
print("Walking to", place, "is quite tiring for ", end='')
print(pronoun(gender, 1)+".", "\"What should I eat for breakfast,\" ", end="")
print("says", name + ",", "who forgot to eat breakfast this morning. ", end="")
print("Maybe if", name, "stocked up on energy,", pronoun(gender, 0), end="")
print(" would be able to continue on", pronoun(gender, 2), "journey.")
print()

# "As {he/she} walks into a store, {he/she} decides on {food}."
print("As", pronoun(gender, 0), "walks into a store, ", end="")
print(pronoun(gender, 0), "decides on " + food + ".")
print()

pause()
print()

# "On the street, there was a great abundance of {animals}."
print("On the street, there was a great abundance of", animals + ".")
print()

# "Noticing that {he/she} is almost late, it would be smart for {name} to call 
# using {his/her} {object} to hail a ride on a(n) {transportation} to {place}.
print("Noticing that", pronoun(gender, 0), "is almost late, it ", end="")
print("would be smart for", name, "to call using", pronoun(gender, 2), end=" ")
print(phone, "to hail a ride on a(n)", ride, "to", place + ".")
print()

pause()
print()

# "The ride was as comfortable as any ride on a(n) {transportation} would be, 
# but due to {plural noun} and {plural animals} on the road, there was a great
# big traffic jam."
print("The ride was as comfortable as any ride on a(n)", ride, end="")
print(" would be, but ", end="")
print("due to", obstacles, "and", animals, "on the road, there was a ", end="")
print("great big traffic jam.")
print()

# "Sadly, because this mode of transportation was slow and due to the to the 
# congestion, {name} was late to participate in the {event} and thus was forced
# to {punishment} as punishment."
print("Sadly, because this mode of transportation was slow and due ", end="")
print("to the congestion,", name, "was late to participate in the ", end="")
print(event, "and thus had to", punishment, "as punishment.")
print()

# "What a long {adjective} day it was for {name}."
print("What a long", adjective, "day it was for", name + ".\n")

print("The end.")
