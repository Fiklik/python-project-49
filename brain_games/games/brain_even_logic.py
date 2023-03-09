from random import randint
from . import engine


def is_even_number(number):
    res = number % 2 == 0

    return 'yes' if res else 'no'


def even_or_odd(pl_name):
    random_number = randint(1, 100)
    right_answer = is_even_number(random_number)

    print(f'Question: {random_number}')

    player_answer = engine.get_answer()

    return engine.is_right_answer(player_answer, right_answer, pl_name)


def brain_even():
    engine.greeting()
    player_name = engine.get_player_name()

    print('Answer "yes" if the number is even, otherwise answer "no".')

    engine.start_game(even_or_odd, player_name)
