import matplotlib
import numpy
import array
import matplotlib.pyplot as plt

radiusIntervalArr = numpy.array([0.0])

#Initialization:
Nr = 101
setAMatrix = numpy.zeros([Nr,Nr])
setBMatrix = numpy.full([Nr],-2.5*10**-7)

#Boundary Condition
#---------------------------------------------
setAMatrix [0][0] = 1.0
setAMatrix [0][1] = -1.0
setBMatrix [0] = 0
setAMatrix [100][100] = 1.0
setBMatrix [100] = 0
radiusIntervalArr = []
#AValue = numpy.array ([1.0,-1.0])
#zerosAdderAfter = numpy.zeros([99,1])
#setAMatrixValue = numpy.append(AValue,zerosAdderAfter)
#setAMatrix = numpy.array([])
#setAMatrix = numpy.append (setAMatrix,setAMatrixValue,axis=0)
#print (setAMatrix)
#print (setAMatrix.shape)

#setBMatrix = [(0)]
deltaRadius = 0.0005
i = 0
while i in range (Nr):
    radiusValue = deltaRadius * (i)
    #assume: aUz,(i+1) +bUz,(i) + cUz,(i-1) -> for r!=0 && r!=R -> a = 1+(deltaR/r) || b = -(2+(deltaR/r)) || c = -1 || d = (dP/dR)*(deltaR^2/miu) = -25
    if (i==0):
        setAMatrix [i][i] = 1.0
        setAMatrix [i][i+1] = -1.0
        setBMatrix [i] = 0
    
    elif (i==100):
        setAMatrix [i][i] = 1.0
        setBMatrix [i] = 0

    else: 
        setAMatrix[i][i+1] = (1/20) + (1/20)*(deltaRadius/radiusValue) + (radiusValue**2)/50 + (radiusValue*deltaRadius/50)
        setAMatrix[i][i] = -1 * (2/20 + (1/20)*(deltaRadius/radiusValue) + 2*(radiusValue**2)/50 + (radiusValue*deltaRadius/50))
        setAMatrix[i][i-1] = (1/20) + (radiusValue**2/50)
    

    #a = (1/20) + (1/20)*(deltaRadius/radiusValue) + (radiusValue**2)/50 + (radiusValue*deltaRadius/50)
    #b = -1 * (2/20 + (1/20)*(deltaRadius/radiusValue) + 2*(radiusValue**2)/50 + (radiusValue*deltaRadius/50))
    #c = (1/20) + (radiusValue**2/50)
    #d = -2.5*10**-7
    radiusIntervalArr = numpy.append([radiusIntervalArr],[radiusValue])
    #print(radiusValue)
    #print(i)
    
    #New Code
    #Assume function to be like [A][x]=[B] 
    
    #Creating Matrix of B 
    #------------------------------
    #setBMatrix = numpy.append([setBMatrix],[d])

    #Creating Matrix of A
    #------------------------------
    #AValue = numpy.array ([c,b,a]) #Generating the main Value of A
    
    #Calculation for number of zeros that will be added to the array A
    #------------------------------
    #zerosAfterNumber = 101-i+1-3 #Generating number of Zeros that will be added after A in respective array
    #print ("Zeros After: ", zerosAfterNumber)
    #if (zerosAfterNumber >= 0):
    #    zerosAdderAfter = numpy.zeros([zerosAfterNumber,1]) #Generating array of zeros that will be added after the A array
    #else:
    #    pass

    #zerosBeforeNumber = i-1 #Generating number of Zeros that will be added before A in respective array
    #print ("Zeros Before : ", zerosBeforeNumber)
    #if (zerosBeforeNumber >= 0):
    #    zerosAdderBefore = numpy.zeros([zerosBeforeNumber,1]) #Generating array of zeros that will be added before the A array
    #else:
    #    pass

    #Create an Array that will be appended to the A Matrix
    #------------------------------
    #if ((i-1) <= 0): #special cases where array of zeroes doesn't need to be added to before A Array
    #    setAMatrixValue = numpy.append(AValue,zerosAdderAfter)
    #    setAMatrix = numpy.append (setAMatrix, setAMatrixValue, axis=0 )
    #    setAMatrix = setAMatrix.reshape(2,101) #Reshape because to initialize the matrix A shape
    #    #print (setAMatrix)
    
    #elif ((101 - i + 1 -3) < 0): #special cases where array of zeroes doesn't need to be added to before A Array
    #    AValue = numpy.array ([0,c])
    #    setAMatrixValue = numpy.append(zerosAdderBefore,AValue)
    #    setAMatrixValue = setAMatrixValue.reshape(1,101) #Reshape to change the shape into the same shape of matrix A 
    #    #print(setAMatrixValue)
    #    setAMatrix = numpy.append(setAMatrix,setAMatrixValue,axis=0) #Appending the respective array (zeros and A) to the matrix A
        
    #else: #Normal cases where array of zeroes need to be added to before and after A Array
    #    setAMatrixValue = numpy.append(zerosAdderBefore,AValue)
    #    setAMatrixValue = numpy.append (setAMatrixValue,zerosAdderAfter)
    #    setAMatrixValue = setAMatrixValue.reshape(1,101) #Reshape to change the shape into the same shape of matrix A 
    #    #print(setAMatrixValue)
    #    setAMatrix = numpy.append(setAMatrix,setAMatrixValue,axis=0) #Appending the respective array (zeros and A) to the matrix A
    #    #print (setAMatrix.shape)
    
    #print (setBMatrix)
    #print ("a= ",a," b= ",b," c= ",c," d= ",d)
    i+=1 #Increaing the step of i


    #List of Debugging console print
    #------------------------------
    #print ("Start of Array: ", radiusIntervalArr[0], "End of Array: ", radiusIntervalArr[100], "With interval: ", radiusIntervalArr[1]-radiusIntervalArr[0])
    #print ("Start of Array: ", xiMin1Arr[0], "End of Array: ", xiMin1Arr[100])
    #print ("Start of Array: ", xiArr[0], "End of Array: ", xiArr[100])
    #print ("Start of Array: ", xiPls1Arr[0], "End of Array: ", xiPls1Arr[100])
    #print ("Start of Array: ", setBMatrix[0], "End of Array: ", setBMatrix[100])

#A[Uz]=B
#Assignging Value of A and B Matrix
#------------------------------
AMatrix = setAMatrix
BMatrix = setBMatrix

#Doing linear solver alogrithm
#------------------------------
UzArr = numpy.linalg.solve(AMatrix,BMatrix)
#UzArrZero = numpy.append (UzArr,[0])
#radiusIntervalArr = numpy.append(radiusIntervalArr,[0.505])
#print (UzArrZero)
print (UzArr.shape)
print (radiusIntervalArr)

figure = plt.figure('Task 2')
plt.plot (radiusIntervalArr,UzArr)
plt.title("Uz Value")
plt.xlabel("Radius Value")
plt.ylabel("Uz Value")
plt.grid()
plt.draw()
plt.waitforbuttonpress(0)
plt.close(figure)