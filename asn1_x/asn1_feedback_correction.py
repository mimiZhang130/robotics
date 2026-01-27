import sonar
from asn1_movement import sensor_right
import time

s = sonar.Sonar()

if __name__ == '__main__':  
    
    # pid 
    k_p = 1 # proportional gain
    k_i = 0 # integral gain
    k_d = 0 # derivative gain
    
    # error
    total_error = 0
    error = 0
    prev_error = error

    # time
    prev_time = 0
    curr_time = 0

    # setup
    measured = 35
    
    target = 35 # our target is 35

    while True:
        # get measured distance
        sensor_right()
        measured = s.getDistance()

        # set dt
        prev_time = curr_time
        curr_time = time.time()
        dt = curr_time - prev_time

        # calculate error
        error = measured - target

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

        # TODO what do you do with output? 
        print("hello")