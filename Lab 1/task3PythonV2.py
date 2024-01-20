import matplotlib
import numpy
import array
import matplotlib.pyplot as plt

radiusIntervalArr = numpy.array([0.0])

#Initialization:
Nr = 101
setAMatrix = numpy.zeros([Nr,Nr])
setBMatrix = numpy.full([Nr],-2.5*10**-7)
radiusIntervalArr = []
deltaRadius = 0.0005

i = 0
while i in range (Nr):
    radiusValue = deltaRadius * (i)
    #assume: aUz,(i+1) +bUz,(i) + cUz,(i-1) -> for r!=0 && r!=R -> a = 1+(deltaR/r) || b = -(2+(deltaR/r)) || c = -1 || d = (dP/dR)*(deltaR^2/miu) = -2.5*10**-7
    #Boundary Condition
    if (i==0):
        setAMatrix [i][i] = 1.0
        setAMatrix [i][i+1] = -1.0
        setBMatrix [i] = 0
    
    elif (i==100):
        setAMatrix [i][i] = 1.0
        setBMatrix [i] = 0

    #---------------------------------------------
    else: 
        setAMatrix[i][i+1] = (1/20) + (1/20)*(deltaRadius/radiusValue) + (radiusValue**2)/50 + (radiusValue*deltaRadius/50)
        setAMatrix[i][i] = -1 * (2/20 + (1/20)*(deltaRadius/radiusValue) + 2*(radiusValue**2)/50 + (radiusValue*deltaRadius/50))
        setAMatrix[i][i-1] = (1/20) + (radiusValue**2/50)
    
    radiusIntervalArr = numpy.append([radiusIntervalArr],[radiusValue])
    
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
figure = plt.figure('Task 2')
plt.plot (radiusIntervalArr,UzArr)
plt.title("Uz Value in respect to Radius Value",fontsize=20)
plt.xlabel("Radius Value [m]",fontsize=15)
plt.ylabel("Uz Value [m/s]",fontsize=15)
plt.grid()
plt.show()