#!/usr/bin/env python3
# Hexagonal Maze for challenge
# Created by RKS, Sept 13th

class HexMaze:
    '''
    A 2D Hexangonal Maze for a lost robot to traverse through.
    '''

    def __init__(self, width=1, height=1):
        """
        Constructor for hexagonal maze

        Arguments:
        int width: the number of horizontal hexs in the Maze
        int height: the number of vertical hex in the Maze
        TODO: Add examples
        """
        # Check if making standard grid
        if (isinstance(width, int) and isinstance(height, int) 
            and width > 0 and height > 0):
            self.width = width
            self.height = height
        else:
            error_str = f"""
                Maze cannot be generated. 
                width: {width}, and height {height} must be integers over 0
                """"
            raise(RuntimeError(error_str))
        
        # Define private strings for generation
        self._corner_strs = ["\ ", " \\", " /", "/ "]
        self._connect_str = "____"



        # Define maze
        self.maze_cols = []
        




    
    def __repr__(self) -> str:
        """
        Return string representation of maze
        """
        hex_list = []


        return "\n".join(hex_list)


class Hex:
    '''
    Representation of single hex block
    '''

    def __init__(self, is_wall=False, is_start=False, is_goal=False):
        '''
        Constructor of Hex Block. Each block has six neighbor arranged in the 
        following pattern

           __2__
        1 /     \\ 3
        6 \\_____/ 4
             5

        Arguments:
            bool is_wall: True is hex block is a wall
            bool is_start: True if hex block is the start (Cannot be wall)
            bool is_goal: True if hex block is goal (Cannot be wall)
        '''
        if(is_wall and (is_start or is_goal)):
            raise RuntimeError("Wall cannot be start or goal")
        self.neighbors = {1:None, 2:None, 3:None, 4:None, 5:None, 6:None}
        self.has_robot = False
        self.is_wall = is_wall
        self.visit_count = 0
        self.is_start = is_start
        self.is_goal = is_goal

    def get_robot_status(self):
        """
        Returns string of robot status for maze
        """
        if(is_wall):
            return "WALL"
        elif(had_robot):
            return "ROBO"
        else:
            return "    "

    def get_hex_status(self):
        """
        Returns string of hex block type for maze
        """
        if(is_wall):
            return "WALL"
        elif(is_goal):
            return "GOAL"
        elif(is_start):
            return "ROOT"
        else:
            return "    "
        



