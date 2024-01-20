requestQueue = [6,5,4,3,1,0]
inputIndexLocation = 100
queueLength = 5
findLocationIndex = 0
inputFloor = int(input("Enter Floor Number: "))

if queueLength == 0:
    requestQueue[0] = inputFloor

while findLocationIndex < (queueLength):
    if inputIndexLocation == 100:
        print ("Current Floor Number Array Value = " + str(requestQueue[findLocationIndex]))
        if requestQueue[findLocationIndex] < inputFloor:
            inputIndexLocation = findLocationIndex
        elif findLocationIndex + 1 == queueLength:
            inputIndexLocation = findLocationIndex + 1

    findLocationIndex = findLocationIndex + 1

sortIndex = (queueLength-1)

while sortIndex >= inputIndexLocation:
    print ("requestQueue[sortIndex+1]: " + str(requestQueue[sortIndex+1]))
    print ("requestQueue[sortIndex]: " + str(requestQueue[sortIndex]))
    print ("sortIndex = " + str(sortIndex))
    requestQueue[sortIndex+1] = requestQueue[sortIndex]
    sortIndex = sortIndex - 1

if not inputIndexLocation == 100:            
    requestQueue[inputIndexLocation] = inputFloor
    queueLength = queueLength + 1
print (inputIndexLocation)
print (requestQueue)