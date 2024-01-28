#Setting up the constant variables for the entire program and PID Control Logic
res = 128.0 #For resolution initialization
center = res/2.0 #To find the center of the image

#PID Gains
kp = 0.05   #Setting up P Value in PID Controller
ki = 0.01   #Setting up I Value in PID Controller
kd = 0.0    #Setting up D Value in PID Controller
scale_factor = 0.5 