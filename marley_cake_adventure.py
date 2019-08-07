"""
author: kalez43@github.com
description: This is a text-based game. The goal is to make the best decisions in order to allow Marley (dog) to
retrieve a cake off of the counter without Kayleigh (her human) catching her.
"""


# Space between story strings
def space():
    print("")


def stars():
    space()
    print("* * * * *")
    space()


# Enter function between story telling strings
def enter():
    space()
    x = 0
    while x < 1:
        x += 1
        user_input = input("Click here then press enter ==> ")
        if user_input == "":
            continue
        else:
            break
    space()


def response():
    player_input = input("Type 1 or 2, then press enter ==> ")
    player_input = int(player_input)
    return player_input


def fail():
    stars()
    print("""Marley didn't make it to the cake. Maybe she'll have better luck next time :( """)


def win():
    stars()
    print("""You have met with success! Marley happily munches on her cake with Kayleigh none the wiser. There may be 
hell to pay later, but right now you are in bliss. You are just a dog after all!""")


# List of storyline interludes
story_lines = ["""Kayleigh places the cake on the counter and walks 20 feet away to sit down on the couch. You notice 
that she is facing away from the counter, and is reading a book. You think her attention should be filled for 
now.""", """Now you are sure Kayleigh is engrossed in her book.""", """You hear Kayleigh shift in her seat. Will she 
notice you heading for the cake?""", """Kayleigh continues to talk loudly on the phone."""]
# List of decisions
decisions = ["""You can:
            1. Stand and walk 3 feet towards the counter
            2. Listen for more information""",
             """You can:
            1. Stand and walk 3 feet towards the counter
            2. Whine and see what Kayleigh does""",
             """You can:
            1. Walk 5 feet towards the counter
            2. Listen for more information""",
             """You can:
            1. Walk 5 feet towards the counter
            2. Walk 10 feet towards the counter"""]
# List of correct responses to decisions
true_ans = ["""The sweet smell of the cake beckons you, but you pause to listen before making any moves. 
You notice that you don't hear Kayleigh turning the pages of her book. She must be listening, 
in case you try for the cake! You decide to wait, and after a few moments you hear her turn the 
page.""", """You walk 2 feet towards the counter. Kayleigh is engrossed in her book and doesn't seem to 
notice.""", """You wait for what seems an eternity, but finally you hear Kayleigh stop shifting and start dialing her 
phone. Within moments she is talking loudly with someone on the other end.""", """You take advantage of Kayleigh's
tendency to talk long and loud when she is on the phone, and move 5 feet closer to the counter. You are now only 10 
feet away, and the smell is heavenly!"""]
# list of incorrect responses to decisions
false_ans = ["""Kayleigh hears your nails clicking on the floor. She gets up and admonishes you for moving towards the 
cake. You go back to your bed in shame.""", """You whine. Kayleigh hears you and looks over to the bed saying 
'Poor Marley, what's wrong?' You realize you have made the wrong decision and you have to wait for her to return
to her book.""", """You took a gamble and it didn't pan out. Kayleigh heard you clicking towards the counter while she 
was momentarily distracted from her reading. Alarmed at how close you are to the cake, she puts you outside where you 
sulk on the porch.""", """You make it just over 6 feet before you notice it is suddenly quiet. You look up and see 
Kayleigh frowning over you with her arms crossed. She fixes you with a stare so withering, you would be shaking in your 
boots if you could wear boots. She silently points towards your kennel, and you hang your head and walk into doggie 
jail knowing you won't be out until the cake is far out of reach."""]
# list of correct inputs
condition = [2, 1, 2, 1]

# Intro
space()
print("""Marley's Cake Adventure!""")
space()
print("""You are a dog named Marley. Marley's favorite food is cake. Your human, Kayleigh, has just baked a cake and 
must let it cool. Make the right decisions to successfully retrieve and eat the cake without being caught by 
Kayleigh!""")
stars()
print("""You are in a dog bed directly behind the couch and 18 feet away from the counter. Follow the instructions to 
move along the story and follow the prompts to choose the best answer for each dilemma. Make all the right choices and 
eat some delicious cake!""")
n = 0
for part in story_lines:
    stars()
    print(part)
    enter()
    print(decisions[n])
    space()
    response()
    if response() == condition[n]:
        space()
        print(true_ans[n])
        n += 1
        continue
    else:
        space()
        print(false_ans[n])
        break

if n == len(story_lines):
    stars()
    win()
else:
    stars()
    fail()






