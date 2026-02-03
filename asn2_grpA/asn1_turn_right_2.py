
# Tripod: This gait is characterized by a pair of legs, one on each side of the body, 
        # being lifted and moved forward (or backward) simultaneously, followed by 
        # the next pair and so forth, creating a “ripple” effect.
from asn1_movement import makeStep, send_positions
import time

OG_HIP = 500
TURN_HIP = 350
def turnRight():
    # Step 1: Lift and move tripod group A where legs 1 & 3 move forwards & 5 moves backwards 
    step1 = makeStep(
        hip = {1:TURN_HIP, 3:TURN_HIP, 5:TURN_HIP, 2:OG_HIP, 4:OG_HIP, 6:OG_HIP},
        knee = {1:213, 3:220, 5:786}
    )
    send_positions(.3, step1) 
    time.sleep(2)
    
    # Step 2: Put down Tripod Group A
    step2 = makeStep(
        knee = {1: 313, 3: 320, 5: 686},
    )
    send_positions(.2, step2)
    time.sleep(2)
    
    # Step 3: Lift and move tripod group B where legs 2 move forwards & legs 4 & 6 move backwards
    step3 = makeStep(
        hip = {1:OG_HIP, 3:OG_HIP, 5:OG_HIP, 2:TURN_HIP, 4:TURN_HIP, 6:TURN_HIP},
        knee = {2:212, 4:786, 6:786}
    )
    send_positions(.3, step3)
    time.sleep(2)

    # Step 4: Put tripod group B back on the ground
    step4 = makeStep(
        knee = {2: 312, 4: 686, 6: 686},
    )

    send_positions(.2, step4)
    time.sleep(2)

def turnRight90():
    for i in range(4):
        turnRight()
    
    # Return tripod B back to beginning
    step5 = makeStep(
        hip = {2:OG_HIP, 4:OG_HIP, 6:OG_HIP}
    )
    send_positions(.2, step5)

if __name__ == '__main__':  
    turnRight90()
    

            
