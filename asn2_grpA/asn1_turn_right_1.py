
# Tripod: This gait is characterized by a pair of legs, one on each side of the body, 
        # being lifted and moved forward (or backward) simultaneously, followed by 
        # the next pair and so forth, creating a “ripple” effect.
from asn1_movement import makeStep, send_positions
import time

OG_HIP = 500

def turnRight():
    # Step 1: Lift and move tripod group A where legs 1 & 3 move forwards & 5 moves backwards 
    step1 = makeStep(
        hip = {1:400, 3:400, 5:400},
        knee = {1:200, 3:200, 5:700}
    )

    send_positions(.3, step1) 
    time.sleep(.3)
    
    # Step 2: Put down Tripod Group A
    step2 = makeStep(
        knee = {1: 280, 3:280, 5:650}
    )

    send_positions(.2, step2)
    time.sleep(.3)

    # Step 3: Lift and move tripod group B where legs 2 move forwards & legs 4 & 6 move backwards
    step3 = makeStep(
        hip = {2:400, 4:400, 6:400},
        knee = {2:180, 4:780, 6:750}
    )

    send_positions(.3, step3)
    time.sleep(.3)

    # Step 4: Put tripod group B back on the ground
    step4 = makeStep(
        knee = {2:270, 4:690, 6:690}
    )
    send_positions(.2, step4)
    time.sleep(.3)

    # Step 5: Put tripod groups back into position
    step5 = makeStep(
        hip = {1:OG_HIP, 2:OG_HIP, 3:OG_HIP, 4:OG_HIP, 5:OG_HIP, 6:OG_HIP}
    )
    send_positions(.2, step5)
    time.sleep(.3)

def turnRight90():
    for i in range(4):
        turnRight()    
    

if __name__ == '__main__':  
    turnRight90()
    

            
