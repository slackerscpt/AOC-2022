
def readData():
    with open('input.txt', "r") as read_file:
        inputData = [line.rstrip() for line in read_file]

        return inputData

def priorityOf(c):
    if c.islower():
        return ord(c) - ord("a") + 1
    else:
        return ord(c) - ord("A") + 27

values = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
}

def part1():
    data = readData()
    total = 0
    for lines in data:
        side1 = lines[:len(lines)//2]
        side2 = lines[len(lines)//2:]
        com_str = ''. join(set(side1). intersection(side2))
        value = values[com_str.lower()]
        if com_str != com_str.lower():
            value = value + 26
        total += value  
        
    print(total)

def part2():
    data = readData()
    print (type(data))
    i = 0
    accumulator = 0
    while i < len(data):
        group = data[i: i + 3]
        commonItem = next(iter(set(group[0]).intersection(set(group[1])).intersection(set(group[2]))))
        accumulator += priorityOf(commonItem)
        i += 3

    print("Day 3 Part 2 = ", accumulator)

part1()
part2()
#Need to rework part 2