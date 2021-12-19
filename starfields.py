import requests
import random
import time
from discord_webhook import DiscordWebhook

url='your-discord-webhook-here'

def spacename():
    Type = ["Nebula", "Galaxy", "Cluster", "Cloud", "Solar System", "Quasar", "Void"]
    Size = ["Exa", "Zetta", "Giga", "Mega", "Micro", "Nano", "Pico", ""]
    Name = ["Aphrodite", "Apollo", "Ares", "Artemis", "Athena", "Demeter", "Dionysus", "Hades", "Hephaestus", "Hera", "Hermes", "Hestia", "Poseidon", "Zeus", "Aether", "Aion", "Chronos", "Erebus", "Eros", "Gaia", "Nyx", "Phanes", "Nesoi", "Tartarus", "Thalassa", "Thanatos", "Ourea", "Pontus"]
    Task = ["Adjusting aperature...", "Scanning the cosmos...", "Starting new exposure...", "Calibrating lenses...", "Capturing more photons...", "Looking for new systems..."]
    Verb = ["Found", "Discovered", "Located", "Uncovered", "Revealed", "Spotted"]

    space_name = random.choice(Verb) + " " + random.choice(Name) + " " + random.choice(Size) + " " + random.choice(Type) + ". " + random.choice(Task)

    return space_name

def space():
    seed = random.randint(0, 999999999999999999)
    random.seed(str(seed))

    stars = {':sunny:':1, ':white_flower:':1, ':eight_pointed_black_star:':1, ':no_mouth:':1, ':heart_on_fire:':1, ':rosette:':1, ':cookie:':1, ':shallow_pan_of_food:':1, ':globe_with_meridians:':1, ':radio_button:':1, ':small_blue_diamond:':1, ':small_orange_diamond:':1, ':black_circle:':1, ':infinity:':0.5, ':rocket:':1, ':full_moon:':2, ':full_moon_with_face:':1, ':sun_with_face:':1, ':flying_disc:':1, ':alien:':0.5, ':flying_saucer:':1, ':satellite_orbital:':1, ':cyclone:':1, ':high_brightness:':1, ':low_brightness:':1, ':earth_americas:':2, ':earth_africa:':2, ':earth_asia:':2, ':crescent_moon:':2, ':sparkles:':2, ':star:':2, ':star2:':2, ':dizzy:':2, ':boom:':2, ':ringed_planet:':2, ':blue_circle:':2, ':green_circle:':2, ':purple_circle:':2, ':comet:':2, '✦':20, '　ﾟ':25, '*':30, '.':35, '\n\n\n\n\n':25, '':80}

    field = ''

    for y in range(6):
        for x in range(6):
            for z, q in stars.items():
                if q >= random.randint(0, 100):
                    field += str(z)
                    if 1975 <= len(field) <=2000:
                        send(spacename())
                        send(field)
                        return

                else:
                    field += str('      ')
                    if 1975 <= len(field) <=2000:
                        send(spacename())
                        send(field)
                        return

        field += str('\n\n\n\n\n')


def send(x):
    webhook = DiscordWebhook(url=url, content=x)
    response = webhook.execute()

while True:
    space()
    time.sleep(3600)
