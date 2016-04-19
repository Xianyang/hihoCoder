import sys

# change marshtomp to fjxmlhx
stringToFind = 'marshtomp'
stringToChange = 'fjxmlhx'

while True:
    try:
        inputString = raw_input()
    except Exception:
        sys.exit()

    lowString = inputString.lower()
    deleteList = []
    while True:
        if stringToFind not in lowString:
            break

        index = lowString.index(stringToFind)
        findString = inputString[index:index+len(stringToFind)]
        inputString = inputString.replace(findString, stringToChange)
        lowString = inputString.lower()

    print inputString
