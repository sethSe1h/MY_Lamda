import time, random, sys
current = time.ctime()
print(f"You start in: ({current})")
box1 = []
box2 = []
def game1(word1, word2):
    print("--> Game start...")
    box1.append(word1)
    box2.append(word2)
    while True:
        print("1 Add new by add one or more")
        print("2 Add one")
        print("3 Delete one index")
        print("4 Guess the word in [box1] and [box2]")
        choose = input("Choose your option> ")
        if choose == "1":
            print("--> [1] <--")
            n = int(input("How many to add : "))
            print(f"--> [left : {n}] <--")
            for count in range(n + 1):
                word1 = input("Enter left: ")
                box1.append(word1)
            print(f"--> [right: {n}] <--")
            for count in range(n + 1):
                word2 = input("Enter right: ")
                box2.append(word2)
        elif choose == "2":
            print("--> [2] <--")
            left = input("Enter left: ")
            box1.append(left)
            right = input("Enter right: ")
            box2.append(right)
        elif choose == "3":
            print("--> [3] <--")
            del_box1 = int(input("Enter to index to delete: "))
            box1.remove(del_box1)
            del_box2 = int(input("Enter to index to delete: "))
            box2.remove(del_box2)
        elif choose == "4":
            print("--> [4] <--")
            while True:
                guess = str(input("Enter to guess word: "))
                box_word1 = random.choice(box1)
                box_word2 = random.choice(box2)
                f_c_l = box_word1[0].upper()
                f_c_r = box_word2[0].upper()
                if f_c_l == f_c_r:
                    print("You lose because it has same first character!")
                    break
                elif guess in box_word1 or guess  in box_word2:
                    print("You right guess word.")
                    print(f"the word is {box_word1}, {box_word2}")
                    break
                print("Guess wrong word, try again?")

def game2(text):
    too_ch = set()
    print("Game start...")
    print("\tThis your word ==> ", end ="")
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.4)
    while True:
        try:
            n = int(input("\nEnter index to convert to uppercase (1-based index): "))
            if n < 1 or n > len(text):
                print("Invalid index! Try again.")
                continue

            if text[n - 1].upper() in too_ch:
                print("Already input! You lose!")
                break

            text[n - 1] = text[n - 1].upper()
            too_ch.add(text[n - 1])

            print("Updated word: " + "".join(text))

            if all(char.isupper() for char in text):  # Win condition
                print("Congratulations! You win!")
                break

        except ValueError:
            print("Invalid input! Enter a valid number.")

while True:
    game_set = input("Choose to 1 and 2 to play game? => ")
    if game_set == "1":
        print("===> [Game 1] <====")
        left = input("Enter left: ")
        right = input("Enter right: ")
        game1(left, right)
        break
    elif game_set == "2":
        print("===> [Game 2] <====")
        text = input("Enter text: ")
        game2(list(text))
        break
    else:
        print("Enter again?")

while True:
    you = input("Do you want to revenge this game?[y/n]: ")
    if you == "yes" or you == "no":
        while True:
            game_set = input("Choose to 1 and 2 to play game? => ")
            if game_set == "1":
                print("===> [Game 1] <====")
                left = input("Enter left: ")
                right = input("Enter right: ")
                game1(left, right)
            elif game_set == "2":
                print("===> [Game 2] <====")
                text = input("Enter text: ")
                game2(list(text))
            else:
                print("Enter again?")
    elif you == "no" or you == "n":
        print("Bye Bye :)")
        break
    else:
        print("Oh oh! Error...")