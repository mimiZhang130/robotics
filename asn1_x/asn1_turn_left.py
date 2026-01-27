from asn1_movement import makeStep, send_positions
import time

OG_HIP = 500

def turnLeft():
    # Step 1: Lift and move tripod group A where legs 1 & 3 move backwards & 5 moves forwards 
    # & return tripod group B back to OG position
    step1 = makeStep(
        hip = {1:600, 3:600, 5:600, 2:OG_HIP, 4:OG_HIP, 6:OG_HIP},
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

    # Step 3: Lift and move tripod group B where legs 2 move backwards & legs 4 & 6 move forwards
    # & return Tripod Group A to OG position and lift
    step3 = makeStep(
        hip = {1:OG_HIP, 3:OG_HIP, 5:OG_HIP, 2:600, 4:600, 6:600},
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

def turnLeft90():
    for i in range(4):
        turnLeft()

    # Return tripod B back to beginning
    step5 = makeStep(
        hip = {2:OG_HIP, 4:OG_HIP, 6:OG_HIP}
    )
    send_positions(.2, step5)

if __name__ == '__main__':  
    turnLeft90()