import utilities


class Empty:
    def __init__(self):
        self.appearance = " "


class Board:
    def __init__(self, width, height):
        self.positions = {}
        self.width = width
        self.height = height
        for x in range(width):
            for y in range(height):
                self.positions[(x, y)] = Empty()

    def __len__(self):
        return len(self.positions)

    def board_print(self):
        for y in range(self.height):
            print_string = ""
            for x in range(self.width):
                print_string += self.positions[(x, y)].appearance
            print(print_string)

board = Board(7, 7)
