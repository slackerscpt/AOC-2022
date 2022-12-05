def readData():
    with open('input.txt', "r") as read_file:
        inputData = [line.rstrip() for line in read_file]

        return inputData

'''
        [Q] [B]         [H]        
    [F] [W] [D] [Q]     [S]        
    [D] [C] [N] [S] [G] [F]        
    [R] [D] [L] [C] [N] [Q]     [R]
[V] [W] [L] [M] [P] [S] [M]     [M]
[J] [B] [F] [P] [B] [B] [P] [F] [F]
[B] [V] [G] [J] [N] [D] [B] [L] [V]
[D] [P] [R] [W] [H] [R] [Z] [W] [S]
 1   2   3   4   5   6   7   8   9 

'''

stacks = {
    1: [ 'V', 'J', 'B', 'D' ],
    2: [ 'F', 'D', 'R', 'W', 'B', 'V', 'P' ],
    3: [ 'Q', 'W', 'C', 'D', 'L', 'F', 'G', 'R'],
    4: [ 'B', 'D', 'N', 'L', 'M', 'P', 'J', 'W'],
    5: [ 'Q', 'S', 'C', 'P', 'B', 'N', 'H'],
    6: [ 'G', 'N', 'S', 'B', 'D', 'R'],
    7: [ 'H', 'S', 'F', 'Q', 'M', 'P', 'B', 'Z'],
    8: [ 'F', 'L', 'W'],
    9: [ 'R', 'M', 'F', 'V', 'S' ],
}

def part1():
    instructions = readData()
    lineCounter = 0
    for instruction in instructions:
        (null, number, null, stackFrom, null, stackTo) = instruction.split(' ')
        counter = 0
        while (counter < int(number)):
            oldNumber = stacks[int(stackFrom)].pop(0)
            stacks[int(stackTo)].insert(0, oldNumber)
            counter += 1
        #print (stacks)
        print (lineCounter)
        lineCounter +=1
    print ('Done')
    for k, v in stacks.items():
        print(k, v[0])

def part2():
    instructions = readData()
    lineCounter = 0
    for instruction in instructions:
        (null, number, null, stackFrom, null, stackTo) = instruction.split(' ')
        counter = int(number)
        while(counter > 0):
            oldNumber = stacks[int(stackFrom)].pop(int(counter)-1)
            stacks[int(stackTo)].insert(0, oldNumber)
            counter -= 1
        print (lineCounter)
        lineCounter +=1
    for k, v in stacks.items():
        print(k, v[0])
#part1()
part2()