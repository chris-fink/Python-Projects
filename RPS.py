#!/usr/bin/python3
import random

print("Let's play a game of Rock, Paper, Scissors!")
userChoice = input("Enter your choice (Rock, Paper, Scissors): ")
possibleChoice = ["Rock", "Paper", "Scissors"]
compChoice = random.choice(possibleChoice)
print(f"You chose {userChoice}, the computer chose {compChoice}.")

if userChoice == compChoice:
    print(f"Draw! You both picked {userChoice}.")
elif userChoice == "Rock":
    if compChoice == "Scissors":
        print("Rock smashes Scissors! You win!")
    else:
	      print("Paper covers rock! You lose.")
elif userChoice == "Paper":
    if compChoice == "Rock":
        print("Paper covers Rock! You win!")
    else:
	      print("Scissors cut Paper! You lose.")
elif userChoice == "Scissors":
    if compChoice == "Paper":
        print("Scissors cut Paper! You win!")
    else:
	      print("Rock smashes Scissors! You lose.")   
