from GameState.space import CrystalSpace

class Board():
    """Contains all methods and data structures necessary for creating and storing a game board."""
    spaces = []
    parsed_layout = None

    def __init__(self):
        import json
        import os
        #print("Current Path: " + os.path.curdir)
        with open(os.path.curdir + "/boards/board1.json") as data_file:
            self.parsed_layout = json.loads(data_file.read())
        self.LoadFromLayout()

    def LoadFromLayout(self):
        self.spaces.append(CrystalSpace(0, [1, 2], 0))
        self.spaces.append(CrystalSpace(1, [0, 2], 0))
        self.spaces.append(CrystalSpace(2, [0, 1], 0))

    def print_spaces(self):
        for space in self.spaces:
            print(space)


