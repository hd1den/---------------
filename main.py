# hello all !
import colorama
import os

colorama.init()
green = colorama.Fore.GREEN
red = colorama.Fore.RED
magenta = colorama.Fore.MAGENTA
blue = colorama.Fore.BLUE
reset =  colorama.Fore.RESET
board = list(range(1, 10))


cells = 3
dashes = 13
spaces = 4
counter = 0

is_win = False

win_coords = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8), 
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
)
tokens_list = [red + 'X' + reset, green + 'O' + reset]
# напишем функцию для вывода игровой доски

def draw_board():
    os.system('cls')
    print(magenta + "\n* Игра крестики-нолики*\n" + reset)
    for i in range(cells):
        print(" " * spaces, end ='')
        print('-' * dashes)
        print(" " * spaces, end ='')
        print(f'| {board[0 + i * 3]} | {board[1 + i * 3 ]} | {board[2 + i * 3]} |')
    print(" " * spaces, end ='')
    print('-' * dashes)


while not is_win:
    draw_board()

    
    player_token = tokens_list[counter % 2 ]
   


    player_answer = input(f'Куда ставим {player_token}? ')

    player_answer = int(player_answer) - 1
    if board[player_answer] not in tokens_list:
        board[player_answer] = player_token
        counter += 1

    else:
        print(f"{magenta}Эта {red}ячейка {blue}уже {green}занята!" + reset)
        input("Нажмите ENTER\n")
        continue

    if counter > 4:
        for each in win_coords:
            if board[each[0]] == board[each[1]] == board[each[2]]:
                is_win = True
                break
        if is_win:
            draw_board()
            print(f'Победил {player_token}! Поздравляем!\n')
            break

    if counter == 9:
        draw_board()
        print("Ничья\n")
        break