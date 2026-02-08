# Importing set directions (k) and map
from asn2_grpA import DIRECTION, CSME301Map
# https://docs.python.org/3/library/heapq.html
from heapq import *
from asn2_grpA_localization_testing import runActions

# parse user input into a dict with i, j, k values
def userInput(prompt):
    # Inputs the string as 0 0 1 for example
    raw_str = input(prompt)
    parts = raw_str.split()

    i = int(parts[0])
    j = int(parts[1])
    k = int(parts[2])

    return (i, j, k)

# set the cost of each grid cell.
def setCostGrid():
    default_cost = 1
    for i in range(map.getCostmapSize(True)):
        for j in range(map.getCostmapSize(False)):
            map.setCost(i, j, default_cost)

# generate a path from xs to xg
def h(start, end):
    action, heading_cost = calc_neighbor_cost_and_action(end[2], start[2])
    return abs(end[0] - start[0]) + abs(end[1] - start[1]) + heading_cost

# if turn left or right, penalize 1 | if turn 180, penalize 2 | if turn 0, penalize 0
def calc_neighbor_cost_and_action(new_k, k, only_turn = False):
    heading_change = (new_k + 4 - k) % 4
    action = ''
    if heading_change == 0:
        cost = 0
    if heading_change == 1:
        cost = 1
        action += 'R'
    if heading_change == 2:
        cost = 2
        action += 'B'
    if heading_change == 3:
        cost = 1
        action += 'L'

    if not only_turn:
        action += 'F'
    
    return (action, cost)

# return neighbors of a cell
def get_neighbors(curr_cell):
    i, j, k = curr_cell
    neighbors = []

    for new_k in range(1, 5):
        if (map.getNeighborObstacle(i, j, new_k) == 0): # valid neighbor
            match new_k:
                case(DIRECTION.North): 
                    new_i, new_j = i - 1, j
                case(DIRECTION.East): 
                    new_i, new_j = i, j + 1
                case(DIRECTION.South): 
                    new_i, new_j = i + 1, j
                case(DIRECTION.West):
                    new_i, new_j = i, j - 1

            action, cost = calc_neighbor_cost_and_action(new_k, k)
        
            neighbors.append(((new_i, new_j, new_k), action, cost))

        action, cost = calc_neighbor_cost_and_action(new_k, k, True) 
        neighbors.append(((i, j, new_k), action, cost))              
    return neighbors

# f(n) = g(n) + h(n)
def a_star(x_s, x_g):
    not_seen_heap = []
    
    s_cost = 0 + h(x_s, x_g)
    heappush(not_seen_heap, (s_cost, x_s))
    seen = [] # set of seen cells
    g_scores = {x_s: 0}
    path_tracker = {} # keeps track of previous cell & action to take from previous cell
    
    while not_seen_heap:
        curr_f_score, curr_cell = heappop(not_seen_heap)

        if curr_cell == x_g:
            return build_path(x_s, x_g, path_tracker)
        
        seen.append(curr_cell)

        # check each neighbor
        for neighbor, action, cost in get_neighbors(curr_cell):
            if neighbor in seen:
                continue
            
            g_score = g_scores[curr_cell] + cost
            
            # if we haven't visited the neighbor or the g_score is better, update g_score and push onto heap
            if neighbor not in g_scores or g_score < g_scores[neighbor]:
                g_scores[neighbor] = g_score
                f_score = g_score + h(neighbor, x_g)
                heappush(not_seen_heap, (f_score, neighbor))
                seen.append(neighbor)
                path_tracker[neighbor] = (curr_cell, action)
                # TODO: NOT SURE IF I'VE CAUGHT UP
                map.setCost(neighbor[0], neighbor[1], g_score)

    print("FAILED IF WE REACHED HERE :(")

# generate a command sequence to achieve your path
def build_path(x_s, x_g, path_tracker):
    path = []
    curr = x_g
    while curr in path_tracker:
        prev_cell, action = path_tracker[curr]
        path.append((prev_cell, action))
        curr = prev_cell
        # print(prev_cell)

    path.reverse()
    # print(path)
    build_action_list(path, x_s)

# build action string based on build_path
def build_action_list(path, x_s):
    actions = '' 
    for prev_cell, action in path:
        actions += action
    
    robot_info = [x_s[2], [x_s[0], x_s[1]]]
    # print(actions)
    runActions(actions, robot_info)

# walk the path following the command sequence
if __name__ == '__main__':
    # accept a starting position xs and an ending position xg from the command line
    x_s = userInput("x_s/Starting Position (i j k): ")
    x_g = userInput("\n x_g/Ending Position (i j k): ")

    # initialize map
    map = CSME301Map()
    map.printObstacleMap()

    # create cost map
    setCostGrid()
    # map.setCost(x_s['i'], x_s['j'], 0)

    # generate a path from xs to xg
    a_star(x_s, x_g)

    # print cost map
    map.printCostMap()

