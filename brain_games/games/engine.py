import prompt


def greeting():
    print('Welcome to the Brain Games!')


def get_player_name():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def get_answer():
    player_answer = prompt.string('Your answer: ')
    return player_answer


def start_game(name_of_the_game, player_name):
    correct_answer_count = 0

    while correct_answer_count < 3:
        result = name_of_the_game(player_name)
        if result:
            correct_answer_count += 1
        else:
            return None


def is_right_answer(player_answer, right_answer, pl_name):
    if right_answer == player_answer:
        print('Correct!')
        return True
    else:
        print(f"'{player_answer}' is wrong answer ;(.", end=' ')
        print(f"Correct answer was '{right_answer}'.")
        print(f"Let's try again, {pl_name}!")
        return False
