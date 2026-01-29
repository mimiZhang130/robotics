from asn1_tripod import tripodCycle
from asn1_walk import checkBlockedandRotate
import sonar
from asn1_movement import sensor_right, sensor_left, sensor_reset
import time
from asn1_initialization import initialization

s = sonar.Sonar()

def calculate_error(dt, measured = 350):
    # pid 
    k_p = .02 # proportional gain
    k_i = .005 # integral gain
    k_d = .02 # derivative gain
    
    # error
    total_error = 0
    error = 0
    prev_error = error

    # SETUP
    target = 365 # our target is 35 from chassis (35 + 1.5)

    # calculate error
    error = target - measured

    # proportional: how wrong right now
    p = k_p * error
    
    # integral: how wrong accumulated over time
    total_error += error * dt
    i = k_i * total_error

    # derivative: how is error changing
    d = k_d * (error - prev_error) / dt
    prev_error = error

    # output 
    output = p + i + d

    return [error, output]

def right_correction(prev_time, curr_time):
    initialization()
    while True:
        # calculate times since last measured
        prev_time = curr_time
        curr_time = time.time()

        # set dt
        dt = curr_time - prev_time

        # get measured distance
        sensor_right()
        measured = s.getDistance()
        [error, output] = calculate_error(dt, measured)
        
        # cap output
        output = min(int(output), 20)
        output = max(int(output), -20)

        # print debugs
        print("error: " + str(error))
        print("output: " + str(output))
        print("dist: " + str(measured))
        
        # hip adjusts
        hip_adjusts = [output * 10, 0, output * 10, 0, 0, 0]

        # straighten out sensor
        sensor_reset()
        tripodCycle(hip_adjusts)
        checkBlockedandRotate()

def left_correction(prev_time, curr_time):
    initialization()
    while True:
        # calculate times since last measured
        prev_time = curr_time
        curr_time = time.time()

        # set dt
        dt = curr_time - prev_time

        # get measured distance
        sensor_left()
        measured = s.getDistance()
        [error, output] = calculate_error(dt, measured)
        
        # cap output
        output = min(int(output), 20)
        output = max(int(output), -20)

        # print debugs
        print("error: " + str(error))
        print("output: " + str(output))
        print("dist: " + str(measured))

        # hip adjusts
        hip_adjusts = [output * -10, 0, output * -10, 0, 0, 0]

        # straighten out sensor
        sensor_reset()
        tripodCycle(hip_adjusts)
        checkBlockedandRotate()



    

        