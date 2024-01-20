import matplotlib
import numpy
import array
import matplotlib.pyplot as plt

#Initialization:
Nr = 101
setAMatrix = numpy.zeros([Nr,Nr])       #Filling A Matrix with 0 (Pre-defined value)
setBMatrix = numpy.full([Nr],-0.0025)   #Filling B Matrix with -0.0025 (Pre-defined value)
radiusIntervalArr = []
deltaRadius = 0.0005                    #Assinging value of 0.0005 as radius interval

i = 0
while i in range (Nr):
    radiusValue = deltaRadius * (i)
    #Boundary Condition
    if (i==0):
        setAMatrix [i][i] = 1.0     #Set the value for A Matrix [0][0]
        setAMatrix [i][i+1] = -1.0  #Set the value for A Matrix [0][1]
        setBMatrix [i] = 0          #Set the value for B Matrix [0]
    
    elif (i==100):
        setAMatrix [i][i] = 1.0 #Set the value for A Matrix [100][100]
        setBMatrix [i] = 0      #Set the value for B Matrix [100]

    #---------------------------------------------
    else: 
       
        setAMatrix[i][i+1] = 1.0 + ((0.0005)/radiusValue)   #Set the value for A Matrix [i][i+1]
        setAMatrix[i][i] = (-2.0 - ((0.0005/radiusValue)))  #Set the value for A Matrix [i][i]
        setAMatrix[i][i-1] = 1.0                            #Set the value for A Matrix [i][i-1]
    
    radiusIntervalArr = numpy.append([radiusIntervalArr],[radiusValue]) #Create an array of radius set points which will be used to plot the graph afterwards
    
    i+=1

#A[Uz]=B
#Assignging Value of A and B Matrix
#------------------------------
AMatrix = setAMatrix
BMatrix = setBMatrix

#Doing linear solver alogrithm
#------------------------------
UzArr = numpy.linalg.solve(AMatrix,BMatrix)

#Plotting the graph
#------------------------------
figure = plt.figure('Number 1')                                 #Setting the window name of the graph
plt.plot (radiusIntervalArr,UzArr)                              #Plotting the graph
plt.title("Uz Value in respect to Radius Value",fontsize=20)    #Setting the title of the graph
plt.xlabel("Radius Value [m]",fontsize=15)                      #Assignging x Axis Name
plt.ylabel("Uz Value [m/s]",fontsize=15)                        #Assignging y Axis Name
plt.grid()                                                      #Show Grid on the graph
plt.show()                                                      #Generate Graph Pop Up Window
