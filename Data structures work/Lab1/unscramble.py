from Lab1 import *
from random import randint

def main():
    file = open("words_list.txt","r")
    words = file.readlines()
    word = words[randint(0,len(words))][0:-1]
    prompt = "Unscramble the word:"
    scrambled = scramble_word(word)
    for letter in scrambled:
    	prompt += " " + letter
    print(prompt)
    winner = False
    for trynum in range(3):
        userAns = input("Try #"+str(trynum+1)+ " ")
        if userAns == word:
            winner = True
            break
    if winner:
        print("Yay you got it!")
    else:
        print("Too bad, maybe next time, the answer was "+ word)

if __name__ == "__main__":
    main()
