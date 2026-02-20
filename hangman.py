import random


def mainGame():
    global usedLetters
    usedLetters = []
    global wrongGuesses
    wrongGuesses = 0
    continueGame = True
    endofGame = False
    print("Welcome to Hangman!")
    print("Guess the word before you run out of guesses. You can guess a letter or the whole word at once. Good luck!")
    print()
    global answerWord
    answerWord = chosenWord()

    while continueGame:
        displayWord(wrongGuesses)
        guess = userGuess()
        endofGame = checker(guess, wrongGuesses)
        if endofGame:
            continueGame = False


def chosenWord():
    animals = [
        "lion", "tiger", "zebra", "giraffe", "monkey", "panda", "rabbit", "hamster", "horse", "donkey",
        "camel", "otter", "beaver", "badger", "weasel", "ferret", "walrus", "dolphin", "shark", "whale",
        "octopus", "squid", "crab", "lobster", "shrimp", "eagle", "falcon", "sparrow", "pigeon", "parrot",
        "turkey", "chicken", "rooster", "penguin", "lizard", "gecko", "iguana", "python", "viper", "cobra",
        "frog", "toad", "newt", "salmon", "trout", "carp", "turtle", "leopard", "cheetah", "hyena"
    ]

    food = [
        "apple", "banana", "orange", "grapes", "melon", "mango", "papaya", "peach", "pear", "plum",
        "cherry", "lemon", "lime", "apricot", "avocado", "carrot", "potato", "tomato", "onion", "garlic",
        "pepper", "lettuce", "cabbage", "spinach", "broccoli", "pickle", "burger", "pizza", "pasta", "noodle",
        "rice", "bread", "butter", "cheese", "yogurt", "omelet", "sausage", "bacon", "steak", "chicken",
        "cookie", "biscuit", "donut", "cake", "brownie", "muffin", "cereal", "pancake", "waffle", "honey"
    ]

    countries = [
        "france", "spain", "italy", "germany", "sweden", "norway", "denmark", "poland", "greece", "turkey",
        "canada", "mexico", "brazil", "chile", "peru", "argentina", "egypt", "kenya", "nigeria", "ghana",
        "china", "japan", "korea", "india", "nepal", "thailand", "vietnam", "laos", "qatar", "oman",
        "iran", "iraq", "jordan", "iceland", "ireland", "scotland", "wales", "england", "finland",
        "belgium", "austria", "swiss", "cuba", "haiti", "jamaica", "panama", "sudan", "algeria", "morocco"
    ]

    sports = [
        "soccer", "tennis", "cricket", "rugby", "hockey", "boxing", "karate", "judo", "golf", "skiing",
        "cycling", "rowing", "surfing", "skating", "archery", "fencing", "badminton", "handball", "netball", "softball",
        "baseball", "basketball", "volleyball", "swimming", "diving", "climbing", "running", "walking", "bowling", "snooker",
        "darts", "wrestling", "weightlifting", "triathlon", "marathon", "canoeing", "kayaking", "motocross", "polo", "sailing",
        "fishing", "hunting", "parkour", "gymnastics", "pilates", "yoga", "skateboard", "snowboard", "bobsled", "equestrian"
    ]

    household = [
        "table", "chair", "sofa", "couch", "desk", "lamp", "clock", "mirror", "carpet", "curtain",
        "pillow", "blanket", "mattress", "wardrobe", "drawer", "shelf", "cabinet", "fridge", "freezer", "oven",
        "stove", "toaster", "kettle", "microwave", "sink", "faucet", "shower", "bathtub", "toilet", "brush",
        "broom", "mop", "bucket", "sponge", "towel", "basket", "hanger", "notebook", "remote", "speaker",
        "television", "router", "charger", "battery", "switch", "socket", "door", "window", "handle", "lock"
    ]

    toys = [
        "puzzle", "lego", "doll", "blocks", "marbles", "ball", "frisbee", "kite", "yojo", "top",
        "cards", "domino", "chess", "checkers", "dice", "robot", "train", "rocket", "plane", "drone",
        "truck", "tractor", "helmet", "scooter", "skate", "teddy", "plush", "figure", "spinner", "tablet",
        "console", "joystick", "keyboard", "mouse", "monitor", "screen", "camera", "paint", "crayon", "marker",
        "glue", "scissors", "paper", "coloring", "book", "comic", "sticker", "helmet", "target", "whistle"
    ]

    categories = {
        "animals": animals,
        "food": food,
        "countries": countries,
        "sports": sports,
        "household": household,
        "toys": toys
    }

    while True:
        categoryChoice = input(
            "Choose a category (animals, food, countries, sports, household, toys): ")
        print()
        if categoryChoice.lower() in categories:
            wordList = categories[categoryChoice.lower()]
            break
        else:
            print("Invalid category. Please choose from the given options.")

    return random.choice(wordList)


def userGuess():
    while True:
        guess = input("Guess a letter or a Word: ")
        print()
        if guess in usedLetters:
            print("You have already guessed that letter")
        elif guess.isalpha():
            return guess.lower()
        else:
            print("Invalid input")


def incrementWrongGuesses():
    global wrongGuesses
    wrongGuesses += 1
    return wrongGuesses


def checker(guess, wrongGuesses):
    if len(guess) == 1:
        if guess in answerWord:
            return (correctLetter(guess))

        else:
            incrementWrongGuesses()
            return (wrongLetter(guess, wrongGuesses))

    else:
        if guess == answerWord:
            return (correctWord(guess))

        else:
            incrementWrongGuesses()
            return wrongWord(guess, wrongGuesses)


def displayWord(wrongGuesses):
    hangmanArt = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
    display = ""
    for letter in answerWord:
        if letter in usedLetters:
            display += " " + letter + " "
        else:
            display += " _ "
    print("\nUsed Letters: " + str(usedLetters))
    print(display)
    print()
    print(hangmanArt[wrongGuesses])
    print()


def correctLetter(guess):
    print("\u2705 Correct! The letter " + guess + " is in the word. \u2705")
    print()
    usedLetters.append(guess)
    return False


def wrongLetter(guess, wrongGuesses):
    print("\u274C Wrong! The letter " + guess + " is not in the word. \u274C")
    usedLetters.append(guess)
    print("You have " + str(5 - wrongGuesses) + " guesses left.")
    print()
    if wrongGuesses >= 5:
        loseScreen()
        return True
    else:
        return False


def correctWord(guess):
    print("\u2b50 \u2b50 \u2b50 Congratulations! You guessed the word " + "'" +
          guess + "'" + " correctly! \u2b50 \u2b50 \u2b50")
    print()
    return True


def wrongWord(guess, wrongGuesses):
    print("\u274C Wrong! The word " + guess + " is not correct. \u274C")
    print("You have " + str(5 - wrongGuesses) + " guesses left.")
    if wrongGuesses >= 5:
        loseScreen()
        return True
    else:
        return False


def loseScreen():
    displayWord(wrongGuesses)
    print("\u2620 \u2620 \u2620 Game Over! The correct word was " +
          answerWord + "." + "\u2620 \u2620 \u2620")
    print()


def decider():
    decision = input("Do you want to play again? (yes/no): ")
    while True:
        if decision.lower() == "yes":
            return True
        elif decision.lower() == "no":
            print("Thanks for playing!")
            return False
        else:
            decision = input("Invalid input. Please enter 'yes' or 'no': ")


while True:
    mainGame()
    if not decider():
        break
