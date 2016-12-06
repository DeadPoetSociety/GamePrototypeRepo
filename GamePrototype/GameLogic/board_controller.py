from GameState.board import Board
class board_controller():

    board = None

    def __init__(self):
        self.init_board()

    def init_board(self):
        self.board = Board()

    def update_district(self, space_id, element, value):
        district_id = self.board.spaces[space_id].district_id
        current_controlled = self.get_current_controlled_spaces(element, district_id)
        print("Before: " + str(current_controlled))
        self.board.spaces[space_id].change_element_value(element, value)
        new_controlled = self.get_current_controlled_spaces(element, district_id)
        print("After: " + str(new_controlled))
        controlled_difference = new_controlled - current_controlled
        print("Difference: " + str(controlled_difference))
        self.board.print_spaces()
        if controlled_difference != 0:
            self.propagate_overturn(district_id, element, controlled_difference)
        return value

    def propagate_overturn(self, district_id, element, power):
        current_controlled = self.get_current_controlled_spaces(element, district_id)
        print("Before: " + str(current_controlled))
        for space in self.board.spaces:
            if space.district_id == district_id:
                space.change_element_value(element, pow(2, power) * space.elements[element] - space.elements[element])
        new_controlled = self.get_current_controlled_spaces(element, district_id)
        print("After: " + str(new_controlled))
        controlled_difference = new_controlled - current_controlled
        print("Difference: " + str(controlled_difference))
        self.board.print_spaces()
        if controlled_difference != 0:
            self.propagate_overturn(district_id, element, controlled_difference)

    def get_current_controlled_spaces(self, element, district_id):
        """
        Gets the number of spaces in a district containing the provided space_id which are controlled by the given element.
        """
        current_dominant_spaces = 0
        for space in self.board.spaces:
            if (space.district_id == district_id) and (space.highest_element == element):
                current_dominant_spaces += 1
        return current_dominant_spaces
        