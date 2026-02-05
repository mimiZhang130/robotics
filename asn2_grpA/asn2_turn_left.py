from asn2_movement import makeStep, send_positions
import time

OG_HIP = 500
TURN_HIP = 600
TIME_SLEEP = .3
def turnLeft():
    # Step 1: Lift and move tripod group A where legs 1 & 3 move forwards & 5 moves backwards 
    step1 = makeStep(
        hip = {1:TURN_HIP, 3:TURN_HIP, 5:TURN_HIP},
        knee = {1:213, 3:320, 5:686}
    )

    send_positions(.3, step1) 
    time.sleep(TIME_SLEEP)
    
    # Step 2: Put down Tripod Group A
    step2 = makeStep(
        knee = {1: 313, 3: 320, 5: 686}
    )

    send_positions(.2, step2)
    time.sleep(TIME_SLEEP)

    # Step 3: Lift and move tripod group B where legs 2 move forwards & legs 4 & 6 move backwards
    step3 = makeStep(
        hip = {2:TURN_HIP, 4:TURN_HIP, 6:TURN_HIP},
        knee = {2:212, 4:786, 6:786}
    )

    send_positions(.3, step3)
    time.sleep(TIME_SLEEP)

    # Step 4: Put tripod group B back on the ground
    step4 = makeStep(
        knee = {2: 312, 4: 686, 6: 686}
    )
    send_positions(.2, step4)
    time.sleep(TIME_SLEEP)

    # Step 5: Put tripod groups back into position
    step5 = makeStep(
        hip = {1:OG_HIP, 2:OG_HIP, 3:OG_HIP, 4:OG_HIP, 5:OG_HIP, 6:OG_HIP}
    )
    send_positions(.2, step5)
    time.sleep(TIME_SLEEP)

def turnLeft90():
    for i in range(4):
        turnLeft()

if __name__ == '__main__':  
    turnLeft90()