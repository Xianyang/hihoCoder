inserts = ['A', 'B', 'C']

def playgame(str):
    while True:
        count = []
        i = 0
        j = 0
        while True:
            j += 1
            if str[j] == str[i] and j < len(str) - 1:
                continue
            elif str[j] == str[i] and j == len(str) - 1:
                count.append((i, j))
                i = j
            else:
                if j > i + 1:
                    count.append((i, j - 1))
                i = j

            if i == len(str) - 1:
                count.reverse()
                for (a, b) in count:
                    newstr = str[:a] + str[b+1:]
                    str = newstr
                break

        if len(count) == 0 or len(str) <= 1:
            break

    # print str
    return str

playgametimes = input()

for i in range(0, playgametimes):
    inputStr = raw_input()
    finalstr = inputStr
    for insert in inserts:
        for i in range(0, len(inputStr) + 1):
            newstr = inputStr[:i] + insert + inputStr[i:]
            gamestr = playgame(newstr)
            if len(gamestr) < len(finalstr):
                finalstr = gamestr

    if len(inputStr) == len(finalstr):
        print 0
    else:
        print len(inputStr) - len(finalstr) + 1




