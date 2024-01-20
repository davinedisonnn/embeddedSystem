import matplotlib
import numpy
import array
import matplotlib.pyplot as plt
import xlsxwriter
from mpl_toolkits import mplot3d
#150409
Radius_Interval = 0.0005 
Delta_Z = 0.01
Nr = 101
Nz = 101
Left_Matrix = numpy.zeros([Nz*Nr,Nz*Nr])
rho = 0.01
Right_Matrix = numpy.full ([Nz*Nr],-10000)
VzMatrix = numpy.zeros ([Nz,Nr])
Vz_inv = numpy.zeros([Nr,Nz])
Z = []
Radius = []

def Indexing(x,y):
    Index_Number = x + y * Nr
    return Index_Number

def ReDo_Matrix(Index):
    Vertcial = int(Index / Nr)
    Horizontal = int(Index % Nr)
    return Horizontal,Vertcial

for j in range (Nz):
    Z_Sing = j * Delta_Z
    Z = numpy.append([Z],[Z_Sing])
    for i in range (Nr):
        Radius_Sing = i * Radius_Interval
        if (j == 0):
            Radius = numpy.append([Radius],[Radius_Sing])
        if (((j==0))):
            Left_Matrix[Indexing(i,j),Indexing(j,(i))] = 1
            Right_Matrix[Indexing(i,j)] = 15
        
        elif (j==(Nz-1)):
            Left_Matrix[Indexing(i,j),Indexing(j,(i))] = 1
            Right_Matrix[Indexing(i,j)] = 15

        elif (i==(Nr-1)):
            Left_Matrix[Indexing(i,j),Indexing(j,(i))] = 1
            Right_Matrix[Indexing(i,j)] = 0

        elif (i==0):       
            Left_Matrix[Indexing(i,j),Indexing(j,(i+1))] = 1
            Left_Matrix[Indexing(i,j),Indexing(j,(i))] = -1
            Right_Matrix[Indexing(i,j)] = 0
            
        else:
            Left_Matrix[Indexing(i,j),Indexing(j,(i+1))] = (1/(Radius_Interval**2))+(1/(Radius_Sing * Radius_Interval)) 
            Left_Matrix[Indexing(i,j),Indexing(j,(i))] = -1 * (((2)/(Radius_Interval**2)) + ((1)/(Radius_Sing * Radius_Interval)) + ((0.25 * 2)/(rho * (Delta_Z**2))))
            Left_Matrix[Indexing(i,j),Indexing(j,(i-1))] = (1 / (Radius_Interval**2))
            Left_Matrix[Indexing(i,j),Indexing(j+1,(i))] = (0.25 /((rho) * (Delta_Z**2)))
            Left_Matrix[Indexing(i,j),Indexing(j-1,(i))] = (0.25 /((rho) * (Delta_Z**2)))
        
Vz = numpy.linalg.solve(Left_Matrix,Right_Matrix)

for q, w in enumerate (Vz):
    Vz_Index = ReDo_Matrix(q)
    Vz_inv[Vz_Index[0]][Vz_Index[1]] = w

X_Axis, Y_Axis = numpy.meshgrid (Radius,Z)
fig = plt.figure()
ax=plt.axes(projection="3d")
graph = ax.plot_surface(X_Axis, Y_Axis, Vz_inv, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
plt.title("Vz ",fontsize=20) 
ax.set_xlabel("Radius",fontsize=15)
ax.set_ylabel("Axial",fontsize=15)
ax.set_zlabel("Vz",fontsize=15) 
fig.colorbar(graph, shrink=1, aspect=15)
plt.show()                              
