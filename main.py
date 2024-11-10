import objects
from objects import PlayerThing

levels = [(7, 5, "TODO: Level System")]
board = objects.board.board


class YouQuitNow(Exception):
    pass


def player_move_function(x_add, y_add):
    for index in range(len(board)):
        if board[board[index]] is PlayerThing:
            board[board[index]].move(x_add, y_add)


def other_stuff_move():
    pass


def turn():
    board.board_print()
    player_move = input("Where to move? (WASD to move, nowhere to wait, bye to quit) ")
    if player_move.lower() == "w":
        player_move_function(0, 1)
    elif player_move.lower() == "s":
        player_move_function(0, -1)
    elif player_move.lower() == "d":
        player_move_function(1, 0)
    elif player_move.lower() == "a":
        player_move_function(-1, 0)
    elif player_move.lower() == "nowhere":
        pass
    elif player_move.lower() == "bye" or player_move.lower() == "byebye":
        raise YouQuitNow("Thanks for playing!")
    else:
        print("That's not an option...")
        turn()
    other_stuff_move()
