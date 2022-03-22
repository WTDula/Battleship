class Ship:
    def __init__(self, name, spaces, position = []):
        self.name = name
        self.spaces = spaces
        self.is_sunk = False
        self.position = position

    def placed_valid(self, position):
        # return true if ship is placed in valid position -> 
        # not diagonally, no other ships in position, enough room on board
        pass

    