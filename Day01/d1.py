def readData():
    with open('input.txt', "r") as read_file:
        inputData = [line.rstrip() for line in read_file]

        return inputData


def determineElf(data):
    elf = 0
    total = 0
    details = {}
    for numbers in data:
        if numbers != '':
            total = total + int(numbers)
        else:
            details[elf] = total
            total = 0
            elf = elf + 1

    max = 0
    for (elf, total) in details.items():
        if elf > 0:
            if total > details[max]:
                max = elf
    #print ('Max: %s' %max )
    print ('Part 1: %s' %details[max])
    return details

def determineTop3(details):
    ranked = []
    for (_, total) in details.items():
        ranked.append(total)

    ranked.sort(reverse=True)
    #print (ranked)
    total = ranked[0] + ranked[1] + ranked[2]
    print ('Part 2: %s' %total)

data = readData()
updatedData = determineElf(data)
determineTop3(updatedData)
#print (updatedData)