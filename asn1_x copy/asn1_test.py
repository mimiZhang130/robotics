import ros_robot_controller_sdk as rrc
import time
import signal
import sonar

# Tripod: This gait is characterized by a pair of legs, one on each side of the body, 
        # being lifted and moved forward (or backward) simultaneously, followed by 
        # the next pair and so forth, creating a “ripple” effect.

OG_HIP = 500
STEP_SIZE = 100

# + Initializaion 
board = rrc.Board()
start = True
s = sonar.Sonar()

def Stop(signum, frame):
    global start
    start = False

signal.signal(signal.SIGINT, Stop)

def send_positions(duration, positions):
    # Positions is a list of servo ids positions 
    # EX: [[1, 500], [3, 200], [5, 230]]
    bounds = 175
    if not s.getDistance() < bounds:
        board.bus_servo_set_position(duration, positions)

def hip_servo(legNum):  
    return (legNum - 1) * 3 + 1
def knee_servo(legNum): 
    return (legNum - 1) * 3 + 2
def foot_servo(legNum):
    return (legNum - 1) * 3 + 3

def makeStep(hip=None, knee=None, foot=None):
    # hip, knee, and foot are dicts that hold legNum:positionValue
    # Makes dictionaries
    hip  = hip  or {}
    knee = knee or {}
    foot = foot or {}

    positions = []
    for leg, val in hip.items():
        positions.append([hip_servo(leg), val])
    for leg, val in knee.items():
        positions.append([knee_servo(leg), val])
    for leg, val in foot.items():
        positions.append([foot_servo(leg), val])

    return positions

# Initializes the robot to starting position (spider?)
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

# New Tripod Stuff Starts Here
tripodA = (1, 3, 5) 
tripodB = (2, 4, 6)

def tripodCycle():
    # Step 1: Lifting and moving forwards Tripod Group A and Return Tripod Group B to OG option
    step1 = makeStep(
        hip = {1:380, 3:380, 5:600, 2:OG_HIP, 4:OG_HIP, 6:OG_HIP},
        knee = {1:200, 3:200, 5:700}
    )
    
    send_positions(.3, step1) 
    time.sleep(.1)
    
    # Step 2: Put down Tripod Group A
    step2 = makeStep(
        knee = {1: 280, 3:280, 5:650}
    )

    send_positions(.2, step2)
    time.sleep(.1)

    # Step 3: Return Tripod Group A to OG position and lift Tripod Group B
    step3 = makeStep(
        hip = {1:OG_HIP, 3:OG_HIP, 5:OG_HIP, 2:400, 4:620, 6:620},
        knee = {2:180, 4:780, 6:750 }
    )

    send_positions(.3, step3)
    time.sleep(.1)

    # Step 4: Put tripod group B back on the ground
    step4 = makeStep(
        knee = {2:270, 4:690, 6:690}
    )

    send_positions(.2, step4)
    time.sleep(.1)

def turnRight():
    # Step 1: Lift and move tripod group A where legs 1 & 3 move forwards & 5 moves backwards 
    # & return tripod group B back to OG position
    step1 = makeStep(
        hip = {1:380, 3:380, 5:400, 2:OG_HIP, 4:OG_HIP, 6:OG_HIP},
        knee = {1:200, 3:200, 5:700}
    )

    send_positions(.3, step1) 
    time.sleep(.1)
    
    # Step 2: Put down Tripod Group A
    step2 = makeStep(
        knee = {1: 280, 3:280, 5:650}
    )

    send_positions(.2, step2)
    time.sleep(.1)

    # Step 3: Lift and move tripod group B where legs 2 move forwards & legs 4 & 6 move backwards
    # & return Tripod Group A to OG position and lift
    step3 = makeStep(
        hip = {1:OG_HIP, 3:OG_HIP, 5:OG_HIP, 2:400, 4:400, 6:400},
        knee = {2:180, 4:780, 6:750 }
    )

    send_positions(.3, step3)
    time.sleep(.1)

    # Step 4: Put tripod group B back on the ground
    step4 = makeStep(
        knee = {2:270, 4:690, 6:690}
    )

    send_positions(.2, step4)
    time.sleep(.1)

if __name__ == '__main__':
    initialization()
    print("done initializing")
    while True:
        turnRight()