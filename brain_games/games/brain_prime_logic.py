from random import randint
from . import engine


def is_prime(num):
    dividers_count = 0

    for i in range(1, num + 1):
        if num % i == 0:
            dividers_count += 1

    return 'yes' if dividers_count == 2 else 'no'


def prime(pl_name):
    random_number = randint(1, 100)
    right_answer = is_prime(random_number)

    print(f'Question: {random_number}')

    player_answer = engine.get_answer()

    return engine.is_right_answer(player_answer, right_answer, pl_name)


def brain_prime():
    engine.greeting()
    player_name = engine.get_player_name()

    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    engine.start_game(prime, player_name)
