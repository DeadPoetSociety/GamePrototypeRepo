class Space():
    """
    Base class for a space on a game board.
    Contains basic data structures for how a space relates to its neighbors and the board.
    Each has space_id and neighbors regardless of type (e.g. CrystalSpace or AltarSpace)
    space_id -- the integer identifier the game uses to reference this Space
    neighbors -- a list of integers corresponding to the space_id of each of the Space's neighbors.
    """
    space_id = 0
    neighbors = []

    def __init__(self, space_id, neighbors):
        self.space_id = space_id
        self.neighbors = neighbors

class CrystalSpace(Space):
    """
    A space on the board which players fight for control of.
    Contains a dictionary of elements and their current values.
    All elements start at 0 by default.
    """
    elements = None
    district_id = 0
    highest_element = None

    def __init__(self, space_id, neighbors, district_id):
        Space.__init__(self, space_id, neighbors)
        self.elements = {"fire": 0, "water": 0, "wind": 0, "earth": 0, "dark": 0, "light": 0}
        self.district_id = district_id

    def change_element_value(self, element_name, element_difference):
        """
        Changes the named element by the supplied difference.
        element_name -- the element in the space's dictionary' to change.
        element_difference -- will add to the value if positive, and subtract if negative.
        returns the value of the element after change.
        """
        self.elements[element_name] += element_difference
        self.refresh_dominant_element()
        return self.elements[element_name]

    def refresh_dominant_element(self):
        """
        Checks the value of each element and changes the current highest element if it is different.
        """
        highest_value = 0
        new_highest_element = self.highest_element
        for key in self.elements:
            if self.elements[key] > highest_value:
                highest_value = self.elements[key]
                new_highest_element = key
        self.highest_element = new_highest_element

    def __str__(self):
        crystal_space_string = "==============================\n"
        crystal_space_string += "Space Id: " + str(self.space_id) + "\n"
        crystal_space_string += "District: " + str(self.district_id) + "\n"
        if self.highest_element is None:
            crystal_space_string += "Current Highest Element: None\n"
        else:
            crystal_space_string += "Current Highest Element: " + self.highest_element + "\n"
        crystal_space_string += "Elements: \n"
        for key in self.elements:
            crystal_space_string += key + ": " + str(self.elements[key]) + "\n"
        return crystal_space_string


