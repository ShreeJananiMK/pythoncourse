inputList = [23, 65, 3, 9, 100, 9]

def smallestNumber(cList):
    sNumber = 999
    for x in cList:
        if x < sNumber:
            sNumber = x
    
    return sNumber 
    
def compareList (newList,inputList):
    tempList = []
    for i in inputList:
        if i not in newList:
            tempList.append(i)
    return tempList

def sorting(inputList):
    newList = []
    for num in inputList:
        sn = smallestNumber(compareList (newList,inputList))
        if sn < 999:
            newList.append(sn)

    return newList
    

print(sorting(inputList))