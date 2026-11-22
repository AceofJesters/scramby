import random


running = True
while running:
    options = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
            "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d",
            "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
            "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8",
            "9", "0"]

    iterations = random.randint(9,12)

    yourString = ""
    for i in range(iterations):
        yourString += random.choice(options)

    print(f"Your name is: \n{yourString}\n")

    reroll = input("Do you want to reroll? (y/n)")
    if reroll == "n":
        running = False
        print("Enjoy your new label :3")
    else:
        pass