
import sonar
import ros_robot_controller_sdk as rrc
import time

board = rrc.Board()
s = sonar.Sonar()

def calculateServoNum(legNum):
    return (legNum - 1) * 3 + 1

def rightLiftAndRotate(legNum, stepSize, knee = 600):
    servoNum = calculateServoNum(legNum)
    if not stopCheck(s.getDistance()):
        board.bus_servo_set_position(.5, [[servoNum + 1, knee], [servoNum, 500 - stepSize]])

def rightPutDown(legNum, knee = 400):
    servoNum = calculateServoNum(legNum)
    if not stopCheck(s.getDistance()):
        board.bus_servo_set_position(.5, [[servoNum + 1, knee]])

def leftLiftAndRotate(legNum, stepSize, knee = 400):
    servoNum = calculateServoNum(legNum)
    if not stopCheck(s.getDistance()):
        board.bus_servo_set_position(.5, [[servoNum + 1, knee], [servoNum, 500 + stepSize]])

def leftPutDown(legNum, knee = 600):
    servoNum = calculateServoNum(legNum)
    if not stopCheck(s.getDistance()):
        board.bus_servo_set_position(.5, [[servoNum + 1, knee]])

def resetHip(legNum, hip = 500):
    servoNum = calculateServoNum(legNum)
    if not stopCheck(s.getDistance()):
        board.bus_servo_set_position(.5, [[servoNum, hip]])

def resetKnee(legNum, knee = 500):
    servoNum = calculateServoNum(legNum)
    if not stopCheck(s.getDistance()):
        board.bus_servo_set_position(.5, [[servoNum + 1, knee]])

def resetLeftFoot(legNum, foot = 350):
    servoNum = calculateServoNum(legNum)
    if not stopCheck(s.getDistance()):
        board.bus_servo_set_position(1, [[servoNum + 2, foot]])

def resetRightFoot(legNum, foot = 650):
    servoNum = calculateServoNum(legNum)
    if not stopCheck(s.getDistance()):
        board.bus_servo_set_position(1, [[servoNum + 2, foot]])

def initialization ():
    print("Setting Hips")
    resetHip(1)
    resetHip(2)
    resetHip(3)
    time.sleep(1)
    resetHip(4)
    resetHip(5)
    resetHip(6)
    time.sleep(1)
    print("Setting Knees")
    resetKnee(1)
    resetKnee(2)
    resetKnee(3)
    time.sleep(1)
    resetKnee(4)
    resetKnee(5)
    resetKnee(6)
    time.sleep(1)
    print("Setting Feet")
    resetRightFoot(4)
    resetRightFoot(6)
    resetLeftFoot(2)
    time.sleep(1)
    resetRightFoot(5)
    resetLeftFoot(1)
    resetLeftFoot(3)

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
    # time.sleep(.5)
    # resetRightFoot(rightLegNum)
    # resetLeftFoot(leftLegNumOne)
    # resetLeftFoot(leftLegNumTwo)

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
    # time.sleep(.5)
    # resetRightFoot(rightLegNumOne)
    # resetRightFoot(rightLegNumTwo)
    # resetLeftFoot(leftLegNum)

def rotateRight(rotateSize = 230):
    leftLiftAndRotate(1, rotateSize)
    leftLiftAndRotate(3, rotateSize)
    rightLiftAndRotate(5, -rotateSize)
    time.sleep(.5)
    leftPutDown(1)
    leftPutDown(3)
    rightPutDown(5)
    time.sleep(1)
    resetHip(1)
    resetHip(3)
    resetHip(5)  
    time.sleep(1)
    resetKnee(1)
    resetKnee(3)
    resetKnee(5)

def rotateLeft(rotateSize = 230):
    leftLiftAndRotate(2, -rotateSize)
    rightLiftAndRotate(4, rotateSize)
    rightLiftAndRotate(6, rotateSize)
    time.sleep(.5)
    leftPutDown(2)
    rightPutDown(4)
    rightPutDown(6)
    time.sleep(1)
    resetHip(2)
    resetHip(4)
    resetHip(6)  
    time.sleep(1)
    resetKnee(2)
    resetKnee(4)
    resetKnee(6)

# check for stopping 
def stopCheck(distance):
    bounds = 175
    if distance < bounds:
        return True
    else:
        return False
    