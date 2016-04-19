import sys

redBall = 'R'
yellowBall = 'Y'
blueBall = 'B'

def isNeedCleanBox(count1, count2, count3, constraint):
    a = abs(count1 - count2)
    b = abs(count1 - count3)
    c = abs(count2 - count3)

    setA = {a, b, c}
    if setA == set(constraint):
        return True
    else:
        return False


while True:
    try:
        constraint = [int(x) for x in raw_input().split()]
        sequence = raw_input()
    except Exception:
        sys.exit()

    maxCount, i, j = 0, 0, 0
    while j < len(sequence):
        # check if clean the box
        subSequence = sequence[i:j+1]
        countForRed = subSequence.count(redBall)
        countForYellow = subSequence.count(yellowBall)
        countForBlue = subSequence.count(blueBall)
        if isNeedCleanBox(countForRed, countForYellow, countForBlue, constraint):
            maxCount = max(maxCount, len(subSequence))
            j += 1
            i = j
            continue
        else:
            maxCount = max(maxCount, len(subSequence))
            j += 1

    print maxCount
