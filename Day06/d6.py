def readData():
    with open('input.txt', "r") as read_file:
        inputData = [line.rstrip() for line in read_file]

        return inputData