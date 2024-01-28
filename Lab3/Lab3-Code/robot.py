#Script for creating a class for the robots with complete algorithm and generalised functions which can be used to control the robots in the class
from coppeliasim_zmqremoteapi_client import RemoteAPIClient #Importing ZMW Remote API for communicating with CoppeliSim
import constant     #Importing constant.py file to load all of the constant variables
import utils        #Improting utils.py file to load the image processing function
import numpy as np  #Importing NumPy to process matrixes
import cv2 as cv    #Importing OpenCV for image processing
from constant import res, center, kp, ki, kd, scale_factor  #Importing Variables from constant.py file

#Creating a new instance of CoppeliaSim using Remote API Client from ZMQ and assigning sim as its name
client = RemoteAPIClient()
sim = client.require('sim')

#Create a class called Robots in which all of the functions of the robot can be made and accessed for multiple robots
class Robots:
    motor_r = "null"
    motor_l = "null"
    vision = "null"
    targetVelocity_r = 5.0
    targetVelocity_l = 5.0
    speed = 5.0
    integral = 0
    error_prev = 0

#Constructor to set the values of some class variables. Also to do object selectin in the robot
    def __init__(self, num):
        self.motor_r = sim.getObject(f"/PioneerP3DX[{num}]/rightMotor")
        self.motor_l = sim.getObject(f"/PioneerP3DX[{num}]/leftMotor")
        self.vision = sim.getObject(f"/PioneerP3DX[{num}]/Vision_sensor")
        self.speed = 5.0
        self.integral = 0
        self.error_prev = 0

#Function for Calculating the steering angle using Image Processing and PID Controller
    def steeringcalc(self, cy):
        error = constant.center - cy
        self.integral = self.integral + error
        derivative = error - self.error_prev
        # Calculate PID output
        if error:
            pid_output = constant.kp * error + constant.ki * self.integral + constant.kd * derivative
        else:
            pid_output = 0.0
        # Save current error for the next iteration
        self.error_prev = error

        # Steering Angle Value
        steering_angle = constant.scale_factor * pid_output
        return steering_angle

#Function for calculating final velocity of the robot.
    def velocityangle(self, angle):
        self.targetVelocity_l = self.speed - (angle / 180) * self.speed
        self.targetVelocity_r = self.speed + (angle / 180) * self.speed

#Function that will update the condition of the robot in which will update the steering angle and velocity of the robot.
    def update(self):
        image, constant.res = sim.getVisionSensorImg(self.vision)
        cy = utils.processimage(image)
        ang = self.steeringcalc(cy)
        self.velocityangle(ang)
        sim.setJointTargetVelocity(self.motor_r, self.targetVelocity_r)
        sim.setJointTargetVelocity(self.motor_l, self.targetVelocity_l)