def readData():
    with open('test.txt', "r") as read_file:
        inputData = [line.rstrip() for line in read_file]

        return inputData


'''
Start by figuring out the signal being sent by the CPU. The CPU has a single register, X, which starts with the value 1. It supports only two instructions:

addx V takes two cycles to complete. After two cycles, the X register is increased by the value V. (V can be negative.)
noop takes one cycle to complete. It has no other effect.

The interesting signal strengths can be determined as follows:

During the 20th cycle, register X has the value 21, so the signal strength is 20 * 21 = 420. (The 20th cycle occurs in the middle of the second addx -1, so the value of register X is the starting value, 1, plus all of the other addx values up to that point: 1 + 15 - 11 + 6 - 3 + 5 - 1 - 8 + 13 + 4 = 21.)
During the 60th cycle, register X has the value 19, so the signal strength is 60 * 19 = 1140.
During the 100th cycle, register X has the value 18, so the signal strength is 100 * 18 = 1800.
During the 140th cycle, register X has the value 21, so the signal strength is 140 * 21 = 2940.
During the 180th cycle, register X has the value 16, so the signal strength is 180 * 16 = 2880.
During the 220th cycle, register X has the value 18, so the signal strength is 220 * 18 = 3960.
The sum of these signal strengths is 13140.

Find the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles. What is the sum of these six signal strengths?
'''

def part1():
    data = readData()
    cycle = 1
    values = {}
    value = 0
    answer = 0
    while cycle < 222:
        for command in data:
            if command == "noop":
                values[cycle] = value
                cycle += 1
                next
            else:
                null, amount = command.split(' ')
                values[cycle + 1] = value
                values[cycle + 2] = value
                value += int(amount)
                cycle += 1
    numbers = [20, 60, 100, 140, 180, 220]
    for number in numbers:
        answer += (number * values[number-1])
        print(number)
        print(values[number-1])
        print (number * values[number-1])

    print('Part 1 Answer: %s' %answer)
    

    


part1()