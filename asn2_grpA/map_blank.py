#!/usr/bin/env python
import sys

# Usage:
#
# #Create object
# your_map = CSME301Map()
#
# #Use Object (examples)
# your_map.printObstacleMap()
# your_map.clearObstacleMap()
# your_map.printCostMap()
# isBlocked = your_map.getObstacle(3, 4, DIRECTION.North)
# cell_cost = your_map.getCost(3, 4)

def enum(**enums):
    return type('Enum', (), enums)

DIRECTION = enum(North=1, East=2, South=3, West=4)

class CSME301Map():
    def __init__(self):

        n_row = 8
        n_col = 8

        self.obstacle_size_row = n_row
        self.obstacle_size_col = n_col
        self.costmap_size_row = n_row
        self.costmap_size_col = n_col

        self.horizontalWalls = [[0 for x in range(n_col)] for x in range(n_row+1)]
        self.verticalWalls = [[0 for x in range(n_col+1)] for x in range(n_row)]
        self.costMap = [[0 for x in range(n_col)] for x in range(n_row)]

        for i in range(n_row):
            for j in range(n_col):
                self.costMap[i][j] = 0


    # ================= OBSTACLE FUNCTIONS =================
    # ***********************************************************************
    # Function Name : getNeighborObstacle
    # Description   : Checks if the neighboring cell is blocked on the map.
    # Input         : i: The row coordinate of the current cell on the map.
    #               : j: The column coordinate of the current cell on the map
    #               : dir: A Direction enumeration (North, South, East, West)
    #               :      indicating which neighboring cell to check for
    #               :      obstacles
    # Output        : None
    # Return        : 1 if neighboring cell is blocked, 0 if neighboring cell
    #               : is clear, -1 if index i or j is out of bounds
    # ***********************************************************************/
    def getNeighborObstacle(self, i, j, dir):
        if (i < 0 or i >= self.costmap_size_row) or (j < 0 or j >= self.costmap_size_col):
            print("ERROR (getNeighborObstacle): index out of range")
            return -1

        if dir == DIRECTION.North:
            return self.horizontalWalls[i][j]

        elif dir == DIRECTION.South:
            return self.horizontalWalls[i+1][j]

        elif dir == DIRECTION.West:
            return self.verticalWalls[i][j]

        elif dir == DIRECTION.East:
            return self.verticalWalls[i][j+1]

        return 0

    # ******************************************************************************
    # Function Name  : setObstacle
    # Description    : Used for map building, sets the obstacle status of a given map cell
    # Input          : i: The row coordinate of the current cell on the map.
    #                : j: The column coordinate of the current cell on the map
    #                : isBlocked: A boolean (0 or 1) value indicated if the cell is blocked
    #                : dir: A Direction enumeration (North, South, East, West) indicating
    #                :      which neighboring cell to set for obstacles
    # Output         : None
    # Return         : 0 if successful, -11 if i or j is out of map bounds, -2 if isBlocked is not 0 or 1
    # *****************************************************************************/
    def setObstacle(self, i, j, isBlocked, dir):
        if (i < 0 or i >= self.obstacle_size_row) or (j < 0 or j >= self.obstacle_size_col):
            print("ERROR (setObstacle): index out of range")
            return -1
        if isBlocked not in [0, 1]:
            print("ERROR (setObstacle): isBlocked must be 0 or 1")
            return -2

        if dir == DIRECTION.North:
            self.horizontalWalls[i][j] = isBlocked
        elif dir == DIRECTION.South:
            self.horizontalWalls[i+1][j] = isBlocked
        elif dir == DIRECTION.West:
            self.verticalWalls[i][j] = isBlocked
        elif dir == DIRECTION.East:
            self.verticalWalls[i][j+1] = isBlocked

        return 0

    # ******************************************************************************
    # Function Name  : clearObstacleMap
    # Description    : Sets all of the values in the obstacle map to 0
    # Input          : None
    # Output         : None
    # Return         : None
    # *****************************************************************************/
    def clearObstacleMap(self):
        for i in range(self.costmap_size_row):
            for j in range(self.costmap_size_col + 1):
                self.verticalWalls[i][j] = 0

        for i in range(self.costmap_size_row + 1):
            for j in range(self.costmap_size_col):
                self.horizontalWalls[i][j] = 0


    # ================= COST FUNCTIONS =================
    # ******************************************************************************
    # Function Name  : getNeighborCost
    # Description    : Retrieves the calculated cost of a neighboring cell on the map.
    # Input          : i: The row coordinate of the current cell on the map.
    #                : j: The column coordinate of the current cell on the map
    #                : dir: A Direction enumeration (North, South, East, West) indicating
    #                :      which neighboring cell to retrieve the cost.
    # Output         : None
    # Return         : Positive float valued cost for the neighboring cell, -1 on error
    # *****************************************************************************/
    def getNeighborCost(self, i, j, dir):
        if (i < 0 or i > (self.costmap_size_row - 1) or j < 0 or j > (self.costmap_size_col - 1)):
            print("ERROR (getNeighborCost): index out of range")
            return -1

        cellValue = 0
        if dir == DIRECTION.North:
            if (i == 0):
                cellValue = 1000
            else:
                cellValue = self.costMap[i-1][j]
        elif dir == DIRECTION.South:
            if(i == (self.costmap_size_row - 1)):
                cellValue = 1000
            else:
                cellValue = self.costMap[i+1][j]
        elif dir == DIRECTION.West:
            if (j == 0):
                cellValue = 1000
            else:
                cellValue = self.costMap[i][j-1]
        elif dir == DIRECTION.East:
            if (j == (self.costmap_size_col - 1)):
                cellValue = 1000
            else:
                cellValue = self.costMap[i][j+1]

        return cellValue

    # ******************************************************************************
    # Function Name  : setNeighborCost
    # Description    : Sets the calculated cost of a neighboring cell on the map.
    # Input          : i: The row coordinate of the current cell on the map.
    #                : j: The column coordinate of the current cell on the map
    #                : dir: A Direction enumeration (North, South, East, West) indicating
    #                :      which neighboring cell to retrieve the cost.
    #                : val: Positive float valued cost for the neighboring cell
    # Output         : None
    # Return         : None
    # *****************************************************************************/
    def setNeighborCost(self, i, j, dir, val):
        if (i < 0 or i > (self.costmap_size_row - 1) or j < 0 or j > (self.costmap_size_col - 1)):
            print("ERROR (setNeighborCost): index out of range, value not set")
            return

        if dir == DIRECTION.North:
            if (i > 0):
                self.costMap[i-1][j] = val
        elif dir == DIRECTION.South:
            if (i < (self.costmap_size_row - 1)):
                self.costMap[i+1][j] = val
        elif dir == DIRECTION.West:
            if (j > 0):
                self.costMap[i][j-1] = val
        elif dir == DIRECTION.East:
            if (j < (self.costmap_size_col - 1)):
                self.costMap[i][j+1] = val

    # ******************************************************************************
    # Function Name  : setCost
    # Description    : Used for map building, sets the calculated cost of a given map cell
    # Input          : i: The row coordinate of the current cell on the map.
    #                : j: The column coordinate of the current cell on the map
    #                : val: An integer value (0 to 1023) indicated the cost of a map cell
    # Output         : None
    # Return         : 0 if successful, -1 if i or j is out of map bounds
    # *****************************************************************************/
    def setCost(self, i, j, val):
        if (i < 0 or i >= self.costmap_size_row) or (j < 0 or j >= self.costmap_size_col):
            print("ERROR (setCost): index out of range")
            return -1

        self.costMap[i][j] = val
        return 0

    # ******************************************************************************
    # Function Name  : getCost
    # Description    : Used for map building, gets the calculated cost of a given map cell
    # Input          : i: The row coordinate of the current cell on the map.
    #                : j: The column coordinate of the current cell on the map
    # Output         : None
    # Return         : cost >= 0 if successful, -1 if i or j is out of map bounds
    # *****************************************************************************/
    def getCost(self, i, j):
        if (i < 0 or i >= self.costmap_size_row) or (j < 0 or j >= self.costmap_size_col):
            print("ERROR (getCost): index out of range")
            return -1

        return self.costMap[i][j]

    # ******************************************************************************
    # Function Name  : clearCostMap
    # Description    : Sets all of the values in the cost map to 0
    # Input          : None
    # Output         : None
    # Return         : None
    # *****************************************************************************/
    def clearCostMap(self):
        for i in range(self.costmap_size_row):
            for j in range(self.costmap_size_col):
                self.costMap[i][j] = 0


    # ================= PRINT FUNCTIONS =================
    # ******************************************************************************
    # Function Name  : printObstacleMap
    # Description    : When connected to a terminal, will print out the 4x6 obstacle map
    # Input          : None
    # Output         : None
    # Return         : None
    # *****************************************************************************/
    def printObstacleMap(self):
        print("Obstacle Map: ")
        for i in range(self.obstacle_size_row):
            # print horizontal walls (top of row)
            for j in range(self.obstacle_size_col):
                if self.horizontalWalls[i][j] == 0:
                    sys.stdout.write("    ")
                else:
                    sys.stdout.write(" ---")
            print()

            # print vertical walls and cells
            for j in range(self.obstacle_size_col):
                # Left wall
                if self.verticalWalls[i][j] == 0:
                    sys.stdout.write("  O ")
                else:
                    sys.stdout.write("| O ")

            # rightmost boundary wall
            if self.verticalWalls[i][self.obstacle_size_col] == 1:
                sys.stdout.write("|")

            print(" ")

        # print bottom horizontal walls
        for j in range(self.obstacle_size_col):
            if self.horizontalWalls[self.obstacle_size_row][j] == 0:
                sys.stdout.write("    ")
            else:
                sys.stdout.write(" ---")
        print(" ")

    # ******************************************************************************
    # Function Name  : printCostMap
    # Description    : When connected to a terminal, will print out the 4x6 cost map
    # Input          : None
    # Output         : None
    # Return         : None
    # *****************************************************************************/
    def printCostMap(self):
        print("Cost Map:")
        for i in range(self.costmap_size_row):
            for j in range(self.costmap_size_col):
                print(str(self.costMap[i][j]), end=" "),
            # from IPython import embed; embed()

            print(" ")

    # =================== OTHER FUNCTIONS ===================
    # ******************************************************************************
    # Function Name  : getCostmapSize
    # Description    : Retrieve the size of a given dimension of the costmap
    # Input          : bool rowDim (true for row dimension, false for column dimension)
    # Output         : None
    # Return         : costmap size in the requested dimension
    # *****************************************************************************/
    def getCostmapSize(self, rowDim):
        if (rowDim):
            return self.costmap_size_row
        else:
            return self.costmap_size_col

    # ******************************************************************************
    # Function Name  : getObstacleMapSize
    # Description    : Retrieve the size of a given dimension of the Obstacle Map
    # Input          : bool rowDim (true for row dimension, false for col dimension)
    # Output         : None
    # Return         : obstacle map size in the requested dimension
    # *****************************************************************************/
    def getObstacleMapSize(self, rowDim):
        if rowDim:
            return self.obstacle_size_row
        else:
            return self.obstacle_size_col


# ================= TEST =================

def main():
    your_map = CSME301Map()

    print("Initial (no walls):")
    your_map.printObstacleMap()

    # Add some walls
    # your_map.setObstacle(3, 3, 1, DIRECTION.North)
    # your_map.setObstacle(3, 3, 1, DIRECTION.East)
    # your_map.setObstacle(3, 3, 1, DIRECTION.South)
    # your_map.setObstacle(3, 3, 1, DIRECTION.West)
    your_map.setObstacle(2, 2, 1, DIRECTION.North)

    print("After adding walls around:")
    your_map.printObstacleMap()


if __name__ == "__main__":
    main()