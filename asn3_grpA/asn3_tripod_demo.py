
# Tripod: This gait is characterized by a pair of legs, one on each side of the body, 
        # being lifted and moved forward (or backward) simultaneously, followed by 
        # the next pair and so forth, creating a “ripple” effect.
from asn3_movement import makeStep, send_positions
import time
from asn3_initialization import initialization
import common.ros_robot_controller_sdk as rrc
from knn import run_knn_combo, run_knn_maze, run_knn_out_maze
from gaussian import run_gaussian_combo, run_gaussian_maze, run_gaussian_out_maze

OG_HIP = 500

board = rrc.Board()
board.enable_reception()

def tripodCycle(hipAdjusts = [0, 0]):
    # Step 1: Lifting and moving forwards Tripod Group A 
    step1 = makeStep(
        hip = {1:350, 3:350, 5:610, 2:495, 4:495, 6:495},
        knee = {1:212, 3:220, 5:786}
    )
    
    send_positions(.2, step1) 
    time.sleep(.2)
    
    # Step 2: Put down Tripod Group A
    step2 = makeStep(
        knee = {1: 312, 3: 320, 5: 686}
    )

    send_positions(.2, step2)
    time.sleep(.2)

    # Step 3: Return Tripod Group A to OG position and lift Tripod Group B
    step3 = makeStep(
        # hip = {1:OG_HIP, 3:OG_HIP, 5:OG_HIP, 2:400 + hipAdjusts[1], 4:620 + hipAdjusts[3], 6:620 + hipAdjusts[5]},
        hip = {1:OG_HIP, 3:OG_HIP, 5:OG_HIP, 2:400, 4:640 + hipAdjusts[0], 6:640 + hipAdjusts[1]},
        knee = {2:212, 4:786, 6:786 }
    )

    send_positions(.2, step3)
    time.sleep(.2)

    # Step 4: Put tripod group B back on the ground
    step4 = makeStep(
        knee = {2:270, 4:693, 6:693}
    )

    send_positions(.2, step4)
    time.sleep(.2)

if __name__ == '__main__':  
    # allow us to read in step size from terminal argument
    while True:
        userInput = input("data type (maze, not maze, combo): ")
        floor_type = userInput.strip()
        if floor_type == "combo":
            maze = input("maze (yes/no): ") == "yes"
            out_maze = input("out_maze (yes/no): ") == "yes"
            out_maze_2 = input("out_maze_2 (yes/no): ") == "yes"

        userInput2 = input("model (knn, gaussian): ")
        userInput3 = input("battery_level: ")
        
        model_type = userInput2.strip()
        batteryLevel = int(userInput3.strip())

        if floor_type == "maze":
            if model_type == "knn":
                model = run_knn_maze()
            else:
                model = run_gaussian_maze()
        elif floor_type == "not maze":
            if model_type == "knn":
                model = run_knn_out_maze()
            else:
                model = run_gaussian_out_maze()
        else:
            
            if model_type == "knn":
                model = run_knn_combo(maze, out_maze, out_maze_2)
            else:
                model = run_gaussian_combo(maze, out_maze, out_maze_2)

        # get battery level in volts
        hipAdjusts = model.predict(batteryLevel)
        print(f"Starting battery level: {batteryLevel}")
        print(f"Starting hipAdjusts: {hipAdjusts}")

        for i in range(20):
            tripodCycle(hipAdjusts)
        time.sleep(1)
        initialization()
