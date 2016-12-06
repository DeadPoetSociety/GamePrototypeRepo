from GameLogic.board_controller import board_controller
from GameState.space import CrystalSpace

board_controller = board_controller()
board_controller.board.print_spaces()
board_controller.update_district(0,"fire",10)
board_controller.update_district(1,"earth",10)
board_controller.update_district(1,"fire",11)

def trythis():
    test_list = []
    test_list.append(CrystalSpace(0, [1,2], 0))
    test_list.append(CrystalSpace(1, [1,2], 0))
    test_list.append(CrystalSpace(2, [1,2], 0))
    #test_list[0].change_element_value("fire", 100)
    board_controller.update_district(0,"fire",100)
    for space in test_list:
        print(space)

#trythis()