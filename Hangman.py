import random
database=["apricot","delicious","pizza","crocodile","watermelon","elephant","mercedes","playstation"]
word= random.choice(database)
spaces=""
for x in range(0,len(word)):
    spaces+="-"
spaces_list=list(spaces)
word_list=list(word)
print("Let's play Hangman\n I chose a word\nTry to guess it 👇")
print(f'\t\t\t\t{spaces}')
live=5
while live > 0:
    if spaces == word:
        print("You Win")
        break
    letter = str(input("Guess a letter: ")).lower()
    if letter not in word:
        print(spaces)
        live -= 1
        if live == 0:
            print("You Lost")
            print(
                         _______
                         |/      |
                         |      (_)
                         |      \|/
                         |       |
                         |      / |
                         |
                         |___
                        )
        elif live == 4:
            print(
                         Wrong!
                        |/      |
                         |      (_)
                         |
                         |
                         |___
                        )
        elif live == 3:

            print(
                        Wrong!
                         _______
                         |/      |
                         |      (_)
                         |      \|
                         |
                         |
                         |
                         |___
                        )
        elif live == 2:
            print(
                        Wrong!
                         _______
                         |/      |
                         |      (_)
                         |      \|/
                         |
                         |
                         |
                         |___
                        )
        elif live == 1:

            print(
                            Wrong!
                             _______
                             |/      |
                             |      (_)
                             |      \|/
                             |       |
                             |      /
                             |
                             |___
                            )



    else:
        print("Right Guess")
        if spaces == word:
            print("You Win")
            break
        for l in range(0,len(word)):
            if letter==word_list[l]:
                spaces_list[l]=letter
        spaces="".join(spaces_list)
        print(spaces)
