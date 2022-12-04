def readData():
    with open('input.txt', "r") as read_file:
        inputData = [line.rstrip() for line in read_file]

        return inputData


def numRange(numbers):
    start, finish = numbers.split('-')
    return (int(start), int(finish))

def part1():
    data = readData()
    found = 0
    for lines in data:
        
        elf1, elf2 = lines.split(',')
        elf1Min, elf1Max = numRange(elf1)
        elf2Min, elf2Max = numRange(elf2)

        if elf1Min > elf2Min:
            if elf2Max >= elf1Max:
                found += 1
        elif elf2Min > elf1Min:
            if elf1Max >= elf2Max:
                found += 1
        else:
            found +=1

    print('Part 1 answer: %s' %found)

def part2():
    data = readData()
    found = 0
    for lines in data:  
        elf1, elf2 = lines.split(',')
        elf1Min, elf1Max = numRange(elf1)
        elf2Min, elf2Max = numRange(elf2)

        if elf1Min <= elf2Min <= elf1Max:
            found += 1
        elif elf2Min <= elf1Min <= elf2Max:
            found += 1
        
    

    print('Part 2 answer: %s' %found)


part1()
part2()

