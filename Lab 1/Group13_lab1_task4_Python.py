import matplotlib
import numpy
import array
import matplotlib.pyplot as plt
import xlsxwriter
from mpl_toolkits import mplot3d

#Declaration of Variables
deltaRadius = 0.0005 
deltaZ = 0.01
Nr = 101
Nz = 101
setAMatrix = numpy.zeros([Nz*Nr,Nz*Nr]) #Filling A Matrix with 0 (Pre-defined value)
viscosityValue = 0.01
setBMatrix = numpy.full ([Nz*Nr],-10000) #Filling B Matrix with -10000 (Pre-defined value)
UzMatrix = numpy.zeros ([Nz,Nr])
inversedUzMatrix = numpy.zeros([Nr,Nz])
zValueArr = []
radiusIntervalArr = []

#Function to map matrix index to a new value, from [i][j] to [1][10201]
def idx(x,y):
    indexNumber = x + y * Nr
    return indexNumber

#Function to map matrix index to a new value, from [1][10201] to [i][j]
def inverseIdx(indexValue):
    yValue = int(indexValue / Nr)
    xValue = int(indexValue % Nr)
    return xValue,yValue

#Boundary Condition for D Matrix
#--------------------------------

#Loop from z=0 to z=0.1 with z interval = 0.01
for j in range (Nz):
    zValue = j * deltaZ
    zValueArr = numpy.append([zValueArr],[zValue]) #Create an array of z set points which will be used to plot the graph afterwards
    
    #Loop from r=0 to r=0.05 with radius interval = 0.0005
    for i in range (Nr):
        radiusValue = i * deltaRadius
        if (j == 0):
            radiusIntervalArr = numpy.append([radiusIntervalArr],[radiusValue]) #Create an array of radius set points which will be used to plot the graph afterwards
        
        #Setting up Boundary Conditions
        #------------------------------
        #When i = N || r = 0.05 || Uz = 0 -> r=0.05, z = 0 - 1
        if (i==(Nr-1)):
            setAMatrix[idx(i,j),idx(j,(i))] = 1
            setBMatrix[idx(i,j)] = 0

        #When i = 0 to 99 and j=0 or N|| Uz = 15 -> r= 0-0.05, z = 0 or z = 1
        elif ((i!=(Nr-1)) and ((j==0) or (j==(Nz-1)))):
            setAMatrix[idx(i,j),idx(j,(i))] = 1
            setBMatrix[idx(i,j)] = 15

        #When i = 0 and j = 1 to 99 || dUz/dr = 0 -> r = 0, z = 0.01 - 0.99
        elif (i==0 and ((j!=0) or (j!=(Nz-1)))):       
            setAMatrix[idx(i,j),idx(j,(i+1))] = (1/(deltaRadius**2)) 
            setAMatrix[idx(i,j),idx(j,(i))] = -1 * (((2)/(deltaRadius**2))+ ( (0.25 * 2) / (viscosityValue * (deltaZ**2)) ) )
            setAMatrix[idx(i,j),idx(j,(i-1))] = (1/(deltaRadius**2))
            setAMatrix[idx(i,j),idx(j+1,(i))] = (0.25 / ( (viscosityValue) * (deltaZ**2) ))
            setAMatrix[idx(i,j),idx(j-1,(i))] = (0.25 / ( (viscosityValue) * (deltaZ**2) ))
        
        #When i = 1 to 99 and j = 1 to 99 || Normal Operation
        else:
            #print ("index = ", idx(i,j), " variable = ", idx(j,(i+1)))
            setAMatrix[idx(i,j),idx(j,(i+1))] = (1/(deltaRadius**2))+(1/(radiusValue * deltaRadius)) 
            setAMatrix[idx(i,j),idx(j,(i))] = -1 * (((2)/(deltaRadius**2)) + ((1)/(radiusValue * deltaRadius)) + ((0.25 * 2)/(viscosityValue * (deltaZ**2))))
            setAMatrix[idx(i,j),idx(j,(i-1))] = (1 / (deltaRadius**2))
            setAMatrix[idx(i,j),idx(j+1,(i))] = (0.25 /((viscosityValue) * (deltaZ**2)))
            setAMatrix[idx(i,j),idx(j-1,(i))] = (0.25 /((viscosityValue) * (deltaZ**2)))
        
#A[Uz]=B
#Assignging Value of A and B Matrix
#------------------------------
AMatrix = setAMatrix
BMatrix = setBMatrix

#Doing linear solver alogrithm
#------------------------------
setUzArr = numpy.linalg.solve(AMatrix,BMatrix)

#Re-configure the matrix of Uz to the form of [101][101] to be plotted
for m, n in enumerate (setUzArr):
    inversedUzMatrixIndex = inverseIdx(m)
    print ("Uz= ",n)
    inversedUzMatrix[inversedUzMatrixIndex[0]][inversedUzMatrixIndex[1]] = n

#For debugging Uz Value, export to excel
"""
workbook = xlsxwriter.Workbook('InversedUzMatrix.xlsx')
worksheet = workbook.add_worksheet()
row = 0

for col, data in enumerate (inversedUzMatrix):
    worksheet.write_column (row,col,data)
    
workbook.close()
"""

xAxes, yAxes = numpy.meshgrid (radiusIntervalArr,zValueArr) #Create a mesh of set points value in the XY plane
fig = plt.figure()
ax=plt.axes(projection="3d") #Define that the plot will be in 3d.
graph = ax.plot_surface(xAxes, yAxes, inversedUzMatrix, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
plt.title("Uz Value in respect to Radius Value and Axial Value",fontsize=20) #Setting the title of the graph
ax.set_xlabel("Radius Value [m]",fontsize=15)   #Assignging x Axis Name
ax.set_ylabel("Axial Value [m]",fontsize=15)    #Assignging y Axis Name
ax.set_zlabel("Uz Value [m/s]",fontsize=15)     #Assignging z Axis Name 
fig.colorbar(graph, shrink=1, aspect=15)        #Assignging color map to see the Uz Value
plt.show()                                      #Generate Graph Pop Up Window
