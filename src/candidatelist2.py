invalidValue = 0xFFFF

def initCandidateList():
    global candidateList
    global validCount
    global worstIndex
    global bestIndex

    candidateList = [invalidValue]*6
    validCount = 0
    worstIndex = 0
    bestIndex = 0
    
def getCandidateList():
    return candidateList

def GetNumOfValidCandidates():
    return validCount

def GetMaxNumCandidates():
    return len(candidateList)

def GetNextBestCandidate():
    global bestIndex
    bestCandidate = candidateList[bestIndex]
    if bestIndex < (len(candidateList)-1):
        bestIndex += 1
    return bestCandidate

def AddCandidate(newValue):
    global worstIndex

    if candidateList[worstIndex] > newValue:
        candidateList[worstIndex] = newValue
        global validCount 
        if validCount < len(candidateList):
            validCount = validCount + 1

        tempIndex = worstIndex
        while (tempIndex > 0):
            prev = tempIndex - 1
            if candidateList[prev] > newValue:
                temp = candidateList[prev]
                candidateList[prev] = newValue
                candidateList[tempIndex] = temp
                tempIndex -= 1
            else:
                break
        
        if worstIndex < (len(candidateList)-1):
            worstIndex += 1
