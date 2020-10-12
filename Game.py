import random
import argparse

def buildPlayer(numPlayers):
    player={}
    for i in range(1, int(numPlayers)+1):
        player[i] = 0
    return player        

def decision(player):
    p=0
    win=0    
    result = 0
    while win < 100:
        print("Do you want to roll or hold --")
        decision = input("Please enter 'r' or 'h' :")
        currentPlayer = (p % len(player)) + 1
        if decision == 'r':
            roll = random.randint(1,6)
            print("Player "+str(currentPlayer)+" has rolled: "+str(roll))
            if roll == 1:
                result = 0
                p += 1
                print("Next player's turn..")
            else:
                result += roll
        elif decision == 'h':
            player[currentPlayer] += result
            result = 0
            p+=1
            print("Player "+str(currentPlayer)+" Score is :" + str(player[currentPlayer]))
            print("Next player's turn..")

        win = max(player.values())           
    return max(player.items(), key=lambda x : x[1])



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--numPlayers", help='please enter number of players..')
    args = parser.parse_args()

    if args.numPlayers != None:
        player = buildPlayer(args.numPlayers)
        
        againPlay=True
        while againPlay:        
            winner = decision(player)
            print("Winner is Player "+ str(winner[0]))
            print("\nDo you want to play again?")
            play = input("y/n :")
            player = buildPlayer(args.numPlayers)
            if play == 'n':
                againPlay = False
    else:
        print("Please enter valid argument value!")
        parser.exit()
     

if __name__ == "__main__":
    main()
