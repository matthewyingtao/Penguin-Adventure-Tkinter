from tkinter import *
from tkinter.scrolledtext import *
from tkinter import ttk
import random
import sys

root = Tk()
# root.iconbitmap(default="Penguin.ico")
root.wm_title("Penguin Adventure")


# manages invalid inputs
def invalid_input():
    gstate.consecutive_invalid += 1
    if gstate.consecutive_invalid < 3:
        textBox.insert(END, "please enter a valid input\n")
    else:
        gstate.exit = input("do you want to exit the game? \n"
                            "-1- yes \n"
                            "-2- no \n")
        if gstate.exit in ("1", ""):
            gstate.play = 0
            sys.exit()
        else:
            gstate.consecutive_invalid = 0


class StringInformation:
    def __init__(self):
        self.color_string = ""
        self.colors = ["Blue", "Red", "Yellow", "Green"]
        self.emoji_assets = ["🗿 ", "🌵 ", "💦 ", "🌴 ", "🐧 ", "💰 ", "🐕", "🦂 ", "👽 ", "🦀 ", "🐠 ", "🔥  ", "🐦 ",
                             "📚 ", "🍏 ",
                             "🏠 ", "🏎️ ", "🍔 ", "🍹 ", "🛸 ", "🐾 ", "🧘 ", "⛑ "]
        self.map_state = ["█", "█", "█", "█", "█", "█", "█", "█", "█", "█", "█", "█", "█", "█", "█", "█", "█", "█", "█",
                          "█", "█", "█", "█", "█", "█"]
        self.area_string = ["{} is in a musty dungeon", "{} is in a sandy desert", "{} is in the Pacific Ocean",
                            "{} is in a jungle \nThe jungle is on fire! run away!"]

        self.penguin_facts = ["Penguins are birds but cannot fly.\n",
                              "Penguins are often black and white, which lets the camouflage into the water and ice\n",
                              "Penguins spend half their life on land and the other half in water\n",
                              "Penguins wings function as flippers\n",
                              "Penguins waddle their feet when they walk\n",
                              "Penguins slide on their bellies across the snow\n",
                              "Almost all penguins live in the southern hemisphere\n",
                              "Most penguins actually live in warmer seas\n",
                              "Penguins eat krill (which look similar to shrimp)\n",
                              "Penguins are fast swimmers, and can outswim a lot of their predators\n",
                              "Penguins can swim at speeds of over 20 miles per hour\n"]
        self.questions = [
            "first question: what category are dogs? \n-1- carnivore \n-2- omnivore \n-3- herbivore\n-4- trucknivore",
            "second question: how many paw pads do dogs have? \n-1- \"4\" \n-2- \"16\" \n-3- \"28\" \n-4- \"10\"",
            "third question: how long does a dog sleep in a day? \n-1- 8-10 hours \n-2- 10-12 hours \n-3- 12-14 hours \n-4- 14-16 hours",
            "fourth question: how many muscles do dogs have for moving their ears? \n-1- \"4\" \n-2- \"7\" \n-3- \"24\" \n-4- \"18\"",
            "last question: how many dogs are there in the world? \n-1- 300 million \n-2- 900 million \n-3- 1 billion \n-4- 10 million",
            "first question: what meat has the most protein? \n-1- chicken \n-2- beef \n-3- lamb \n-4- pig",
            "second question: how much sugar is in a can of coke? \n-1- 13 grams\n-2- 25 grams \n-3- 39 grams \n-4- 42 grams",
            "third question: what color is an unripe lemon? \n-1- yellow \n-2- green \n-3- orange \n-4- grey",
            "fourth question: what fruit contains the most sugar? (all weighing the same) \n-1- bananas \n-2- cherries \n-3- mangos \n-4- grapes",
            "last question: how long can a human live without water? \n-1- 3 days \n-2- 1 week \n-3- 5 days \n-4- 1 month"]

    # asks the user for their color, which will be used in place of their name.
    def ask_color_1(self):
        iinfo.user_input = 0
        textBox.insert(END, "--PENGUIN CLUB 97-- \n"
                            "As I'm colorblind, I can't see the color of your feathers.\n"
                            "What color are you?\n")
        textBox.insert(END, "-1- Blue       -2- Red \n -3- Yellow    -4- Green \n")
        gstate.state = 1

    def ask_color_2(self):
        self.color_string = self.colors[iinfo.user_input - 1]
        textBox.insert(END,
                       "That's a unique color for a penguin! I'll call you {} from now on.\n".format(self.color_string))
        iinfo.user_input = 0
        gstate.consecutive_invalid = 0
        gstate.state = 2
        mcreate.create_map()


class IntInformation:
    def __init__(self):
        self.expected_inputs = [1, 2, 3, 4]
        self.answers = [2, 3, 3, 4, 2, 1, 3, 2, 4, 1]
        self.user_input = 0


class GameState:
    def __init__(self):
        self.event = 0
        self.consecutive_invalid = 0
        self.state = 0
        self.button_input_1 = ttk.Button(root, text="Blue", command=input_1)
        self.button_input_2 = ttk.Button(root, text="Red", command=input_2)
        self.button_input_3 = ttk.Button(root, text="Yellow", command=input_3)
        self.button_input_4 = ttk.Button(root, text="Green", command=input_4)

    # Displays the current map
    def show_map(self):
        if self.event == 0:
            map_text.insert(END, "\n{}{}{}{}{} \n"
                                 "{}{}{}{}{} \n"
                                 "{}{}{}{}{} \n"
                                 "{}{}{}{}{} \n"
                                 "{}{}{}{}{} \n \n".format(*sinfo.map_state))
            map_text.yview(END)

    # Checks if the penguin is occupying an event space
    def event_check(self):
        quiz.question_number = mcreate.area * 5
        if mcreate.area == 0:
            if pos.penguin_position == pos.event1_location:
                self.event = 1
                self.state = 4
                self.button_input_3.config(state=DISABLED)
                self.button_input_4.config(state=DISABLED)
                b_place_2_option()
                textBox.insert(END, "{} has found big money! Do you want to: \n".format(sinfo.color_string) +
                               "-1- Take it for yourself \n"
                               "-2- Donate it to charity \n")
            elif pos.penguin_position == pos.event2_location:
                self.event = 1
                self.state = 5
                textBox.insert(END, "The golden dog greets {} \n".format(sinfo.color_string) +
                               "\"Hello fellow animal! I assume you want to leave this dungeon, I can help you, if you answer at least 3 of my 5 dog questions correctly\"\n")
                quiz.start_quiz()
        elif mcreate.area == 1:
            if pos.penguin_position == pos.event1_location:
                self.event = 1
                self.state = 6
                textBox.insert(END, "The scorpion croaks to {} \n".format(sinfo.color_string) +
                               "\"Brttt brtt me give sustenance, if you answer 3 of my 5 food and drink questions correctly\"\n")
                quiz.start_quiz()
            elif pos.penguin_position == pos.event2_location:
                self.event = 1
                self.state = 7
                self.button_input_3.config(state=DISABLED)
                self.button_input_4.config(state=DISABLED)
                gstate.state = 7
                b_place_2_option()
                textBox.insert(END, "{} has found Bob le Alien francais! Tu veux: \n".format(sinfo.color_string) +
                               "-1- Ask to board his cool UFO \n"
                               "-2- Escort him to Area 51 \n")
        elif mcreate.area == 2:
            if pos.penguin_position == pos.fish_location[0]:
                textBox.insert(END, "{} has collected a fish\n".format(sinfo.color_string))
                mcreate.fish_collected += 1
                pos.fish_location[0] = -1
            elif pos.penguin_position == pos.fish_location[1]:
                textBox.insert(END, "{} has collected a fish\n".format(sinfo.color_string))
                mcreate.fish_collected += 1
                pos.fish_location[1] = -1
            elif pos.penguin_position == pos.fish_location[2]:
                textBox.insert(END, "{} has collected a fish\n".format(sinfo.color_string))
                mcreate.fish_collected += 1
                pos.fish_location[2] = -1
            if mcreate.fish_collected == 3:
                self.event = 1
                textBox.insert(END, "{} swims home and feed your family \n".format(sinfo.color_string) +
                               sinfo.emoji_assets[4] + sinfo.emoji_assets[15] + (3 * sinfo.emoji_assets[4]) + "\n"
                                                                                                              "    ~THE END~    ")
                finish_game()
            if pos.penguin_position == pos.crab_location:
                textBox.insert(END, "'I am the Crab of Wisdom!' \n"
                                    "'To prove it, I will tell you three facts about your kind'\n")
                fact1 = random.randint(0, 10)
                fact2 = random.randint(0, 10)
                while fact2 == fact1:
                    fact2 = random.randint(0, 10)
                    if fact2 != fact1:
                        break
                fact3 = random.randint(0, 10)
                while fact3 in {fact1, fact2}:
                    fact3 = random.randint(0, 10)
                    if fact3 not in {fact1, fact2}:
                        break
                textBox.insert(END, sinfo.penguin_facts[fact1])
                textBox.insert(END, sinfo.penguin_facts[fact2])
                textBox.insert(END, sinfo.penguin_facts[fact3])
                pos.apple_location = random.randint(0, 24)
                while pos.apple_location in pos.occupied:
                    pos.apple_location = random.randint(0, 24)
                    if pos.apple_location not in pos.occupied:
                        break
                pos.crab_location = 30
                sinfo.map_state[pos.apple_location] = sinfo.emoji_assets[14]
                gstate.show_map()
                textBox.insert(END, "okay, you get the point. Now I'll tell you about the Apple of Wisdom. \n"
                                    "*the Apple of Wisdom has appeared on the map*\n")
            if pos.penguin_position == pos.apple_location:
                self.event = 1
                textBox.insert(END, "{} has found the Apple of Wisdom \n".format(sinfo.color_string) +
                               "{} eats the apple and transcend the universe, {} has infinite knowledge and wisdom, {} has ascended.".format(
                                   sinfo.color_string, sinfo.color_string, sinfo.color_string) + sinfo.emoji_assets[
                                   21] +
                               sinfo.emoji_assets[4] +
                               sinfo.emoji_assets[
                                   21] + "\n"
                                         "    ~THE END~    ")
                finish_game()
        elif mcreate.area == 3:
            if pos.penguin_position == pos.parrot_location:
                self.event = 1
                textBox.insert(END, "'ey ey it's me, parrot' \n"
                                    "Hop on my back, I can fly you out of here!\n")
                textBox.insert(END,
                               "The parrot flies {} out of the rainforest unhurt and takes {} back to his family in antarctica.\n".format(
                                   sinfo.color_string, sinfo.color_string) + "\n" + sinfo.emoji_assets[
                                   mcreate.event_emoji + 1] + "\n" +
                               sinfo.emoji_assets[4] + sinfo.emoji_assets[15] + "\n"
                                                                                "    ~THE END~    ")
                finish_game()
            if pos.penguin_position > 19:
                self.event = 1
                textBox.insert(END, "{} runs away from the fire and meets a firefighter \n".format(sinfo.color_string) +
                               "He takes {} under his WING and {} becomes a firefighter \n".format(sinfo.color_string,
                                                                                                   sinfo.color_string) +
                               sinfo.emoji_assets[22] + "\n" +
                               sinfo.emoji_assets[4] + "\n"
                                                       "The forest is saved!")
                textBox.insert(END, "    ~THE END~    ")
                finish_game()
        if pos.penguin_position == pos.book_location:
            fact = random.randint(0, 10)
            textBox.insert(END, sinfo.penguin_facts[fact])

    def start_game(self):
        input_1()
        button_start.place_forget()
        self.button_input_1.place(relheight=0.05, relwidth=0.1, relx=0.65, rely=0.65)
        self.button_input_2.place(relheight=0.05, relwidth=0.1, relx=0.85, rely=0.65)
        self.button_input_3.place(relheight=0.05, relwidth=0.1, relx=0.65, rely=0.8)
        self.button_input_4.place(relheight=0.05, relwidth=0.1, relx=0.85, rely=0.8)


class MapCreation:
    def __init__(self):
        self.fish_create = 0
        self.fire_stage = 0
        self.fish_collected = 0
        self.map_making = 0
        self.area = 0
        self.event_emoji = 0

    # Random number to choose map
    def area_setup(self):
        self.area = random.randint(0, 3)
        self.event_emoji = self.area * 2 + 5

    # replaces the tiles in the map into the area tiles
    def make_map(self):
        while self.map_making < 25:
            sinfo.map_state[self.map_making] = sinfo.emoji_assets[self.area]
            self.map_making += 1
        sinfo.map_state[12] = sinfo.emoji_assets[4]

    # places the events on the map
    def make_events_01(self):
        pos.event1_location = random.randint(0, 24)
        while pos.event1_location in pos.occupied:
            pos.event1_location = random.randint(0, 24)
            if pos.event1_location not in pos.occupied:
                break
        pos.occupied[1] = pos.event1_location
        pos.event2_location = random.randint(0, 24)
        while pos.event2_location in pos.occupied:
            pos.event2_location = random.randint(0, 24)
            if pos.event2_location not in pos.occupied:
                break
        pos.occupied[2] = pos.event2_location
        pos.book_location = random.randint(0, 24)
        while pos.book_location in pos.occupied:
            pos.book_location = random.randint(0, 24)
            if pos.book_location not in pos.occupied:
                break
        pos.occupied[3] = pos.book_location
        sinfo.map_state[pos.event1_location] = sinfo.emoji_assets[self.event_emoji]
        sinfo.map_state[pos.event2_location] = sinfo.emoji_assets[self.event_emoji + 1]
        sinfo.map_state[pos.book_location] = sinfo.emoji_assets[13]

    def make_events_2(self):
        while self.fish_create != 3:
            pos.fish_location[self.fish_create] = random.randint(0, 24)
            while pos.fish_location[self.fish_create] in pos.occupied:
                pos.fish_location[self.fish_create] = random.randint(0, 24)
                if pos.fish_location[self.fish_create] not in pos.occupied:
                    self.fish_create += 1
                    break
        pos.occupied[1] = pos.fish_location[0]
        pos.occupied[2] = pos.fish_location[1]
        pos.occupied[3] = pos.fish_location[2]
        pos.crab_location = random.randint(0, 24)
        while pos.crab_location in pos.occupied:
            pos.crab_location = random.randint(0, 24)
            if pos.crab_location not in pos.occupied:
                break
        pos.occupied[4] = pos.crab_location
        pos.book_location = random.randint(0, 24)
        while pos.book_location in pos.occupied:
            pos.book_location = random.randint(0, 24)
            if pos.book_location not in pos.occupied:
                break
        pos.occupied[5] = pos.book_location
        sinfo.map_state[pos.crab_location] = sinfo.emoji_assets[self.event_emoji]
        sinfo.map_state[pos.fish_location[0]] = sinfo.emoji_assets[self.event_emoji + 1]
        sinfo.map_state[pos.fish_location[1]] = sinfo.emoji_assets[self.event_emoji + 1]
        sinfo.map_state[pos.fish_location[2]] = sinfo.emoji_assets[self.event_emoji + 1]
        sinfo.map_state[pos.book_location] = sinfo.emoji_assets[13]

    def make_events_3(self):
        pos.parrot_location = random.randint(10, 19)
        while pos.parrot_location in pos.occupied:
            pos.parrot_location = random.randint(10, 19)
            if pos.parrot_location not in pos.occupied:
                break
        pos.occupied[1] = pos.parrot_location
        pos.book_location = random.randint(10, 19)
        while pos.book_location in pos.occupied:
            pos.book_location = random.randint(10, 19)
            if pos.book_location not in pos.occupied:
                break
        pos.occupied[1] = pos.book_location
        sinfo.map_state[pos.parrot_location] = sinfo.emoji_assets[self.event_emoji + 1]
        sinfo.map_state[pos.book_location] = sinfo.emoji_assets[13]
        sinfo.map_state[0] = sinfo.emoji_assets[self.event_emoji]
        sinfo.map_state[1] = sinfo.emoji_assets[self.event_emoji]
        sinfo.map_state[2] = sinfo.emoji_assets[self.event_emoji]
        sinfo.map_state[3] = sinfo.emoji_assets[self.event_emoji]
        sinfo.map_state[4] = sinfo.emoji_assets[self.event_emoji]

    def create_map(self):
        self.area_setup()
        textBox.insert(END, sinfo.area_string[self.area].format(sinfo.color_string))
        self.make_map()
        if self.area < 2:
            self.make_events_01()
        elif self.area == 2:
            self.make_events_2()
        elif self.area == 3:
            self.make_events_3()
        gstate.show_map()
        textBox.insert(END, "\nWhich way would you like to go? \n"
                            "-1- north ▲       -2- south ▼ \n"
                            "-3- east ▶        -4- west ◀ \n")
        gstate.state = 3


class Positions:
    def __init__(self):
        self.penguin_position = 12
        self.book_location = -1
        self.occupied = [12, -1, -1, -1, -1, -1, -1]
        self.north_boundary = [0, 1, 2, 3, 4]
        self.south_boundary = [20, 21, 22, 23, 24]
        self.east_boundary = [4, 9, 14, 19, 24]
        self.west_boundary = [0, 5, 10, 15, 20]

        self.event1_location = -1
        self.event2_location = -1

        self.apple_location = -1
        self.fish_location = [-1, -1, -1]
        self.crab_location = -1

        self.parrot_location = -1

    # moves the penguin on the map
    def move_map(self):
        if iinfo.user_input == 1:
            sinfo.map_state[self.penguin_position - 5] = sinfo.emoji_assets[4]
            sinfo.map_state[self.penguin_position] = sinfo.emoji_assets[mcreate.area]
            self.penguin_position -= 5
        elif iinfo.user_input == 2:
            sinfo.map_state[self.penguin_position + 5] = sinfo.emoji_assets[4]
            sinfo.map_state[self.penguin_position] = sinfo.emoji_assets[mcreate.area]
            self.penguin_position += 5
        elif iinfo.user_input == 3:
            sinfo.map_state[self.penguin_position + 1] = sinfo.emoji_assets[4]
            sinfo.map_state[self.penguin_position] = sinfo.emoji_assets[mcreate.area]
            self.penguin_position += 1
        elif iinfo.user_input == 4:
            sinfo.map_state[self.penguin_position - 1] = sinfo.emoji_assets[4]
            sinfo.map_state[self.penguin_position] = sinfo.emoji_assets[mcreate.area]
            self.penguin_position -= 1
        if mcreate.area == 3:
            if self.penguin_position > mcreate.fire_stage * 5 + 9:
                sinfo.map_state[mcreate.fire_stage * 5 + 5] = sinfo.emoji_assets[mcreate.event_emoji]
                sinfo.map_state[mcreate.fire_stage * 5 + 6] = sinfo.emoji_assets[mcreate.event_emoji]
                sinfo.map_state[mcreate.fire_stage * 5 + 7] = sinfo.emoji_assets[mcreate.event_emoji]
                sinfo.map_state[mcreate.fire_stage * 5 + 8] = sinfo.emoji_assets[mcreate.event_emoji]
                sinfo.map_state[mcreate.fire_stage * 5 + 9] = sinfo.emoji_assets[mcreate.event_emoji]
                mcreate.fire_stage += 1

    # Checks for area boundaries
    def move_check(self):
        while True:
            if iinfo.user_input == 1:
                if pos.penguin_position in pos.north_boundary:
                    textBox.insert(END, "you cannot move there\n")
                    gstate.show_map()
                    break
                if mcreate.area == 3:
                    if sinfo.map_state[pos.penguin_position - 5] == sinfo.emoji_assets[11]:
                        textBox.insert(END, "Don't walk into the fire!\n")
                        gstate.show_map()
                        break
            elif iinfo.user_input == 2:
                if pos.penguin_position in pos.south_boundary:
                    textBox.insert(END, "you cannot move there\n")
                    gstate.show_map()
                    break
            elif iinfo.user_input == 3:
                if pos.penguin_position in pos.east_boundary:
                    textBox.insert(END, "you cannot move there\n")
                    gstate.show_map()
                    break
            elif iinfo.user_input == 4:
                if pos.penguin_position in pos.west_boundary:
                    textBox.insert(END, "you cannot move there\n")
                    gstate.show_map()
                    break
            pos.move_map()
            iinfo.user_input = 0
            gstate.show_map()
            gstate.event_check()
            break


class Quiz:
    def __init__(self):
        self.score = 0
        self.answer = 0
        self.lives = 3
        self.answered = 0
        self.question_number = 0

    def wrong_answer(self):
        self.lives -= 1
        if self.lives < 1:
            gstate.event = 1
            if mcreate.area == 0:
                textBox.insert(END, "the dog starts to growl at {}, and {} runs away \n".format(sinfo.color_string,
                                                                                                sinfo.color_string) +
                               "    ~THE END~    ")
                finish_game()
            elif mcreate.area == 1:
                textBox.insert(END, "He leaves and {} starve/thirst in the desert \n".format(sinfo.color_string) +
                               "    ~THE END~    ")
                finish_game()
            sys.exit()
        else:
            textBox.insert(END, "Wrong answer! You have {} lives remaining\n.".format(self.lives))

    # Does the quizzes
    def start_quiz(self):
        b_place_4_option()
        if self.answered != 5:
            textBox.insert(END, "\n" + sinfo.questions[self.question_number] + "\n")
        else:
            textBox.insert(END, "{} scored {} out of 5!".format(sinfo.color_string, quiz.score))
            if mcreate.area == 0:
                textBox.insert(END, "'alright, as promised, I'll get you out of this dungeon, hop onto my back!' \n"
                                    "*{} hops onto the dog, gripping his fur as tight as your flippers will allow* \n".format(
                    sinfo.color_string) +
                               "*The golden dog bolts {} out of the dungeon safely*".format(sinfo.color_string))
                textBox.insert(END, "{} live a fulfilling life outside of the dungeon \n".format(sinfo.color_string) +
                               "    ~THE END~    ")
                finish_game()
            elif mcreate.area == 1:
                textBox.insert(END,
                               "*The scorpion silently crawls into his burrow and brings out a burger and a drink* \n"
                               "'Brtt Brtt'" + sinfo.emoji_assets[mcreate.event_emoji] + sinfo.emoji_assets[17] +
                               sinfo.emoji_assets[18])
                textBox.insert(END, "He gives {} the refreshments and {} walk back home to Antarctica".format(
                    sinfo.color_string,
                    sinfo.color_string) +
                               sinfo.emoji_assets[4] + sinfo.emoji_assets[20] + "\n    ~THE END~    ")
                finish_game()


def game():
    if gstate.state == 0:
        sinfo.ask_color_1()
    elif gstate.state == 1:
        sinfo.ask_color_2()
        b_place_compass()
    elif gstate.state == 3:
        gstate.consecutive_invalid = 0
        pos.move_check()
    elif gstate.state == 4:
        if iinfo.user_input == 1:
            textBox.insert(END, sinfo.color_string + " goes home and buys himself a very nice house and a car \n" +
                           sinfo.emoji_assets[4] + sinfo.emoji_assets[15] + sinfo.emoji_assets[16])
            textBox.insert(END, "    ~THE END~    ")
            finish_game()
        elif iinfo.user_input == 2:
            textBox.insert(END,
                           sinfo.color_string + " goes home and donates the money towards starving Antarctic penguins \n" +
                           sinfo.emoji_assets[4] * 3)
            textBox.insert(END, "    ~THE END~    ")
            finish_game()
    elif gstate.state == 5:
        if iinfo.user_input == (iinfo.answers[quiz.question_number]):
            textBox.insert(END, "Correct!\n")
            quiz.score += 1
            gstate.consecutive_invalid = 0
        else:
            quiz.wrong_answer()
            gstate.consecutive_invalid = 0
        quiz.question_number += 1
        iinfo.user_input = 0
        quiz.answered += 1
        quiz.start_quiz()
    elif gstate.state == 6:
        if iinfo.user_input == (iinfo.answers[quiz.question_number]):
            textBox.insert(END, "Correct!\n")
            quiz.score += 1
            gstate.consecutive_invalid = 0
        else:
            quiz.wrong_answer()
            gstate.consecutive_invalid = 0
        quiz.question_number += 1
        iinfo.user_input = 0
        quiz.answered += 1
        quiz.start_quiz()
    elif gstate.state == 7:
        if iinfo.user_input == 1:
            textBox.insert(END, sinfo.color_string + " and Bob have a very fun time in his UFO with the boys \n"
                           + sinfo.emoji_assets[4] + sinfo.emoji_assets[17] + sinfo.emoji_assets[18] + "     " +
                           sinfo.emoji_assets[
                               8] +
                           sinfo.emoji_assets[18] + sinfo.emoji_assets[17] + "\n" +
                           sinfo.color_string + " and the boys -------->", sinfo.emoji_assets[19])
            textBox.insert(END, "    ~THE END~    ")
            finish_game()
        elif iinfo.user_input == 2:
            textBox.insert(END, "The government gives {} a billion dollars for saving le alien \n".format(
                sinfo.color_string) + sinfo.emoji_assets[4] + (3 * sinfo.emoji_assets[5]) + "\n"
                           + sinfo.emoji_assets[8] + sinfo.emoji_assets[2])
            textBox.insert(END, "    ~THE END~    ")
            finish_game()


def input_1():
    map_text.config(state=NORMAL)
    textBox.config(state=NORMAL)
    iinfo.user_input = 1
    game()
    textBox.yview(END)
    textBox.config(state=DISABLED)
    map_text.config(state=DISABLED)


def input_2():
    map_text.config(state=NORMAL)
    textBox.config(state=NORMAL)
    iinfo.user_input = 2
    game()
    textBox.yview(END)
    textBox.config(state=DISABLED)
    map_text.config(state=DISABLED)


def input_3():
    map_text.config(state=NORMAL)
    textBox.config(state=NORMAL)
    iinfo.user_input = 3
    game()
    textBox.yview(END)
    textBox.config(state=DISABLED)
    map_text.config(state=DISABLED)


def input_4():
    map_text.config(state=NORMAL)
    textBox.config(state=NORMAL)
    iinfo.user_input = 4
    game()
    textBox.yview(END)
    textBox.config(state=DISABLED)
    map_text.config(state=DISABLED)


def finish_game():
    gstate.button_input_1.config(state=DISABLED)
    gstate.button_input_2.config(state=DISABLED)
    gstate.button_input_3.config(state=DISABLED)
    gstate.button_input_4.config(state=DISABLED)


def b_place_compass():
    gstate.button_input_1.configure(text="Up", command=input_1)
    gstate.button_input_1.place_configure(relheight=0.05, relwidth=0.1, relx=0.75, rely=0.65)

    gstate.button_input_2.configure(text="Down", command=input_2)
    gstate.button_input_2.place_configure(relheight=0.05, relwidth=0.1, relx=0.75, rely=0.85)

    gstate.button_input_3.configure(text="Right", command=input_3)
    gstate.button_input_3.place_configure(relheight=0.05, relwidth=0.1, relx=0.88, rely=0.75)

    gstate.button_input_4.configure(text="Left", command=input_4)
    gstate.button_input_4.place_configure(relheight=0.05, relwidth=0.1, relx=0.62, rely=0.75)


def b_place_2_option():
    gstate.button_input_3.place_forget()
    gstate.button_input_4.place_forget()
    gstate.button_input_1.configure(text="1")
    gstate.button_input_1.place_configure(relheight=0.05, relwidth=0.1, relx=0.65, rely=0.725)
    gstate.button_input_2.configure(text="2")
    gstate.button_input_2.place_configure(relheight=0.05, relwidth=0.1, relx=0.85, rely=0.725)


def b_place_4_option():
    gstate.button_input_1.configure(text="1")
    gstate.button_input_2.configure(text="2")
    gstate.button_input_3.configure(text="3")
    gstate.button_input_4.configure(text="4")
    gstate.button_input_1.place_configure(relheight=0.05, relwidth=0.1, relx=0.65, rely=0.65)
    gstate.button_input_2.place_configure(relheight=0.05, relwidth=0.1, relx=0.85, rely=0.65)
    gstate.button_input_3.place_configure(relheight=0.05, relwidth=0.1, relx=0.65, rely=0.8)
    gstate.button_input_4.place_configure(relheight=0.05, relwidth=0.1, relx=0.85, rely=0.8)


sinfo = StringInformation()
iinfo = IntInformation()
gstate = GameState()
mcreate = MapCreation()
pos = Positions()
quiz = Quiz()

# Tkinter Widgets
textBox = ScrolledText(root, font=('Everson Mono', 20), wrap=WORD, state=DISABLED)
textBox.place(relheight=0.98, relwidth=0.60, relx=0.01, rely=0.01)

map_text = Text(root, font=('Everson Mono', 20), wrap=WORD, state=DISABLED)
map_text.place(relheight=0.5, relwidth=0.35, relx=0.62, rely=0.01)

button_start = ttk.Button(root, text="Start Game", command=gstate.start_game)
button_start.place(relheight=0.1, relwidth=0.2, relx=0.7, rely=0.75)

root.geometry("800x800")
root.mainloop()
