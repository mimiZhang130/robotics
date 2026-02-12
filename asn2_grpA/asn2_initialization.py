from asn2_movement import send_positions, makeStep, sensor_reset
import signal
import time
OG_HIP = 500

start = True

def Stop(signum, frame):
    global start
    start = False

signal.signal(signal.SIGINT, Stop)

def initialization ():
    sensor_reset()
    print("Initializing")
    
    print("Setting Tripod Group A")
    step1 = makeStep(
        hip = {1: OG_HIP, 3: OG_HIP, 5: OG_HIP},
        knee = {1: 312, 3: 320, 5: 686},
        foot = {1: 200, 3: 200, 5: 800}
    )
    send_positions(1, step1)
    time.sleep(1)

    print("Setting Tripod Group B")
    step2 = makeStep(
        hip = {2: OG_HIP,4: OG_HIP, 6: OG_HIP},
        knee = {2:270, 4:690, 6:690},
        foot = {2: 199, 4: 799, 6: 799}
    )
    send_positions(1, step2)
    time.sleep(1)
    
    print("Finished Initialization")

if __name__ == '__main__':
    # Initializes the robot to starting position (spider?)
    initialization()
