from random import randint
from . import engine


def progression(pl_name):
    progression_start = randint(1, 20)
    progression_len = randint(5, 10)
    progression_step = randint(1, 10)
    progression_list = [progression_start]
    random_index = randint(0, progression_len -1)

    for i in range(1, progression_len):
        progression_list.append(progression_list[i - 1] + progression_step)

    right_answer = str(progression_list[random_index]) 
    progression_list[random_index] = '..'

    progression_output = str(progression_list[0])

    for elem in progression_list[1:]:
        progression_output += f' {elem}'

    print(f'Question: {progression_output}')

    player_answer = engine.get_answer()

    return engine.is_right_answer(player_answer, right_answer, pl_name)


def brain_progression():
    engine.greeting()
    player_name = engine.get_player_name()

    print('What number is missing in the progression?')

    engine.start_game(progression, player_name)
