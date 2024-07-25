import random
import re

wordlist = []
f = open("wordlist.txt", "r")
for x in f:
    wordlist.append(x.replace("\n", ""))

filtered_words = [word for word in wordlist if re.match(r"\b[a-z]{5}\b", word)]

answer = ''.join(random.choices(filtered_words))

print("Guess the 5 letter word")
chance = 5

while chance > 0:
    guess = input(f"{chance} chances left: ")

    if len(guess) != 5:
        print("This is a 5 letter word game, not more, not less.")
        continue
    
    if guess == answer:
        print("You win")
        break
    else:
        chance -= 1
        if chance == 0:
            print("Game Over")
            print(f"The answer is {answer}")
        else:
            print("Wrong guess, try again")