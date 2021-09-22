"""

A simple tic tac toe terminal program I made for the first solo project in codeacademy.

Mainly was made to get familiar with git terminal commands.

"""

playing_board = {'1': ' ' , '2': ' ' , '3': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '7': ' ' , '8': ' ' , '9': ' ' }


def game():
    new_game = input("Welcome to Tic Tac Toe! Press 1 if you would like to play. Press 2 if you would like to know how to play. Press 3 if you would like to exit the program.")
    if new_game == "1":
        moves = 0
        turn = "X"
        
        for i in range(10):
            print_board(playing_board)
            print("It is {}'s turn. Where would you like to place your move?".format(turn))
            move = input()

            if playing_board[move] == " ":
                playing_board[move] = turn
                moves += 1
            else:
                print("That spot is already taken")
                continue
            
            if moves > 4:
                if playing_board["1"] == playing_board["2"] == playing_board["3"] != " ":
                    print_board(playing_board)
                    print(turn + " won! Congratulations!")
                    break

                elif playing_board["4"] == playing_board["5"] == playing_board["6"] != " ":
                    print_board(playing_board)
                    print(turn + " won! Congratulations!")
                    break

                elif playing_board["7"] == playing_board["8"] == playing_board["9"] != " ":
                    print_board(playing_board)
                    print(turn + " won! Congratulations!")
                    break

                elif playing_board["1"] == playing_board["4"] == playing_board["7"] != " ":
                    print_board(playing_board)
                    print(turn + " won! Congratulations!")
                    break

                elif playing_board["2"] == playing_board["5"] == playing_board["8"] != " ":
                    print_board(playing_board)
                    print(turn + " won! Congratulations!")
                    break

                elif playing_board["3"] == playing_board["6"] == playing_board["9"] != " ":
                    print_board(playing_board)
                    print(turn + " won! Congratulations!")
                    break

                elif playing_board["1"] == playing_board["5"] == playing_board["9"] != " ":
                    print_board(playing_board)
                    print(turn + " won! Congratulations!")
                    break

                elif playing_board["3"] == playing_board["5"] == playing_board["7"] != " ":
                    print_board(playing_board)
                    print(turn + " won! Congratulations!")
                    break
            
            if moves == 9:
                print("It was a tie!")
                break
                
            if turn == "X":
                turn = "O"
            else:
                turn = "X"
        reset_board(playing_board)
        game()

    elif new_game == "2":
        print("""
        Follow the prompts.

        When it asks where you would like to place your move, pick a number 1-9.

        The move you choose will be in one of the corresponding spots.

        1 | 2 | 3
        ---------
        4 | 5 | 6
        ---------
        7 | 8 | 9
        """)

        game()

    else:
        print("Thanks for playing")
        quit()

def print_board(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-----')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-----')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])

def reset_board(board):
    for keys in board:
        board[keys] = " "

if __name__ == "__main__":
    game()
