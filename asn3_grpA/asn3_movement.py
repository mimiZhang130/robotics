import ros_robot_controller_sdk as rrc
import sonar
import signal
import time

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
    board.bus_servo_set_position(duration, positions)

# CREATE A MOVEMENT
# makeStep creates a step that can then be fed into send_positions to run

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


# PLATFORM TURNS
# going towards 0 deg turns the sensor right

plat_servo = 21

def sensor_reset():
    board.bus_servo_set_position(.5, [[plat_servo, 507]])
    time.sleep(.5)

def sensor_right():
    board.bus_servo_set_position(.5, [[plat_servo, 100]])
    time.sleep(.5)

def sensor_left():
    board.bus_servo_set_position(.5, [[plat_servo, 900]])
    time.sleep(.5)