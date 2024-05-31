# final project
# 1 vs 1
import pickle

board = {"1": " ", "2": " ", "3": " ",
         "4": " ", "5": " ", "6": " ",
         "7": " ", "8": " ", "9": " "}
pickle.dump(board, open("test.pkl","wb"))
open("board","w")

board_keys = [ ]
for key in board:
    board_keys.append(key)

# '\033[04m' (underlining)

# setting up the board display
def print_board(board):
    print(board["1"] + "|" + board["2"] + "|" + board["3"])
    print("-+-+-")
    print(board["4"] + "|" + board["5"] + "|" + board["6"])
    print("-+-+-")
    print(board["7"] + "|" + board["8"] + "|" + board["9"])


print("welcome to tic tac toe")


def game():
    turn = "X"
    counter = 0

    for i in range(10):
        print_board(board)
        print("your turn " + turn + ",choose your move ")

        move = input()
        numbers = move.split(',')
        if int(numbers[0]) == 0:
            move = int(numbers[0]) + int(numbers[1]) + 1
        elif int(numbers[0]) == 1:
            move = int(numbers[0]) + int(numbers[1]) + 2
        elif int(numbers[0]) == 2:
            move = int(numbers[0]) + int(numbers[1]) + 3

        move = str(move)
        # if the location of the move is empty,game proceeds
        if board[move] == " ":
            board[move] = turn
            counter += 1
        # elif board[move] == "q" or "Q":
        #     quit()
        # elif board[move] != " ":
        #     print("this place is taken already")
        else:
            print("that place is taken already.")
            continue



        if counter >= 5:
            # horizontal
            if board["1"] == board["2"] == board["3"] != " ":
                print("Game over")
                print(turn + " " + "won, congrats!")
                break
            elif board["4"] == board["5"] == board["6"] != " ":
                print("Game over")
                print(turn + " " + "won, congrats!")
                break
            elif board["7"] == board["8"] == board["9"] != " ":
                print("Game over")
                print(turn + " " + "won, congrats!")
                break
                # vertical
            elif board["1"] == board["4"] == board["7"] != " ":
                print("Game over")
                print(turn + " " + "won, congrats!")
                break
            elif board["2"] == board["5"] == board["8"] != " ":
                print("Game over")
                print(turn + " " + "won, congrats!")
                break
            elif board["3"] == board["6"] == board["9"] != " ":
                print("Game over")
                print(turn + " " + "won, congrats!")
                break
                # diagonal
            elif board["1"] == board["5"] == board["9"] != " ":
                print("Game over")
                print(turn + " " + "won, congrats!")
                break
            elif board["3"] == board["5"] == board["7"] != " ":
                print("Game over")
                print(turn + " " + "won, congrats!")
                break

        if counter == 9:
            print("game over")
            print("it's a tie")
            restart = input("would you like to play again? (y/n)")
            if restart == "y" or restart == "Y":
                for key in board_keys:
                    board[key] = " "

                game()
            else:
                break

        if turn == "X":
            turn = "O"
        else:
            turn = "X"
    restart = input("would you like to play again? (y/n)")
    if restart == "y" or restart == "Y":
        for key in board_keys:
            board[key] = " "

        game()

if __name__ == "__main__":
    game()
