import requests
import random
import time
from discord_webhook import DiscordWebhook

url='your-discord-webhook-here'

def spacename():
    Type = ["Nebula", "Galaxy", "Cluster", "Cloud", "System", "Quasar", "Void", "Star"]
    Size = ["Exa", "Zetta", "Giga", "Mega", "Micro", "Nano", "Pico"]
    Name = ["Aphrodite", "Apollo", "Ares", "Artemis", "Athena", "Demeter", "Dionysus", "Hades", "Hephaestus", "Hera", "Hermes", "Hestia", "Poseidon", "Zeus", "Aether", "Aion", "Chronos", "Erebus", "Eros", "Gaia", "Nyx", "Phanes", "Nesoi", "Tartarus", "Thalassa", "Thanatos", "Ourea", "Pontus"]


    space_name = random.choice(Name) + " " + random.choice(Size) + " " + random.choice(Type)

    send(space_name)

def space():
    seed = random.randint(0, 999999999999999999)
    random.seed(str(seed))

    stars = {':sunny:':2, ':rocket:':2, ':full_moon:':2, ':earth_americas:':2, ':ringed_planet:':2, ':comet:':2, '✦':20, '　ﾟ':25, '*':30, '.':35, '':80}

    field = ''

    key = random.choice(list(stars))
    for y in range(6):
        for x in range(6):
            for z, q in stars.items():
                if q >= random.randint(0, 100):
                    field += str(z)
                else:
                    field += str('      ')
        field += str('\n\n\n\n\n')

    #field += '\nSeed: ' + str(seed)

    send(field)
    print(len(field))


def send(x):
    webhook = DiscordWebhook(url=url, content=x)
    response = webhook.execute()


while True:
    spacename()
    space()
    time.sleep(3600)
