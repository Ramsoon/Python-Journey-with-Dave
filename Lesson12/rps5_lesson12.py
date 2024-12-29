import random
import sys
from enum import Enum
def rps():
    game_count = 0
    player_wins = 0
    python_wins = 0
    
    def play_rps():
        nonlocal player_wins
        nonlocal python_wins
        
        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        # This is how to get Enum values
        # print(RPS(2))
        # print(RPS.ROCK)
        # print(RPS['ROCK'])
        # print(RPS.ROCK.value)
        # sys.exit()
        
        playerchoice = input(
            "\nEnter...\n1 for Rock,\n2 for paper, or \n3 for Scissors:\n\n")

        if playerchoice not in ["1","2","3"]:
            print("You must enter 1, 2, or 3.")
            return play_rps()
        player = int(playerchoice)  # cast playerchoice to int
        

        computerchoice = random.choice("123")

        computer = int(computerchoice)

        print("")
        print("You chose " + str(RPS(player)).replace('RPS.', '') + ".")
        print("Python chose " + str(RPS(computer)).replace("RPS.", '') + ".")

        print("")
        def decide_winner(player, computer):
            nonlocal player_wins
            nonlocal python_wins
            if player == 1 and computer == 3:
                player_wins += 1
                return "🥂You win!"
            elif player == 2 and computer == 1:
                player_wins += 1
                return "🥂You win!"
            elif player == 3 and computer == 2:
                player_wins += 1
                return "🥂You win!"
            elif player == computer:
                return "😲Tie game!"
            else:
                python_wins += 1
                return "🐍Python wins!"
        
        game_result = decide_winner(player, computer)
        print(game_result)
        
        nonlocal game_count
        game_count += 1
        
        print("\n Game count: " + str(game_count))
        print("\n Player wins: " + str(player_wins))
        print("\n Python wins: " + str(python_wins))
        print("\Play again?")
        while True:
            playagain = input("\nY for Yes or\nQ to Quit \n\n")
            if playagain.lower() not in ["y","q"]:
                continue
            else:
                break 
        if playagain.lower() == "y":
            return play_rps()
        else:
            print("🎉🎉🎉🎉🙌")
            print("Thank you for playing!\n")
            playagain = False
            sys.exit("Bye 👋")
    return play_rps
 
play = rps()
play()