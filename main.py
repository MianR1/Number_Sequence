def numIncreasing2(L):
    newLis = []
    bigLis = [[]]
    allLis = []
    pttrn = False
    for x in range(0, len(L)):

        if x == len(L) - 1:
            if len(newLis) == 0:
                newLis.append(L[0])
            else:
                newLis.append(L[x])
            allLis.append(newLis)
            newLis = []

        elif L[x] < L[x + 1]:
            newLis.append(L[x])
            pttrn = True

        elif pttrn:
            newLis.append(L[x])
            allLis.append(newLis)
            newLis = []

    if len(allLis) <= 1:
        bigLis[0] = allLis[0]
    else:
        for i in range(0, len(allLis) - 1):
            if len(allLis[i]) > len(allLis[i + 1]):
                bigLis[0] = allLis[i]
            else:
                bigLis[0] = allLis[i + 1]

    return bigLis[0]