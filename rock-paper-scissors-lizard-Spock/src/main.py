'''
Created on 2015-05-31

@author: mihai
'''
# Rock-paper-scissors-lizard-Spock

import random

# converts the name to a number
def name_to_number(name):
    if name is "rock":
        return 0
    elif name is "Spock":
        return 1
    elif name is "paper":
        return 2
    elif name is "lizard":
        return 3
    elif name is "scissors":
        return 4
    else:
        return "Input Error"

# converts the number to a name    
def number_to_name(number):
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        return "Input error"    
    
    
    
    
def rpsls(player_choice):
    comp_number =random.randrange(0,5)
    comp_name = number_to_name(comp_number)
    
    player_number = name_to_number(player_choice)
    
    difference = (player_number - comp_number) % 5
     
    if difference == 0:
        outcome = "Player and computer tie!"
    elif difference == 1 or difference == 2:
        outcome = "Player wins!"
    else:
        outcome = "Computer wins"
        

    print ("\nPlayer chooses" , player_choice)
    print ("Computer chooses" , comp_name  )
    print (outcome)

# test your code 
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")



