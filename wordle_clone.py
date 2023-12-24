
import requests
from rich import print
from rich.highlighter import Highlighter

print("Starting... \n")
library = requests.get("https://random-word-api.herokuapp.com/word?length=5&number=71081")
libList = library.json()

def validWord(user_word):
    if user_word in libList:
        return 1
    else:
        return 0

def isWord(user_word,word,temp_list):
    list = temp_list.copy()

    for i in range(len(user_word)):
        if user_word[i] == word[i] and list[user_word[i]] >= 1:
            # letter present in same position green
            print("[on green]"+ user_word[i] +"[/]",end =" ")
            list[user_word[i]] -= 1
        elif user_word[i] in word and list[user_word[i]] >= 1:
            # letter present in word yellow
                print("[on yellow]"+ user_word[i] +"[/]",end=" ")
                list[user_word[i]] -= 1
        else:
            # letter is not present  or there is no more duplicates black
            print("[bold white on grey23]"+ user_word[i] +"[/]",end=" ")

    #if word present return true else return false
    if user_word == word:
        return 1
    else:
        return 0
    

response = requests.get("https://random-word-api.herokuapp.com/word?length=5")
random_word = response.json()[0]

# keeps track number of each character
char_count = {}
for char in random_word:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1

if (response.status_code != 200):
    print("Sorry, there is an issue with the game. Please try again another time.")
else:
    print("Welcome to Py-Wordle")
    print("Please type in your 5-letter word guesses...")
    i = 0
    endMessage = {1:"Marvellous Guess",2:"Excellent Job",3:"Very Good",4:"Nice Work",5:"Good Guesses",6:"That Was A Close One"}
    while i<6:
        user_word=input("\nGuess " + str(i+1) + ": ").lower()
        if (len(user_word)==5 and user_word.isalpha() and validWord(user_word)):
            i += 1
            if isWord(user_word, random_word, char_count):
                    print("\n",endMessage[i])
                    break
            else:
                continue
        else:
            print("Please enter a valid 5-letter word.")
    else:
        print("\nGame Over! The correct word is: ", random_word)