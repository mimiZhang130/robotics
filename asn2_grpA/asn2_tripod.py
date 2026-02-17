
# Tripod: This gait is characterized by a pair of legs, one on each side of the body, 
        # being lifted and moved forward (or backward) simultaneously, followed by 
        # the next pair and so forth, creating a “ripple” effect.
from asn2_movement import makeStep, send_positions
from asn2_movement import sensor_right, sensor_left, sensor_reset
import time
import sonar

OG_HIP = 500
s = sonar.Sonar()

def tripodCycle(hipAdjusts = [0, 0, 0, 0, 0, 0]):
    # Step 1: Lifting and moving forwards Tripod Group A 
    step1 = makeStep(
        hip = {1:350 + hipAdjusts[0], 3:350 + hipAdjusts[2], 5:610 + hipAdjusts[4], 2:495, 4:495, 6:495},
        knee = {1:212, 3:220, 5:786}
    )
    
    send_positions(.3, step1) 
    time.sleep(.3)
    
    # Step 2: Put down Tripod Group A
    step2 = makeStep(
        knee = {1: 312, 3: 320, 5: 686}
    )

    send_positions(.2, step2)
    time.sleep(.3)

    # Step 3: Return Tripod Group A to OG position and lift Tripod Group B
    step3 = makeStep(
        # hip = {1:OG_HIP, 3:OG_HIP, 5:OG_HIP, 2:400 + hipAdjusts[1], 4:620 + hipAdjusts[3], 6:620 + hipAdjusts[5]},
        hip = {1:OG_HIP, 3:OG_HIP, 5:OG_HIP, 2:400 + hipAdjusts[1], 4:640 + hipAdjusts[3], 6:640 + hipAdjusts[5]},
        knee = {2:212, 4:786, 6:786 }
    )

    send_positions(.3, step3)
    time.sleep(.3)

    # Step 4: Put tripod group B back on the ground
    step4 = makeStep(
        knee = {2:270, 4:690, 6:690}
    )

    send_positions(.2, step4)
    time.sleep(.3)

def strafeLeft(cycles=1, magnitude=15):
    for i in range(cycles):
        hip_adjusts = [
            magnitude,  # left legs
            magnitude, 
            magnitude,  
            -magnitude,  # right legs
            -magnitude,  
            -magnitude   
        ]
        tripodCycle(hipAdjusts=hip_adjusts)

def strafeRight(cycles=1, magnitude=15):
    for _ in range(cycles):
        hip_adjusts = [
            -magnitude,  # left legs
            -magnitude,
            -magnitude,
            magnitude,  # right legs
            magnitude,
            magnitude
        ]
        tripodCycle(hipAdjusts=hip_adjusts)

def recenter():
    tolerance = 5

    # Look right
    sensor_right()
    time.sleep(.5)
    right_dist = s.getDistance()

    # Look left
    sensor_left()
    time.sleep(.5)
    left_dist = s.getDistance()

    # Reset sensor to forward
    sensor_reset()

    # Compute lateral offset
    offset = right_dist - left_dist

    print("Left:", left_dist)
    print("Right:", right_dist)
    print("Center error:", offset)

    # If right is larger, we are too close to left wall
    if (left_dist > 500) or (right_dist > 500):
        pass
    elif offset > tolerance:
        strafeRight(cycles=1)
    elif offset < -tolerance:
        strafeLeft(cycles=1)


if __name__ == '__main__':  
    # allow us to read in step size from terminal argument
    while True:
        tripodCycle()
