import sonar

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

    # setup
    measured = 35
    dt = 1 # TODO?
    target = 35 # our target is 35

    while True:
        # TODO get measured distance
        
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