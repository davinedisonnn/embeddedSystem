#Main Program
#Create robot objects -> Start simulation -> updating each robot throughout the simulation.
from coppeliasim_zmqremoteapi_client import RemoteAPIClient #Importing Communication API for Python to CoppeliaSim
client = RemoteAPIClient() #Create a new instance of CoppeliaSim Client in Python
sim = client.require('sim') #Create a new instance of CoppeliaSim called sim.
import robot #Importing robot.py file 
from robot import Robots #Improting Robots class from robot.py file

def main():
    r0 = Robots(0) #Create an instance of Robot 0
    r1 = Robots(1) #Create an instance of Robot 1
    r2 = Robots(2) #Create an instance of Robot 2
    r3 = Robots(3) #Create an instance of Robot 3
    r4 = Robots(4) #Create an instance of Robot 4
    sim.setStepping(True)
    sim.startSimulation() #Starting the Simulation
    while (t := sim.getSimulationTime()) < 30: #Limiting the Simulation time to less than 30s
        print(f'Simulation time: {t:.2f} [s]') #Print out simulation time
        r0.update() #Updating the condition of the robot 0, steering angle, and velocity according to its position and orientation
        r1.update() #Updating the condition of the robot 1, steering angle, and velocity according to its position and orientation
        r2.update() #Updating the condition of the robot 2, steering angle, and velocity according to its position and orientation
        r3.update() #Updating the condition of the robot 3, steering angle, and velocity according to its position and orientation
        r4.update() #Updating the condition of the robot 4, steering angle, and velocity according to its position and orientation
        sim.step() #Updating the simulation, take a new step in the simulation
    sim.stopSimulation() #Stop the simulation after t >= 30s
if __name__ == '__main__':
    main()



