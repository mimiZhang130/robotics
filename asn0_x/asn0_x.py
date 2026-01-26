import sys
import time
import signal
import threading
import ros_robot_controller_sdk as rrc
import sonar

print('''
**********************************************************
********CS/ME 301 Assignment Template*******
**********************************************************
----------------------------------------------------------
Usage:
    sudo python3 asn_template.py
----------------------------------------------------------
Tips:
 * Press Ctrl+C to close the program. If it fails,
      please try multiple times！
----------------------------------------------------------
''')

board = rrc.Board()
start = True

def Stop(signum, frame):
    global start
    start = False

signal.signal(signal.SIGINT, Stop)

def calculateServoNum(legNum):
    return (legNum - 1) * 3 + 1

def rightLiftAndRotate(legNum, stepSize, knee = 400):
    servoNum = calculateServoNum(legNum)
    board.bus_servo_set_position(.5, [[servoNum + 1, knee], [servoNum, 500 - stepSize]])

def rightPutDown(legNum, knee = 550):
    servoNum = calculateServoNum(legNum)
    board.bus_servo_set_position(.5, [[servoNum + 1, knee]])

def leftLiftAndRotate(legNum, stepSize, knee = 600):
    servoNum = calculateServoNum(legNum)
    board.bus_servo_set_position(.5, [[servoNum + 1, knee], [servoNum, 500 + stepSize]])

def leftPutDown(legNum, knee = 450):
    servoNum = calculateServoNum(legNum)
    board.bus_servo_set_position(.5, [[servoNum + 1, knee]])

def resetHip(legNum, hip = 500):
    servoNum = calculateServoNum(legNum)
    board.bus_servo_set_position(.5, [[servoNum, hip]])

def resetKnee(legNum, knee = 500):
    servoNum = calculateServoNum(legNum)
    board.bus_servo_set_position(.5, [[servoNum + 1, knee]])

def resetLeftFoot(legNum, foot = 500):
    servoNum = calculateServoNum(legNum)
    board.bus_servo_set_position(.5, [[servoNum + 2, foot]])

def resetRightFoot(legNum, foot = 500):
    servoNum = calculateServoNum(legNum)
    board.bus_servo_set_position(.5, [[servoNum + 2, foot]])

def initialization ():
    resetRightFoot(4)
    resetRightFoot(6)
    resetLeftFoot(2)
    time.sleep(1)
    resetRightFoot(5)
    resetLeftFoot(1)
    resetLeftFoot(3)

def waveRight(legNum, stepSize):
    rightLiftAndRotate(legNum, stepSize)
    time.sleep(.25)
    rightPutDown(legNum)
    time.sleep(.25)
    resetHip(legNum)
    time.sleep(.25)
    resetKnee(legNum)
    time.sleep(.25)
    resetRightFoot(legNum)

def waveLeft(legNum, stepSize):
    leftLiftAndRotate(legNum, stepSize)
    time.sleep(.25)
    leftPutDown(legNum)
    time.sleep(.25)
    resetHip(legNum)
    time.sleep(.25)
    resetKnee(legNum)
    time.sleep(.25)
    resetLeftFoot(legNum)

def ripplePair(rightLegNum, leftLegNum, stepSize):
    rightLiftAndRotate(rightLegNum, stepSize)
    leftLiftAndRotate(leftLegNum, stepSize)
    time.sleep(.5)
    rightPutDown(rightLegNum)
    leftPutDown(leftLegNum)
    time.sleep(.5)
    resetHip(rightLegNum)
    resetHip(leftLegNum)
    time.sleep(.5)
    resetKnee(rightLegNum)
    resetKnee(leftLegNum)
    time.sleep(.5)
    resetRightFoot(rightLegNum)
    resetLeftFoot(leftLegNum)

def tripodTrioLeftHeavy(leftLegNumOne, leftLegNumTwo, rightLegNum, stepSize):
    leftLiftAndRotate(leftLegNumOne, stepSize)
    leftLiftAndRotate(leftLegNumTwo, stepSize)
    rightLiftAndRotate(rightLegNum, stepSize)
    time.sleep(.5)
    rightPutDown(rightLegNum)
    leftPutDown(leftLegNumOne)
    leftPutDown(leftLegNumTwo)
    time.sleep(.5)
    resetHip(rightLegNum)
    resetHip(leftLegNumOne)
    resetHip(leftLegNumTwo)
    time.sleep(.5)
    resetKnee(rightLegNum)
    resetKnee(leftLegNumOne)
    resetKnee(leftLegNumTwo)
    time.sleep(.5)
    resetRightFoot(rightLegNum)
    resetLeftFoot(leftLegNumOne)
    resetLeftFoot(leftLegNumTwo)

def tripodTrioRightHeavy(rightLegNumOne, rightLegNumTwo, leftLegNum, stepSize):
    rightLiftAndRotate(rightLegNumOne, stepSize)
    rightLiftAndRotate(rightLegNumTwo, stepSize)
    leftLiftAndRotate(leftLegNum, stepSize)
    time.sleep(.5)
    rightPutDown(rightLegNumOne)
    rightPutDown(rightLegNumTwo)
    leftPutDown(leftLegNum)
    time.sleep(.5)
    resetHip(rightLegNumOne)
    resetHip(rightLegNumTwo)
    resetHip(leftLegNum)
    time.sleep(.5)
    resetKnee(rightLegNumOne)
    resetKnee(rightLegNumTwo)
    resetKnee(leftLegNum)
    time.sleep(.5)
    resetRightFoot(rightLegNumOne)
    resetRightFoot(rightLegNumTwo)
    resetLeftFoot(leftLegNum)

# check for stopping 
# TODO: set bounds
def stopCheck(distance):
    bounds = 175
    if distance < bounds:
        return True
    else:
        return False
    
if __name__ == '__main__':

    s = sonar.Sonar()

    while True:
        
        print('Assignment [] for Group []')
        
        time.sleep(0.1)
        print(s.getDistance())
        
        # ######## Experimentation to see 0 and 500 extremes ########
        # for i in range(1, 19):
        #     print(f'Moving Servo {i} (500)...: \n')
        #     board.bus_servo_set_position(1, [[i, 500]])
        #     time.sleep(2.5)
        #     print(f'Moving Servo {i} (0)...: \n')
        #     board.bus_servo_set_position(1, [[i, 0]])
        #     time.sleep(2.5)
        
        # ## STEP 2 ##
        # # Lift each servo leg to the right of the LED display
        # # 500 is default spider, < 500 is lower, > 500 is higher
        # for i in range(2, 9, 3):
        #     print(f'Using servo {i}')
        #     board.bus_servo_set_position(1, [[i, 250]])
        #     time.sleep(2.5)
        #     board.bus_servo_set_position(1, [[i, 500]])
        #     time.sleep(2.5)
        #     board.bus_servo_stop([i, i + 1])

        # # Lift each servo leg to the left of the LED display 
        # # 500 is default spider, > 500 is higher, < 500 is lower
        # for i in range(11, 18, 3):
        #     print(f'Using servo {i}')
        #     board.bus_servo_set_position(1, [[i, 750]])
        #     time.sleep(2.5)
        #     board.bus_servo_set_position(1, [[i, 500]])
        #     time.sleep(2.5)
        #     board.bus_servo_stop([i, i + 1])
        
        # # Done lifting 
        # print(f'Lifted all legs!')
        # # break

        # ## STEP 3 ##
        # # stream sonar sensor to terminal for 1 second
        # for i in range(10):
        #     start_time = time.time()
        #     while True:
        #         curr_time = time.time()
        #         if curr_time - start_time > 1:
        #             break
        #         else:
        #             print(s.getDistance())

        ## STEP 4 ## 
        # collect readings of sensor for 10cm, 20cm, and 30cm
        print("-- Readings at 10 cm -- ")
        for i in range(10):
            print(f'Trial {i + 1}')
            print(s.getDistance())
        print("Done with 10cm")

        time.sleep(10)
        print("-- Readings at 20 cm -- ")
        for i in range(10):
            print(f'Trial {i + 1}')
            print(s.getDistance())
        print("Done with 20cm")

        time.sleep(10)
        print("-- Readings at 30 cm -- ")
        for i in range(10):
            print(f'Trial {i + 1}')
            print(s.getDistance())
        print("Done with 30cm")
        
        ## STEP 5 ## 
        # reset
        # initialization()
        # time.sleep(1)
        # implement wave
        # Wave: This gait is characterized by moving only one leg forward (or backward) at a
        # time and cycling through all of the legs, creating a “wave” effect.
        while not stopCheck(s.getDistance()): 
            stepSize = 230
            waveRight(3, stepSize)
            time.sleep(.25)
            waveRight(2, stepSize)
            time.sleep(.25)
            waveRight(1, stepSize)
            time.sleep(.25)
            waveLeft(4, stepSize)
            time.sleep(.25)
            waveLeft(5, stepSize)
            time.sleep(.25)
            waveLeft(6, stepSize)
            time.sleep(.25)

        # # Ripple: This gait is characterized by a pair of legs, one on each side of the body, 
        # # being lifted and moved forward (or backward) simultaneously, followed by 
        # # the next pair and so forth, creating a “ripple” effect.
        # while not stopCheck(s.getDistance()):
        #     stepSize = 250
        #     ripplePair(3, 4, stepSize)
        #     time.sleep(.5)
        #     ripplePair(1, 6, stepSize)
        #     time.sleep(.5)
        #     ripplePair(2, 5, stepSize)
        #     time.sleep(.5) 
            
        # Tripod: This gait is characterized by a pair of legs, one on each side of the body, 
        # being lifted and moved forward (or backward) simultaneously, followed by 
        # the next pair and so forth, creating a “ripple” effect.
        while True:
            stepSize = 250
            if stopCheck(s.getDistance()):
                break
            tripodTrioLeftHeavy(1, 3, 5, stepSize)
            time.sleep(1)
            if stopCheck(s.getDistance()):
                break
            tripodTrioRightHeavy(4, 6, 2, stepSize)
            time.sleep(1)

        break
    
        
