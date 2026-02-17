from asn2_grpA import DIRECTION, CSME301Map

from asn2_mapping_helpers import check_directions, turn_to_direction, forward_cell, get_opp_direction

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
            print("Neighbor found!")
            continue
        neighbors.append(k)
    return neighbors

def explore_world(world, robot_info):
    walked_tiles = set()
    explore_from_tile(world, robot_info, walked_tiles)

def explore_from_tile(world, robot_info, walked_tiles):
    # starting info
    i, j, k = robot_info 

    walked_tiles.add((i, j))

    # visit i, j neighbors that are not blocked / already visited
    for neighbor_k in get_neighbors(i, j, world, walked_tiles):
        wall = check_directions(robot_info[2], neighbor_k)
        
        # if there's a wall, record it
        if wall:
            world.setObstacle(i, j, 1, neighbor_k)
            continue

        # otherwise, traverse down from this tile 
        # turn to tile
        turn_to_direction(robot_info[2], neighbor_k)
        robot_info[2] = neighbor_k

        # move forward one tile
        forward_cell()
        robot_info[0], robot_info[1] = get_neighbor(i, j, neighbor_k)

        world.printObstacleMap()
        # recurse 
        explore_from_tile(world, robot_info, walked_tiles)

        # backtrack
        print("Backtracking")

        # go back one cell
        opp_direction = get_opp_direction(robot_info[2])
        turn_to_direction(robot_info[2], opp_direction)
        robot_info[2] = opp_direction

        forward_cell()
        robot_info[0], robot_info[1] = i, j

        # reorient
        turn_to_direction(robot_info[2], k)
        robot_info[2] = k
        
        
if __name__ == '__main__':
    world = CSME301Map(2, 2)
    world.clearObstacleMap()
    robot_info = [0, 0, 3] # we assume the robot starts at 0, 0 facing south
    explore_world(world, robot_info)
    # see how we did
    world.printObstacleMap()