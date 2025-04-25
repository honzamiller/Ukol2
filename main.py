"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Jan Miller
email: miller.honza.15@seznam.cz 
"""

import random
import time


def welcome_message():
    print("-----------------------------------------------")
    print("Hi there!")
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-----------------------------------------------")


def generate_number():
    digits = list("123456789")
    number = random.choice(digits)
    digits.remove(number)
    digits += "0" 
    while len(number) < 4:
        digit = random.choice(digits)
        if digit not in number:
            number += digit
    return number


def get_user_guess():
    while True:
        guess = input("Enter a 4-digit number: ")
        if not guess.isdigit():
            print("Please enter only digits.")
        elif len(guess) != 4:
            print("Number must be exactly 4 digits long.")
        elif guess[0] == "0":
            print("Number must not start with zero.")
        elif len(set(guess)) != 4:
            print("Digits must be unique.")
        else:
            return guess


def evaluate_guess(secret, guess):
    bulls = sum(s == g for s, g in zip(secret, guess))
    cows = sum(g in secret for g in guess) - bulls
    return bulls, cows


def format_result(bulls, cows):
    b = f"{bulls} bull{'s' if bulls != 1 else ''}"
    c = f"{cows} cow{'s' if cows != 1 else ''}"
    return f"{b}, {c}"


def main():
    welcome_message()
    secret_number = generate_number()
    attempts = 0
    start_time = time.time()

    while True:
        guess = get_user_guess()
        attempts += 1
        bulls, cows = evaluate_guess(secret_number, guess)
        print(format_result(bulls, cows))
        if bulls == 4:
            break

    end_time = time.time()
    elapsed_time = round(end_time - start_time, 2)
    print(f"Correct, you've guessed the right number in {attempts} guess{'es' if attempts != 1 else ''}!")
    print(f"Time taken: {elapsed_time} seconds")
    print("That's amazing!")


if __name__ == "__main__":
    main()
