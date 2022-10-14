# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#  a) Добавьте игру против бота
#  b) Подумайте как наделить бота "интеллектом"

import random

col_gamers = int(input('Выберите количество игроков 1 или 2: '))
all_candies = 2021

def start_game_lot(first_gamer, second_gamer):
    print(f'\nНа столе лежит {all_candies} конфет. За один ход можно взять не более 28 конфет. Все конфеты достанутся тому, кто сделает последний ход. \nОпределим, кто начнет первым игру.\n')

    first_player  = random.choice([first_gamer, second_gamer])
    print(f'Первым ход делаем игрок {first_player}')
    
    if first_player==first_gamer:
        second_player = second_gamer
    else:
        second_player = first_gamer

    return first_player, second_player

def the_game_player (all_candies, player):
    if all_candies != 0:
        candies = int(input(f'Сколько конфет возьмет игрок {player}: '))
        if candies <=28:
            all_candies -= candies
            print(f'На столе осталось {all_candies} конфет\n')
        else:
            print('Можно брать не более 28 конфет! Переход хода!\n')
        if all_candies == 0:
           print(f'Ура! Выйграл игрок {player}. Поздравляем!') 

    return all_candies

def the_game_Computer(all_candies):
    if all_candies != 0:
        candies = all_candies % 29
        print(f'Computer взял {candies} конфет')
        all_candies -= candies
        print(f'На столе осталось {all_candies} конфет\n')
        if all_candies == 0:
            print(f'Выйграл Computer!')
        
    return all_candies

    # Режим игры с компьютером
    
if col_gamers == 1:

    first_gamer = input('Введите имя 1го игрока: ')
    second_gamer = 'Computer'
    print('Против вас играет Computer')
    first_player, second_player = start_game_lot(first_gamer, second_gamer)

    if first_player == first_gamer:
        while all_candies > 0:
            all_candies = the_game_player(all_candies, first_player)
            all_candies = the_game_Computer (all_candies)
    else:
        while all_candies > 0:
            all_candies = the_game_Computer (all_candies)
            all_candies = the_game_player(all_candies, second_player)

    # Игра 2ух игроков

if col_gamers == 2:
    first_gamer = input('Введите имя 1го игрока: ')
    second_gamer = input('Введите имя 2го игрока: ')
    
    first_player, second_player = start_game_lot(first_gamer, second_gamer)

    while all_candies > 0:
        all_candies = the_game_player(all_candies, first_player)
        all_candies = the_game_player(all_candies, second_player)
        

