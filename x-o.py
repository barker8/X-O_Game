#Board
#Player
#Game

class Board:
    def __init__(self):
        self.board = [' '] * 9

    def to_string(self):
        return '{}|{}|{}\n------\n{}|{}|{}\n------\n{}|{}|{}\n'.format(*self.board)

    def make_move(self, player, place)

class Player:
    def __init__(self, name, marker)
        self.name = name
        self.marker = marker

class Game:
    pass



