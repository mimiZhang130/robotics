from asn2_tripod import tripodCycle
from asn2_walk import checkBlockedandRotate
import sonar
from asn2_movement import sensor_right, sensor_left, sensor_reset
import time
from asn2_initialization import initialization

s = sonar.Sonar()

k_p = .06 # proportional gain
k_i = 0 # integral gain
k_d = 0 # derivative gain

# SETUP
target = 365 # our target is 35 from chassis (35 + 1.5)

# error
total_error = 0.0
prev_error = None

def calculate_error(dt, measured):
    # pid 
    global total_error, prev_error

    # calculate error
    error = target - measured

    # proportional: how wrong right now
    p = k_p * error
    
    # integral: how wrong accumulated over time
    total_error += error * dt
    i = k_i * total_error

    # derivative: how is error changing
    if prev_error == None and dt != 0:
        d = 0.0
    else:
        d = k_d * (error - prev_error) / dt
    prev_error = error

    # output 
    output = p + i + d

    return [error, output]

def pid_reset():
    global total_error, prev_error
    total_error = 0.0
    prev_error = None

def right_correction(prev_time, curr_time):
    # initialization()
    pid_reset()

    curr_time = time.time()

    measured_f = None

    while True:
        checkBlockedandRotate()

        # calculate times since last measured
        prev_time = curr_time
        curr_time = time.time()

        # set dt
        dt = curr_time - prev_time

        # get measured distance
        sensor_right()
        measured = s.getDistance()

        # Low pass filter (tunes out high frequency responeses)
        alpha = 0.3
        if measured_f == None:
            measured_f = measured
        else:
            measured_f = (alpha * measured) + (1 - alpha) * measured_f

        [error, output] = calculate_error(dt, measured_f)
        
        # cap output [-20,20]
        output = max(min(output, 20), -20)

        # print debugs
        print("error: " + str(error))
        print("output: " + str(output))
        print("dist: " + str(measured))
        
        # hip adjusts
        u = int(output * 10)     # Scaling servo "ticks" used by hip servo
        hip_adjusts = [u, u, u, u, u, u]

        # straighten out sensor
        sensor_reset()
        tripodCycle(hip_adjusts)

def left_correction(prev_time, curr_time):
    # initialization()
    pid_reset()

    curr_time = time.time()

    measured_f = None

    while True:
        checkBlockedandRotate()

        # calculate times since last measured
        prev_time = curr_time
        curr_time = time.time()

        # set dt
        dt = curr_time - prev_time

        # get measured distance
        sensor_left()
        measured = s.getDistance()

        # alpha = 0.3
        # if measured_f == None:
        #     measured_f = measured
        # else:
        #     measured_f = (alpha * measured) + (1 - alpha) * measured_f

        [error, output] = calculate_error(dt, measured)
        
        # cap output
        output = max(min(output, 20), -20)

        # print debugs
        print("error: " + str(error))
        print("output: " + str(output))
        print("dist: " + str(measured))

        # hip adjusts
        u = int(output * 10)     # Scaling servo "ticks" used by hip servo
        hip_adjusts = [-u, u, -u, -u, u, -u]

        # straighten out sensor
        sensor_reset()
        tripodCycle(hip_adjusts)



    

        