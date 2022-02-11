import datetime
import random
import time
import json


def chatbot():
    response = "yes"
    while response == "yes":
        question = input("What's that your question sef?\n").split()
        a = open("/home/catalyst/Documents/dictionary.json")
        dictionary = json.load(a)
        reply = []          

        question = [x.lower() for x in question]

        if ["exit"] == question:
            print("Exiting...")
        break

    for key in question:
        if key in dictionary.keys():
            reply.append(random.choice(dictionary[key]))

        if reply:
         print(random.choice(reply))
        else:
         print("Ogbeni, don't stress me.... Ask better question biko!")

    time.sleep(1)
    print()

    response = input("Do you want to chat more? (yes or no)\n").lower()
    if response == 'no':
        print("Bye!")

chatbot()

