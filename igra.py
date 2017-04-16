board = ["1","2","3","4","5","6","7","8","9"]
next_move = []
full_mov = [1,2,3,4,5,6,7,8,9]
class game:
    def __init__(self, variant, number ):
        self.variant = variant
        self.number = number

    def human_input():
        number = input()
        return game.review_input(number)

    def review_input(number):
        while True:
            try:
                number = int(number)
                if number <= 0 or number>= 10:
                    print("Вы вели неправильное значение. Повоторите пожалуйста")
                    return game.human_input()
                else:
                    try:
                        next_move.index(number)
                        print("Данная клетка занята. Повторите пожалуйста")
                        return game.human_input()
                    except ValueError:
                        print("Вы вели правильно")
                        next_move.append(number)
                        full_mov.remove(number)
                        return number
            except ValueError:
                print("Вы вели букву. Ведите число")
                return game.human_input()

    def play_win():
        if board[0] == board[1] == board[2]:
            print("Вы виграли ")
            raise SystemExit
        elif board[3] == board[4] == board[5]:
            print("Вы виграли ")
            raise SystemExit
        elif board[6] == board[7] == board[8]:
            print("Вы виграли ")
            raise SystemExit
        elif board[1] == board[4] == board[7]:
            print("Вы виграли ")
            raise SystemExit
        elif board[2] == board[5] == board[8]:
            print("Вы виграли ")
            raise SystemExit
        elif board[0] == board[3] == board[6]:
            print("Вы виграли ")
            raise SystemExit
        elif board[0] == board[4] == board[8]:
            print("Вы виграли ")
            raise SystemExit
        elif board[6] == board[4] == board[2]:
            print("Вы виграли ")
            raise SystemExit
        elif len(next_move) == 9:
            print("Ничья")
            raise SystemExit

    def draw_board():
        print("-------------")
        print("|", board[0], "|", board[1], "|", board[2], "|")
        print("-------------")
        print("|", board[3], "|", board[4], "|", board[5], "|")
        print("-------------")
        print("|", board[6], "|", board[7], "|", board[8], "|")
        print("-------------")
        game.play_win()

    def play_o(number):
        board.pop(number-1)
        board.insert(number-1,"0")
        return game.draw_board()

    def play_x(number):
        board.pop(number-1)
        board.insert(number-1,"X")
        return game.draw_board()

def intelect_game():
    for i in range(1,10):
        if i == 1:
            chislo = 5
            next_move.append(chislo)
            full_mov.remove(chislo)
            print("Ходить игрок PC",)
            game.play_x(chislo)
        elif i == 3:
            if board[0] != "0":
                chislo = 1
                next_move.append(chislo)
                full_mov.remove(chislo)
                print("Ходить игрок PC")
                game.play_x(chislo)
            else:
                chislo = 3
                next_move.append(chislo)
                full_mov.remove(chislo)
                print("Ходить игрок PC")
                game.play_x(chislo)
        elif i == 5:
                if board[0] == "X" and board[4] == "X" and board[8] != "0":
                    chislo = 9
                    next_move.append(chislo)
                    full_mov.remove(chislo)
                    print("Ходить игрок PC")
                    game.play_x(chislo)
                elif board[2] == "X" and board[4] == "X" and board[6] != "0":
                    chislo = 7
                    next_move.append(chislo)
                    full_mov.remove(chislo)
                    print("Ходить игрок PC")
                    game.play_x(chislo)

                elif board[2] == "0" and board[8] == "0" and board[5] != "X":
                    chislo = 6
                    next_move.append(chislo)
                    full_mov.remove(chislo)
                    print("Ходить игрок PC")
                    game.play_x(chislo)

                else:
                    if board[8] != "0":
                        chislo = 9
                        next_move.append(chislo)
                        full_mov.remove(chislo)
                        print("Ходить игрок PC")
                        game.play_x(chislo)
                    elif board[6] != "0":
                        chislo = 7
                        next_move.append(chislo)
                        full_mov.remove(chislo)
                        print("Ходить игрок PC")
                        game.play_x(chislo)
                    else:
                        chislo = 3
                        next_move.append(chislo)
                        full_mov.remove(chislo)
                        print("Ходить игрок PC")
                        game.play_x(chislo)

        elif i == 7:
            if board[0] == "X" and board[6] == "X" and board[3] != "0":
                chislo = 4
                next_move.append(chislo)
                full_mov.remove(chislo)
                print("Ходить игрок PC")
                game.play_x(chislo)
            elif board[4] == "X" and board[6] == "X" and board[2] != "0":
                chislo = 3
                next_move.append(chislo)
                full_mov.remove(chislo)
                print("Ходить игрок PC")
                game.play_x(chislo)
            elif board[0] == "X" and board[2] == "X" and board[1] != "0":
                chislo = 2
                next_move.append(chislo)
                full_mov.remove(chislo)
                print("Ходить игрок PC")
                game.play_x(chislo)
            elif board[2] == "0" and board[8] == "0" and board[5] != "X":
                chislo = 6
                next_move.append(chislo)
                full_mov.remove(chislo)
                print("Ходить игрок PC")
                game.play_x(chislo)
            else:
                if board[1] != "0":
                    print("Ходить игрок PC")
                    chislo = 2
                    next_move.append(chislo)
                    full_mov.remove(chislo)
                    game.play_x(chislo)
                elif board[7] != "0":
                    print("Ходить игрок PC")
                    chislo = 8
                    next_move.append(chislo)
                    full_mov.remove(chislo)
                    game.play_x(chislo)
        elif i == 9:
            chislo = full_mov[0]
            print("Ходить игрок PC")
            next_move.append(chislo)
            game.play_x(chislo)
        else:
            print("Ходтив второй игрок 0")
            second = game
            second.play_o(game.human_input())

