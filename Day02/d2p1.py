def readData():
    with open('input.txt', "r") as read_file:
        inputData = [line.rstrip() for line in read_file]

        return inputData

'''
Appreciative of your help yesterday, one Elf gives you an encrypted strategy guide (your puzzle input) that they say will be sure to help you win. "The first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors. The second column--" Suddenly, the Elf is called away to help with someone's tent.

The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors. Winning every time would be suspicious, so the responses must have been carefully chosen.

The winner of the whole tournament is the player with the highest score. Your total score is the sum of your scores for each round. The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).
'''

'''
This strategy guide predicts and recommends the following:

In the first round, your opponent will choose Rock (A), and you should choose Paper (Y). This ends in a win for you with a score of 8 (2 because you chose Paper + 6 because you won).
In the second round, your opponent will choose Paper (B), and you should choose Rock (X). This ends in a loss for you with a score of 1 (1 + 0).
The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.
In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).
'''

# A / X = Rock
# B / Y = Paper
# C / Z = Scissors
score = {
    "A" : 1,
    "B" : 2,
    "C" : 3,
    "X" : 1,
    "Y" : 2,
    "Z" : 3,
}

def winner(p1,p2):
    if score[p1] == score[p2]:
        return (3 + score[p2])
    elif p1 == "A":
        if p2 == "Y":
            return (6 + score[p2])
        else:
            return (score[p2])
    elif p1 == "B":
        if p2 == "Z":
            return(6 + score[p2])
        else:
            return (score[p2])
    #if p1 == "C":
    else:
        if p2 == "X":
            return (6 + score[p2])
        else:
            return(score[p2])

tableLose = {
    "A": "Z",
    "B": "X",
    "C": "Y"

}
tableWin = {
    "A": "Y",
    "B": "Z",
    "C": "X" 
}

def determineMove(p1,p2):
    '''
    X means you need to lose, 
    Y means you need to end the round in a draw, 
    and Z means you need to win.
    '''
    if p2 == "X":
        play = tableLose[p1]
        return (score[play])
    elif p2 == "Y":
        return( 3 + score[p1])
    else:
        play = tableWin[p1]
        return (6 + score[play])


def round1(data):
    total = 0
    for round in data:
        p1,p2 = round.split(' ')
        roundValue = winner(p1,p2)
        total += roundValue

    print('Part 1: %s' %total)

def part2(data):
    total = 0
    for round in data:
        p1,p2 = round.split(' ')
        roundValue = determineMove(p1,p2)
        total += roundValue

    print('Part 2: %s' %total)

data = readData()
round1(data)
part2(data)