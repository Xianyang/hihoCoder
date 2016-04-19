N = 5
M = 2

def playgame(N, M, leaveDays):
    if M >= N:
        return 100
    else:
        maxcount = 0
        for i in range(0, len(leaveDays) - M + 1):
            newLeaveDays = leaveDays[:i] + leaveDays[i+M:]
            for j in range(0, len(newLeaveDays) + 1):
                if j == 0:
                    count = newLeaveDays[0] - 1
                elif j == len(newLeaveDays):
                    count = 100 - newLeaveDays[j - 1]
                else:
                    count = newLeaveDays[j] - newLeaveDays[j - 1] - 1
                if count > maxcount:
                    maxcount = count
    return maxcount

playgametimes = input()

for i in range(0, playgametimes):
    (N, M) = (int(x) for x in raw_input().split())
    leaveDays = []
    numbers = raw_input().split()
    for x in numbers:
        leaveDays.append(int(x))
    print playgame(N, M, leaveDays)

