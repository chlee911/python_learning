import random
choices = ["Rock","Scissor","Paper"]
computer = random.choice(choices)
computer_score = 0
player_score = 0
tie_score = 0
while True:
    player = input("Rock, Scissor or Paper? (If you do not want to play anymore, type 'Enough')").capitalize()
    if player == computer:
        print("It is a tie!")
        tie_score +=1
    elif player == "Rock":
        if computer == "Scissor":
            print("You win!", player, "smashes", computer)
            player_score += 1 
        else: 
            print("You lose!", computer, "covers", player)
            computer_score += 1
    elif player == "Scissor":
        if computer == "Paper":
            print("You win!", player, "cut", computer)
            player_score += 1 
        else: 
            print("You lose!", computer, "smashes", player)
            computer_score += 1
    elif player == "Paper":
        if computer == "Rock":
            print("You win!", player, "covers", computer)
            player_score += 1 
        else: 
            print("You lose!", computer, "cuts", player)
            computer_score += 1
    elif player == "Enough":
        print("Final Scores:")
        print(f"Computer:{computer_score}")
        print(f"Player:{player_score}")
        print("Tie:", tie_score)
        break
    else:
        print("Not a valid keyword. Please check your spelling!")
    computer = random.choice(choices)