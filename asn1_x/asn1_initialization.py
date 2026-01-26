from asn1_movement import send_positions, makeStep
import signal
import time
OG_HIP = 500

start = True

def Stop(signum, frame):
    global start
    start = False

signal.signal(signal.SIGINT, Stop)

def initialization ():
    print("Initializing")
    
    print("Setting Hips")
    send_positions(1, makeStep(hip = {1: OG_HIP, 2: OG_HIP, 3: OG_HIP, 4: OG_HIP, 5: OG_HIP, 6: OG_HIP}))
    time.sleep(1)

    print("Setting Knees")
    send_positions(1, makeStep(knee = {1: 313, 2: 312, 3: 320, 4: 686, 5: 686, 6: 686}))
    time.sleep(1)

    print("Setting Feet")
    send_positions(1, makeStep(foot = {1: 200, 2: 199, 3: 200, 4: 799, 5: 800, 6: 799}))
    time.sleep(1)
    
    print("Finished Initialization")

if __name__ == '__main__':
    # Initializes the robot to starting position (spider?)
    initialization()
