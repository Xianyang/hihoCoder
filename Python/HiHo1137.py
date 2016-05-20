import itertools


class Candidate:
    def __init__(self, index, information):
        self.index = index + 1
        self.gender = information[0].upper()
        self.ability = int(information[1])
        self.salary = int(information[2])


def getBestCandidates(N, X, Y, B, candidates):
    suitableCanditates = []
    finalCanditateSampleList = []
    femaleCandidates = [candidate for candidate in candidates if candidate.gender == 'F']
    maleCandidates = [candidate for candidate in candidates if candidate.gender == 'M']

    maleSampleList = list(itertools.combinations(maleCandidates, X))
    femaleSampleList = list(itertools.combinations(femaleCandidates, Y))
    for maleSample in maleSampleList:
        for femaleSample in femaleSampleList:
            sample = maleSample + femaleSample
            if sum([candidate.salary for candidate in sample]) <= B:
                sample = sorted(sample, key=lambda candidate:candidate.index)
                suitableCanditates.append(sample)

    suitableCanditates = sorted(suitableCanditates, key=lambda i: sum([people.ability for people in i]))
    suitableCanditates.reverse()

    maxAbility = sum(candidate.ability for candidate in suitableCanditates[0])
    for sample in suitableCanditates:
        if sum(candidate.ability for candidate in sample) == maxAbility:
            finalCanditateSampleList.append(sample)
        else:
            break

    print sum(candidate.ability for candidate in finalCanditateSampleList[0]), sum(candidate.salary for candidate in finalCanditateSampleList[0])
    for candidate in finalCanditateSampleList[0]:
        print candidate.index,

while True:
    try:
        parameter1 = [int(x) for x in raw_input().split()]
        N = parameter1.pop(0)
        X = parameter1.pop(0)
        Y = parameter1.pop(0)
        B = parameter1.pop(0)
        candidates = [Candidate(index, raw_input().split()) for index in range(0, N)]
    except Exception:
        print 'Wrong parameters, try again'
        continue

    getBestCandidates(N, X, Y, B, candidates)
