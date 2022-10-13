# Создайте программу для игры в ""Крестики-нолики""
import random

board = list(range(1,10))

def print_board():
    print( '-'*13)
    for i in range(3):
        print (f'| {board[0+i*3]} | {board[1+i*3]} | {board[2+i*3]} |')
        print( '-'*13)

def player_game(board):
    player_move = int(input('Сделайте ход: ')) 
    if player_move >=1 and player_move <=9:
        if str(player_move) not in 'XO':
            board[player_move-1] = 'O'
        else: 
            print("Эта ячейка занята")
    else:
        print ('Необходимо ввести номер ячейки')

def computer_game(board):
    comp_move = random.choice(board) 
    if str(comp_move) not in 'XO':
        board[comp_move-1] = 'X'
    else:
        computer_game(board)

def check_win(board):
    winner_sets = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in winner_sets:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

def the_game(board):
    count = 0
    win = False
    while not win:
        print_board()
        if count % 2 == 0:
            player_game(board)
        else:
            print('Ходит компьютер')
            computer_game(board)
        count += 1
        if count > 4:
            check = check_win(board)
            if check:
                print ('\nУра! Победа!')
                win = True
                break
        if count == 9:
            print ("Ничья!")
            break

print('Начало игры. \nВы играете за О')
the_game(board)

print( '-'*13)
print('Исход игры')
print_board()