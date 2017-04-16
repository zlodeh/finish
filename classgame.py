import igra

board = ["1","2","3","4","5","6","7","8","9"]
next_move = []
number_input = 0
class human:
    def __init__(self, number, enter_number):
        self.number = number

    def human_input():
        number = input()
        return human.review_input(number)

    def review_input(number):
        while True:
            try:
                number = int(number)
                if number <= 0 or number>= 10:
                    print("Вы вели неправильное значение. Повоторите пожалуйста")
                    return human.human_input()
                else:
                    try:
                        next_move.index(number)
                        print("Данная клетка занята. Повторите пожалуйста")
                        return human.human_input()
                    except ValueError:
                        print("Вы вели правильно")
                        next_move.append(number)
                        return number
            except ValueError:
                print("Вы вели букву. Ведите число")
                return human.human_input()

    def play_x(number):
        board.pop(number-1)
        board.insert(number-1,"X")
        return game.draw_board()


    def play_o(number):
        board.pop(number-1)
        board.insert(number-1,"0")
        return game.draw_board()

class game:
    def __init__(self, variant, ):
        self.variant = variant

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

    def game_variant(variant):
        if variant == "X" or variant == "x":
            while range(5):
                print("Ходить первый игрок X")
                first = human
                first.play_x(first.human_input())
                print("Ходтив второй игрок 0")
                second = human
                second.play_o(second.human_input())
        elif variant == "0":
            while range(5):
                print("Ходтив первый игрок 0")
                second = human
                second.play_o(second.human_input())
                print("Ходить второй игрок X")
                first = human
                first.play_x(first.human_input())
        elif variant == "random" or variant == "Random":
            variant = str(randint(0, 1))
            if variant == "1":
                variant = "X"
                game.game_variant(variant)
            elif variant == "0":
                variant = "0"
                game.game_variant(variant)

def chek_human():
    while True:
        enter_number = input()
        try:
            enter_number = int(enter_number)
            if enter_number <= 0 or enter_number>= 3:
                print("Вы вели неправильное значение. Повоторите пожалуйста")
                return chek_human()
            else:return enter_number
        except ValueError:
            print("Вы вели букву. Ведите число")
            return chek_human()

if __name__ == '__main__':
    print("Добро пожаловать в игру Х и О")
    game.draw_board()
    print("Если хотите играть против PC введите 1.\n Если 2 игрока введите 2")
    variant_play = chek_human()
    if variant_play == 1:
        print("Вы выбриали игру против PC")
        igra.game.draw_board()
        igra.intelect_game()
    elif variant_play == 2:
        print("Добро пожаловать в игру Х и 0 \n Кем будете ходить? 0 (ведите - 0), Х (ведите - X) или вариант Random(ведите - random)? ")
        enter = input()
        game.game_variant(enter)

    else:
        print("Вы вели не правильно, повторите")
