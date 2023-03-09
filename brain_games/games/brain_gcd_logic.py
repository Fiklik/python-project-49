from random import randint
from . import engine


def gcd(pl_name):
    first_num = randint(1, 20)
    second_num = randint(1, 20)
    small_num = first_num if first_num < second_num else second_num
    right_answer = 0

    for i in range(1, small_num + 1):
        if first_num % i == 0 and second_num % i == 0:
            right_answer = str(i)

    print(f'Question: {first_num} {second_num}')

    player_answer = engine.get_answer()

    return engine.is_right_answer(player_answer, right_answer, pl_name)


def brain_gcd():
    engine.greeting()
    player_name = engine.get_player_name()

    print('Find the greatest common divisor of given numbers.')

    engine.start_game(gcd, player_name)
