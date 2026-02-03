from asn1_movement import send_positions, makeStep, sensor_reset
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
        knee = {1: 313, 3: 320, 5: 686},
        foot = {1: 200, 3: 200, 5: 800}
    )
    send_positions(1, step1)
    time.sleep(1)

    print("Setting Tripod Group B")
    step2 = makeStep(
        hip = {2: OG_HIP,4: OG_HIP, 6: OG_HIP},
        knee = {2: 312, 4: 686, 6: 686},
        foot = {2: 199, 4: 799, 6: 799}
    )
    send_positions(1, step2)
    time.sleep(1)

    # print("Setting Feet")
    # step3 = makeStep(
    #     foot = {1: 200, 2: 199, 3: 200, 4: 799, 5: 800, 6: 799}
    # )
    # send_positions(1, step3)
    # time.sleep(1)
    
    print("Finished Initialization")

if __name__ == '__main__':
    # Initializes the robot to starting position (spider?)
    initialization()
