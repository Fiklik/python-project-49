from random import randint, choice
from . import engine


def calc(pl_name):
    first_number = randint(1, 50)
    second_number = randint(1, 10)
    calc_operator = choice('*+')

    if calc_operator == '+':
        right_answer = str(first_number + second_number)
    else:
        right_answer = str(first_number * second_number)

    print(f'Question: {first_number} {calc_operator} {second_number}')

    player_answer = engine.get_answer()

    return engine.is_right_answer(player_answer, right_answer, pl_name)


def brain_calc():
    engine.greeting()
    player_name = engine.get_player_name()

    print('What is the result of the expression?')

    engine.start_game(calc, player_name)
