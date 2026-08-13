import random

COLORS = ["R", "Y", "B", "O", "G", "W"]
TRIES = 10
CODE_LENGTH = 4


def generate_code():
    code = []

    for _ in range(CODE_LENGTH):
        color = random.choice(COLORS)
        code.append(color)

    return code


def guess_code():
    while True:
        guess = input("Guess: ").upper().split()

        if len(guess) != CODE_LENGTH:
            print(f"You must guess {CODE_LENGTH} colors.")
            continue

        for color in guess:
            if color not in COLORS:
                print(f"Invalid color: {color}. Try again.")
                break
        else:
            return guess


def check_code(guess, real_code):
    color_counts = {}
    correct_pos = 0
    incorrect_pos = 0

    # Count the colors in the real code
    for color in real_code:
        if color not in color_counts:
            color_counts[color] = 0

        color_counts[color] += 1

    # Check correct positions
    for guess_color, real_color in zip(guess, real_code):
        if guess_color == real_color:
            correct_pos += 1
            color_counts[guess_color] -= 1

    # Check incorrect positions
    for guess_color, real_color in zip(guess, real_code):
        if (
            guess_color in color_counts
            and color_counts[guess_color] > 0
        ):
            incorrect_pos += 1
            color_counts[guess_color] -= 1

    return correct_pos, incorrect_pos


def game():
    print(
        f"Welcome to Mastermind! "
        f"You have {TRIES} attempts to guess the code."
    )

    print("The valid colours are:", *COLORS)

    code = generate_code()

    for attempts in range(1, TRIES + 1):
        guess = guess_code()

        correct_pos, incorrect_pos = check_code(guess, code)

        if correct_pos == CODE_LENGTH:
            print(f"You guessed the code in {attempts} attempts!")
            break

        print(
            f"Correct positions: {correct_pos} | "
            f"Incorrect positions: {incorrect_pos}"
        )

    else:
        print("You ran out of attempts!")
        print("The code was:", *code)


if __name__ == "__main__":
    game()