import random 

coin = random.choice(["head","tails"]) 
print(coin)
from random import choice

coin = choice(["head","tails"])
print(coin)

import random

cards = ["jack","king","queen"]
random.shuffle(cards) # to shuffle cards
for card in cards:
    print(card)

number = random.randint(1,10) # to get random int between 1 and 10
print(number)

import statistics

print(statistics.mean([100,90,82,52,46,82,92,75,57,23,57,95,79,98,99,75,52,95]))

import sys

print("hello my name is ",sys.argv[1]) # hello my name is  Adii

if len(sys.argv) < 2:
    print("too less argruments")
elif len(sys.argv) > 2:
    print("too many arguments")
else:
    print("hello my name is ",sys.argv[1])

if len(sys.argv) < 2:
    sys.exit("too less argruments")
elif len(sys.argv) > 2:
    sys.exit("too many arguments")

print("hello my name is ",sys.argv[1])


if len(sys.argv) < 2:
    sys.exit("too less argruments")

for arg in sys.argv[1:]:
    print("hello my name is ", arg)


############################################### PACKAGES #########################################################################

import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("hello " + sys.argv[1])
    cowsay.trex("hello " + sys.argv[1])

############################################### API-REQUESTS #########################################################################
import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
print(json.dumps(response.json(),indent = 2))