##
# Mad Lib - A MORNING OF MISHAPS
#
# @author Jerry Zeng
# @course ICS3UC
# @date YYYY/MM/DD - 2023/02/17
##

###*** DEFINITIONS ***#
import time

# Prints text using typewriter effect.
def typed(string, speed=0.1, ending='\n'):
  for c in string:
    print(c, end='', flush=True)
    time.sleep(speed)
  print(end=ending)

# Gets a value POLITELY for each prompt.
def ask_for(thing):
  result = None
  while True:
    typed(f"Please provide {thing}: ", speed=0.005, ending='')
    result = input()
    if result.strip() == '':
      typed('\tERROR: please provide a valid input.', 0.001)
    else:
      return result.strip()

# Returns proper pronoun for each case.
def pronoun(id, subject):
  if id == 'm':
    return ['he', 'him', 'his'][subject]
  elif id == 'f':
    return ['she', 'her', 'hers'][subject]
  else:
    return ['they', 'them', 'theirs'][subject]

# Prompts user to continue running the program.
def pause():
  input('[PRESS ENTER TO CONTINUE]')

#*** INTRODUCTION ***#
typed('Welcome to an exciting game of...')
typed('MAD LIBS!!!', speed=0.4)
print()

typed('The rules of this game are simple: provide the words that I ask for \
and I will generate a very random story for you to read!', 0.00001)
typed('Are you ready? Let\'s begin!')
print()
pause()

#*** INPUT ***#
print()
typed("Following this message, provide input according to what the \
prompt demands.", 0.005)
print('————————————————————')

name = ask_for('your name')

while True:
  gender = ask_for('your gender - male [m], female [f], other [nb]')
  if gender not in ['m', 'f', 'nb']:
    typed('\tERROR: invalid input, please try again.', 0.001)
  else:
    break
  
celeb = ask_for('the name of a famous person')
month = ask_for('a month')
day = ask_for('a day')
place = ask_for('a place')
action1 = ask_for('an action verb [past tense]')
action2 = ask_for('an action verb [ending with "-ing"]')
adjective = ask_for('an adjective')
emergency = ask_for('an emergency service')
food = ask_for('a food')
phone = ask_for('an object')
ride = ask_for('any moving noun')
obstacles = ask_for('a noun [plural]')
animals = ask_for('an animal [plural]')
event = ask_for('an event (the...)')
punishment = ask_for('punishment [verb] (had to...)')

#*** OUTPUT ***#
print()
typed('Generating story.........')
typed('DONE.')
print()
pause()

print()
typed('\n\n\n\n\nA MORNING OF MISHAPS')
print('————————————————————')
print()
typed(f'The morning of {month} {day}, little {name} was walking to {place}.') 
print()
typed(f'On the way to {place}, {name} saw {celeb} lying on the street. What \
happened to poor {celeb}? It seems that they may have been {action1} in the \
middle of the street. Oh dear!')
print()
typed(f'{name} helps them by {action2} and calling {emergency}, \
before continuing on {pronoun(gender, 2)} way to {place}.')
print()
typed(f'Walking to {place} is quite tiring for {pronoun(gender, 1)}\
. "What should I eat for breakfast," says {name}, who forgot to eat \
breakfast this morning. As {pronoun(gender, 0)} walks into a store, \
{pronoun(gender, 0)} decides on {food}.')
print()
typed(f'Noticing that {pronoun(gender, 0)} is almost late, it \
would be smart for {name} to call using {pronoun(gender, 2)} \
{phone} to hail a ride on a(n) {ride} to {place}.')
print()
typed(f'Due to {obstacles} and {animals} on the road, there was a \
great big traffic jam.')
print()
typed(f'Sadly, because this mode of transportation was slow and due \
to the congestion, {name} was late to participate in the {event} and \
thus forced to {punishment} as punishment.')
print()
typed(f'What a(n) long {adjective} day it was for {name}.')
