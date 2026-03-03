from map_blank import DIRECTION, CSME301Map

from asn2_mapping_helpers import check_directions, turn_to_direction, forward_cell, get_opp_direction
from asn2_initialization import initialization

# given original i, j of cell, find neighbor that is in k direction
def get_neighbor(i, j, k):
    match (k):
        case DIRECTION.North:
            return (i - 1, j)
        case DIRECTION.East:
            return (i, j + 1)
        case DIRECTION.South:
            return (i + 1, j)
        case DIRECTION.West:
            return (i, j - 1)

# given original i, j of cell & new i, j of goal cell, find k to get to that
def get_dir_from_neighbor(og_i, og_j, new_i, new_j):
    # going to stay the same
    if (og_i == new_i and og_j == new_j):
        return -1
    
    # going to be E or W
    if og_i == new_i:
        if og_j - new_j == 1:
            return DIRECTION.West
        else:
            return DIRECTION.East
    # going to be N or S 
    if og_j == new_j:
        if og_i - new_i == 1:
            return DIRECTION.North
        else:
            return DIRECTION.South
    print("should never reach here")
    return -1

# get directions of neighbors that are not visited / do not already have an obstacle set
def get_neighbors(i, j, world, walked_tiles):
    neighbors = []
    for k in range(1, 5):
        if world.getNeighborObstacle(i, j, k) == True:
            print("Obstacle recorded: " + str(k))
            continue
        check_neighbor = get_neighbor(i, j, k)
        print("Check neighbor: " + str(check_neighbor[0]) + ", " + str(check_neighbor[1]))
        if check_neighbor in walked_tiles:
            print("Neighbor found in walked tiles!")
            continue
        neighbors.append(k)
    return neighbors

def explore_world(world, robot_info):
    walked_tiles = set()
    
    stack = []
    # backtrack = []

    # starting info
    i, j, k = robot_info 
    
    # backtrack.append([i, j, k])
    stack.append([i, j, k])

    # stack still has cells to visit 
    while stack:
        goal_i, goal_j, goal_k = stack[-1]
        
        world.printObstacleMap()
        
        # if we're not at the goal tile, get there
        if (not (robot_info[0] == goal_i and robot_info[1] == goal_j)):
            # turn to tile
            print(f"Turn to get to goal tile... from {robot_info[2]} to {goal_k}")
            turn_to_direction(robot_info[2], goal_k)
            robot_info[2] = goal_k

            # move forward one tile
            forward_cell()
            robot_info[0], robot_info[1] = get_neighbor(robot_info[0], robot_info[1], goal_k)

        print(f"visit cell: {robot_info[0]}, {robot_info[1]}")
        i, j = robot_info[0], robot_info[1]

        # visit cell
        walked_tiles.add((i, j))
        
        # get neighbors of cell
        neighbors = get_neighbors(i, j, world, walked_tiles)
        
        if neighbors:
            for neighbor_k in neighbors:
                wall, robot_info[2] = check_directions(robot_info[2], neighbor_k)
                if wall:
                    print(f"there's a wall: {neighbor_k}")
                    world.setObstacle(i, j, 1, neighbor_k)
                    continue

                n_i, n_j = get_neighbor(i, j, neighbor_k)
                print(f"adding neighbor to stack: {n_i}, {n_j}, {neighbor_k}")
                stack.append([n_i, n_j, neighbor_k])
                break
            
        # if no neighbors, we should backtrack and return to when there were neighbors
        else:
            stack.pop()

            if stack:
                # get previous cell
                prev_i, prev_j, prev_k = stack[-1]
                print(f"prev_i: {prev_i}, prev_j: {prev_j}, prev_k: {prev_k}")
                # backtrack
                print("Backtracking now...")

                # go back one cell
                opp_direction = get_dir_from_neighbor(robot_info[0], robot_info[1], prev_i, prev_j)
                if opp_direction != -1:
                    print(f"Turned to backtrack... from {robot_info[2]} to {opp_direction}")
                    turn_to_direction(robot_info[2], opp_direction)
                    robot_info[2] = opp_direction
        
                forward_cell()
                robot_info[0], robot_info[1] = prev_i, prev_j

if __name__ == '__main__':
    initialization()
    world = CSME301Map()
    world.clearObstacleMap()
    robot_info = [0, 0, 1] # we assume the robot starts at 0, 0 facing north
    explore_world(world, robot_info)
    # see how we did
    world.printObstacleMap()