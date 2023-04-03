from game_data import *
import random
import os

def generate_string(from_dic):
    output_string = ""
    output_string += from_dic["name"] + ", a "
    output_string += from_dic["description"] + " from "
    output_string += from_dic["country"]
    return output_string

def is_higher(dic1, dic2):
    if int(dic1["follower_count"]) > int(dic2["follower_count"]):
        return True
    else:
        return False

def higher_lower():
    os.system("cls")
    correct_guesses = 0
    guessed_right = True
    print("Welcome to the Higher-Lower game!\nIn this game you will guess which of two things has more followers.\n")
    dictionary_A = random.choice(data)
    while guessed_right:
        if correct_guesses > 0:
            os.system("cls")
            print(f"\nCorrect! You have {correct_guesses} correct guesses in a row!")
        dicitonary_B = random.choice(data)
        while dictionary_A == dicitonary_B:
            dicitonary_B = random.choice(data)
        print("Compare A: " + generate_string(dictionary_A) + "\n")
        print("Versus\n")
        print("Against B: " + generate_string(dicitonary_B))
        user_guess = input("Who do you think has more followers? \'A\' or \'B\': ").lower()
        if user_guess == "a":
            guessed_right = is_higher(dictionary_A,dicitonary_B)
            correct_guesses += 1
        elif user_guess == "b":
            guessed_right = is_higher(dicitonary_B,dictionary_A)
            correct_guesses += 1
        else:
            guessed_right = False
        dictionary_A = dicitonary_B
    os.system("cls")
    print(f"I'm sorry, you've guessed incorrectly. Your total score is: {correct_guesses}")

higher_lower()
        


              



