import pandas as pd 


def setupplayer():


    playername = input("Please provide your name. \n")
    playerfilepath = input("Where did you hide your secret map? \n")
    playermap = pd.read_csv(playerfilepath, delimiter=" ")
    
    return playername, playermap


print("Welcome to Battleships Fellow sailors!")
print("Player 1 setup: ")
p1name, p1map = setupplayer()
print("player 2 setup: ")
p2name, p2map = setupplayer()

p1pieces = p1map.values.sum()
p2pieces = p2map.values.sum()
assert(p1pieces == p2pieces)

inputstr = input(f"Captain {p1name} where do you want to shoot? \n")
column, row = inputstr.split(" ")

row = int(row)

print(p2map[row][column])
