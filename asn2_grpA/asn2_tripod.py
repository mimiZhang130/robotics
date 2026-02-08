
# Tripod: This gait is characterized by a pair of legs, one on each side of the body, 
        # being lifted and moved forward (or backward) simultaneously, followed by 
        # the next pair and so forth, creating a “ripple” effect.
from asn2_movement import makeStep, send_positions
import time

OG_HIP = 500

def tripodCycle(hipAdjusts = [0, 0, 0, 0, 0, 0]):
    # Step 1: Lifting and moving forwards Tripod Group A 
    step1 = makeStep(
        hip = {1:380 + hipAdjusts[0], 3:380 + hipAdjusts[2], 5:600 + hipAdjusts[4], 2:OG_HIP, 4:OG_HIP, 6:OG_HIP},
        knee = {1:200, 3:200, 5:700}
    )
    
    send_positions(.3, step1) 
    time.sleep(.3)
    
    # Step 2: Put down Tripod Group A
    step2 = makeStep(
        knee = {1: 313, 3: 320, 5: 686}
    )

    send_positions(.2, step2)
    time.sleep(.3)


    # Step 3: Return Tripod Group A to OG position and lift Tripod Group B
    step3 = makeStep(
        # hip = {1:OG_HIP, 3:OG_HIP, 5:OG_HIP, 2:400 + hipAdjusts[1], 4:620 + hipAdjusts[3], 6:620 + hipAdjusts[5]},
        hip = {1:OG_HIP, 3:OG_HIP, 5:OG_HIP, 2:400 + hipAdjusts[1], 4:635 + hipAdjusts[3], 6:635 + hipAdjusts[5]},
        knee = {2:180, 4:780, 6:750 }
    )

    send_positions(.3, step3)
    time.sleep(.3)

    # Step 4: Put tripod group B back on the ground
    step4 = makeStep(
        knee = {2:270, 4:690, 6:690}
    )

    send_positions(.2, step4)
    time.sleep(.3)

if __name__ == '__main__':  
    # allow us to read in step size from terminal argument
    while True:
        tripodCycle()
