from board import *
from circle_input import *
from cross_input import *


turn = 1
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

# Search for a winner
def check_winner():
    # Check rows
    r1 = board[0]
    r2 = board[1]
    r3 = board[2]

    # Count rows
    count_ro1 = r1.count(1)
    count_ro2 = r2.count(1)
    count_ro3 = r3.count(1)
    count_rx1 = r1.count(2)
    count_rx2 = r2.count(2)
    count_rx3 = r3.count(2)

    # Check column
    c1 = ([i[0] for i in board])
    c2 = ([i[1] for i in board])
    c3 = ([i[2] for i in board])

    # Count column
    count_co1 = c1.count(1)
    count_co2 = c2.count(1)
    count_co3 = c3.count(1)
    count_cx1 = c1.count(2)
    count_cx2 = c2.count(2)
    count_cx3 = c3.count(2)

    # Check diagonal \
    d1 = [board[0][0], board[1][1], board[2][2]]

    # Count diagonal \
    count_do1 = d1.count(1)
    count_dx1 = d1.count(2)

    # Check diagonal /
    d2 = [board[0][2], board[1][1], board[2][0]]

    # Count diagonal /
    count_do2 = d2.count(1)
    count_dx2 = d2.count(2)

    # Full board
    F1 = [board[1][0], board[2][0]] + board[0]
    F2 = [board[1][2], board[2][2]] + board[0]
    F3 = [board[0][2], board[1][2]] + board[2]
    F4 = [board[0][0], board[1][0]] + board[2]
    count_F1 = F1.count(1)
    count_F2 = F2.count(1)
    count_F3 = F3.count(1)
    count_F4 = F4.count(1)

    if count_F1 == 5 or count_F2 == 5 or count_F4 == 5:
        restart = textinput("Player 1 wins!", "Do you want to play again (y/n)")
        if restart.lower() == "n":
            exit()
        else:
            restart_game()
    elif count_F3 == 5:
        restart = textinput("Papajon for ever!", "Do you want to play again (y/n)")
        if restart.lower() == "n":
            exit()
        else:
            restart_game()
    else:
        # 3 in line row
        if count_rx1 == 3 or count_ro1 == 3:
            penup()
            goto(-310,200)
            red_line2()
            game_over()
        elif count_rx2 == 3 or count_ro2 == 3:
            penup()
            goto(-310,0)
            red_line2()
            game_over()
        elif count_rx3 == 3 or count_ro3 == 3:
            penup()
            goto(-310,-200)
            red_line2()
            game_over()

        # 3 in line column
        if count_cx1 == 3 or count_co1 == 3:
            penup()
            goto(-200,310)
            red_line1()
            game_over()
        elif count_cx2 == 3 or count_co2 == 3:
            penup()
            goto(0,310)
            red_line1()
            game_over()
        elif count_cx3 == 3 or count_co3 == 3:
            penup()
            goto(200,310)
            red_line1()
            game_over()

        # 3 in line diagonal \
        if count_dx1 == 3 or count_do1 == 3:
            penup()
            goto(-310,310)
            red_diagonal1()
            game_over()

        # 3 in line diagonal /
        if count_dx2 == 3 or count_do2 == 3:
            penup()
            goto(310,310)
            red_diagonal2()
            game_over()


# Game over promp
def game_over():
    restart = textinput(f"Player {turn} wins!", "Do you want to play again (y/n)")
    if restart.lower() == "n":
        exit()
    else:
        restart_game()


def do_action(cell):
    global turn
    if turn == 1:
        do_circle(cell)  # Rita ring
    else:
        do_cross(cell)  # Rita kryss
    col = int(cell[0]) - 1
    row = int(ord(cell[1])) - 65
    board[row][col] = turn
    check_winner()
    turn = 2 if turn == 1 else 1


# Get mouse click coor
def get_cell(x, y):
    column = row = None
    if -300 < x < -100:
        column = "1"
    elif -100 < x < 100:
        column = "2"
    else:
        column = "3"
    if 300 > y > 100:
        row = "A"
    elif 100 > y > -100:
        row = "B"
    else:
        row = "C"

    if row and column:
        do_action(column + row)

# Restart game
def restart_game():
    reset()
    global turn, board
    turn = 0
    board = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]
    show_board()
    onscreenclick(get_cell)

show_board()
onscreenclick(get_cell)




mainloop()
