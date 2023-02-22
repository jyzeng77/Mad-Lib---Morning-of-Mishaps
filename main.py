##
# Mad Lib - A MORNING OF MISHAPS
#
# @author Jerry Zeng
# @course ICS3UC
# @date 2023/02/22 - LastModified
##

###*** DEFINITIONS ***#

# Returns proper pronoun for each case.
def pronoun(id, subject):
  if id == "m":
    return ["he", "him", "his"][subject]
  elif id == "f":
    return ["she", "her", "her(s)"][subject]
  else:
    return ["they", "them", "their(s)"][subject]

# Some prompt templates.
pauseMsg = "[PRESS ENTER]"
promptMsg = "Please provide "

#*** INTRODUCTION ***#
print("Welcome to an exciting game of...")
print("MAD LIBS!!!")
print()

input(pauseMsg)
print()

print("The rules of this game are simple: provide the words that I ", end="")
print("ask for and I will generate a very random story for you to read!")
print()

print("Are you ready? Let\'s begin!")
print()

input(pauseMsg)
print()

#*** INPUT ***#
print('Following this message, provide input according to what the ', end='')
print("prompt demands.")
print("————————————————————")

name = input(promptMsg + "your name: ")

# This loop continues looping until the user provides their gender.
while True:
  gender = input(promptMsg+"your gender - male [m], female [f], other [nb]: ")
  if gender not in ["m", "f", "nb"]:
    print("\tERROR: invalid input, please try again.")
  else:
    break
  
celeb = input(promptMsg + "the name of a famous person: ")
month = input(promptMsg + "a month: ")
day = input(promptMsg + "a day [number]: ")
place = input(promptMsg + "a place: ")
action1 = input(promptMsg + "an action verb [past tense]: ")
action2 = input(promptMsg + "an action verb [ending with \"-ing\"]: ")
adjective = input(promptMsg + "an adjective: ")
emergency = input(promptMsg + "an emergency service: ")
food = input(promptMsg + "a food: ")
phone = input(promptMsg + "an object: ")
ride = input(promptMsg + "any moving noun: ")
obstacles = input(promptMsg + "a noun [plural]: ")
animals = input(promptMsg + "an animal [plural]: ")
event = input(promptMsg + "an event (the...): ")
punishment = input(promptMsg + "punishment [verb] (had to...): ")

#*** OUTPUT ***#
print()
print("Generating story.........")
print("DONE.")
print()

input(pauseMsg)
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

input(pauseMsg)
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

input(pauseMsg)
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

input(pauseMsg)
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

input(pauseMsg)
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
