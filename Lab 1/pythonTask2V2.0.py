import matplotlib
import numpy
import array
import matplotlib.pyplot as plt
import xlsxwriter

radiusIntervalArr = numpy.array([0.0])

AValue = numpy.array ([1.0, -1.0])
print (AValue)
zerosAdderAfter = numpy.zeros([99,1])
setAMatrixValue = numpy.append(AValue,zerosAdderAfter)
setAMatrix = numpy.array([])
setAMatrix = numpy.append (setAMatrix,setAMatrixValue,axis=0)
print (setAMatrix)
#print (setAMatrix)
#print (setAMatrix.shape)
setBMatrix = [(0)]
i = 1
while i<101:
    radiusValue = 0.0005 * (i)
    #assume: aUz,(i+1) +bUz,(i) + cUz,(i-1) -> for r!=0 && r!=R -> a = 1+(deltaR/r) || b = -(2+(deltaR/r)) || c = -1 || d = (dP/dR)*(deltaR^2/miu) = -25
    a = (1/(0.0005*0.0005) + (1/(radiusValue*0.0005)))
    b = -(2/(0.0005*0.0005) + (1/(radiusValue*0.0005)))
    c = 1/(0.0005*0.0005)
    d = -10000
    radiusIntervalArr = numpy.append([radiusIntervalArr],[radiusValue])
    #print(radiusValue)
    #print(i)
    
    
    #New Code
    #Assume function to be like [A][x]=[B] 
    
    #Creating Matrix of B 
    #------------------------------
    setBMatrix = numpy.append([setBMatrix],[d])


    #Creating Matrix of A
    #------------------------------
    AValue = numpy.array ([c,b,a]) #Generating the main Value of A
    print (AValue)
    #Calculation for number of zeros that will be added to the array A
    #------------------------------
    zerosAfterNumber = 101-i+1-3 #Generating number of Zeros that will be added after A in respective array
    #print ("Zeros After: ", zerosAfterNumber)
    if (zerosAfterNumber >= 0):
        zerosAdderAfter = numpy.zeros([zerosAfterNumber,1]) #Generating array of zeros that will be added after the A array
    else:
        pass

    zerosBeforeNumber = i-1 #Generating number of Zeros that will be added before A in respective array
    #print ("Zeros Before : ", zerosBeforeNumber)
    if (zerosBeforeNumber >= 0):
        zerosAdderBefore = numpy.zeros([zerosBeforeNumber,1]) #Generating array of zeros that will be added before the A array
    else:
        pass

    #Create an Array that will be appended to the A Matrix
    #------------------------------
    if ((i-1) <= 0): #special cases where array of zeroes doesn't need to be added to before A Array
        setAMatrixValue = numpy.append(AValue,zerosAdderAfter)
        setAMatrix = numpy.append (setAMatrix, setAMatrixValue, axis=0 )
        setAMatrix = setAMatrix.reshape(2,101) #Reshape because to initialize the matrix A shape
        print (setAMatrix)
        #print (setAMatrix)
    
    elif ((101 - i + 1 -3) < 0): #special cases where array of zeroes doesn't need to be added to before A Array
        AValue = numpy.array ([0,c])
        setAMatrixValue = numpy.append(zerosAdderBefore,AValue)
        setAMatrixValue = setAMatrixValue.reshape(1,101) #Reshape to change the shape into the same shape of matrix A 
        #print(setAMatrixValue)
        setAMatrix = numpy.append(setAMatrix,setAMatrixValue,axis=0) #Appending the respective array (zeros and A) to the matrix A
        print (setAMatrix)

    else: #Normal cases where array of zeroes need to be added to before and after A Array
        setAMatrixValue = numpy.append(zerosAdderBefore,AValue)
        setAMatrixValue = numpy.append (setAMatrixValue,zerosAdderAfter)
        setAMatrixValue = setAMatrixValue.reshape(1,101) #Reshape to change the shape into the same shape of matrix A 
        #print(setAMatrixValue)
        setAMatrix = numpy.append(setAMatrix,setAMatrixValue,axis=0) #Appending the respective array (zeros and A) to the matrix A
        #print (setAMatrix.shape)
    
    #print (setBMatrix)
    #print ("a= ",a," b= ",b," c= ",c," d= ",d)
    i+=1 #Increaing the step of i
    
else:
    print("")
    print (setBMatrix.shape)

    workbook = xlsxwriter.Workbook('setAArray.xlsx')
    worksheet = workbook.add_worksheet()
    row = 0


    for col, data in enumerate (setAMatrix):
        worksheet.write_column (row,col,data)
    
    workbook.close()
    #List of Debugging console print
    #------------------------------
    print ("Start of Array: ", radiusIntervalArr[0], "End of Array: ", radiusIntervalArr[100], "With interval: ", radiusIntervalArr[1]-radiusIntervalArr[0])
    #print ("Start of Array: ", xiMin1Arr[0], "End of Array: ", xiMin1Arr[100])
    #print ("Start of Array: ", xiArr[0], "End of Array: ", xiArr[100])
    #print ("Start of Array: ", xiPls1Arr[0], "End of Array: ", xiPls1Arr[100])
    #print ("Start of Array: ", setBMatrix[0], "End of Array: ", setBMatrix[100])

#A[Uz]=B
#Assignging Value of A and B Matrix
#------------------------------
AMatrix = setAMatrix
BMatrix = setBMatrix
BMatrix[100] = 0

#Doing linear solver alogrithm
#------------------------------
UzArr = numpy.linalg.solve(AMatrix,BMatrix)
#UzArrZero = numpy.append (UzArr,[0])
#radiusIntervalArr = numpy.append(radiusIntervalArr,[0.505])
print (UzArr)
#print (UzArrZero.shape)
#print (radiusIntervalArr.shape)
"""
workbook = xlsxwriter.Workbook('AArray.xlsx')
worksheet = workbook.add_worksheet()
row = 0


for col, data in enumerate (AMatrix):
    worksheet.write_column (row,col,data)
    
workbook.close()
figure=plt.figure()
plt.plot (radiusIntervalArr,UzArr)
#plt.draw()
#plt.show()
#plt.waitforbuttonpress(0)
#plt.close(figure)
"""