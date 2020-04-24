import sys

board = ["1", "2", "3",
         "4", "5", "6",
         "7", "8", "9"]


def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])


display_board()
player1 = input("enter the player 1 name")
player2 = input("enter the player 2 name")


def turn():
    i = 0
    t=1
    while i < 9:
        if(i%2==0):
         position = input(player1+"enter your position")
         position = int(position) - 1
        if (i % 2 != 0):
            position = input(player2 + "enter your position")
            position = int(position) - 1
        if (board[position] == "X" or board[position] == "O"):
            print("position accuried try another position")
            i = i - 1
        if i % 2 == 0:
            board[position] = "X"
        else:
            board[position] = "O"
        display_board()
        i = i + 1
        # HORIZONTAL_CHECK
        if (board[0] == "X" and board[1] == "X" and board[2] == "X"):
            print("congrats  " + player1 + "    you won")
            t=1
            sys.exit()
        if (board[0] == "O" and board[1] == "O" and board[2] == "O"):
            print("congrats  " + player2 + "    you won")
            t = 1
            sys.exit()
        if (board[3] == "X" and board[4] == "X" and board[5] == "X"):
            print("congrats  " + player1 + "    you won")
            t = 1
            sys.exit()
        if (board[3] == "O" and board[4] == "O" and board[5] == "O"):
            print("congrats  " + player2 + "    you won")
            t = 1
            sys.exit()
        if (board[6] == "X" and board[7] == "X" and board[8] == "X"):
            print("congrats  " + player1 + "    you won")
            t = 1
            sys.exit()
        if (board[6] == "O" and board[7] == "O" and board[8] == "O"):
            print("congrats  " + player2 + "    you won")
            t = 1
            sys.exit()
        # VERTICAL_CHECK
        if (board[0] == "X" and board[3] == "X" and board[6] == "X"):
            print("congrats  " + player1 + "    you won")
            t = 1
            sys.exit()
        if (board[0] == "O" and board[3] == "O" and board[6] == "O"):  # vertical check :)
            print("congrats  " + player2 + "    you won")
            t = 1
            sys.exit()
        if (board[1] == "X" and board[4] == "X" and board[7] == "X"):
            print("congrats  " + player1 + "    you won")
            t = 1
            sys.exit()
        if (board[1] == "O" and board[4] == "O" and board[7] == "O"):
            print("congrats  " + player2 + "    you won")
            t = 1
            sys.exit()
        if (board[2] == "X" and board[5] == "X" and board[8] == "X"):
            print("congrats  " + player1 + "    you won")
            t = 1
            sys.exit()
        if (board[2] == "O" and board[5] == "O" and board[8] == "O"):
            print("congrats  " + player2 + "    you won")
            t = 1
            sys.exit()
        # diagonal
        if (board[0] == "X" and board[4] == "X" and board[8] == "X" or
                board[2] == "X" and board[4] == "X" and board[6] == "X"):
            print("congrats  " + player1 + "    you won")
            t = 1
            sys.exit()
        if (board[0] == "O" and board[4] == "O" and board[8] == "O" or
                board[0] == "O" and board[4] == "O" and board[6] == "O"):
            print("congrats  " + player2 + "    you won")
            t = 1
            sys.exit()
    if(t==1):
        print("sorry match got tied")

turn()
