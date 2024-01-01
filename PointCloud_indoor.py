import numpy as np
import pandas as pd
import open3d as o3d
import matplotlib.pyplot as plt
import yaml
import os


import random

def choose_geospatial_word():
    geospatial_words = [
        "cartography",
        "coordinate reference systems",
        "geographic data",
        "geographic information systems",
        "geographic information technology",
        "geographic database",
        "geodesy",
        "geodetic coordinate systems",
        "geodetic measurements",
        "geodetic networks",
        "geoinformatics",
        "geomatics engineering",
        "geospatial technologies",
        "gis analysis",
        "gnss",
        "map projection",
        "remote sensing",
        "remote sensing data",
        "spatial analysis",
        "spatial planning"
    ]
    return random.choice(geospatial_words)

def display_word(secret_word, guessed_letters):
    return "".join(letter if letter in guessed_letters else "_" for letter in secret_word)

def calculate_score(secret_word, guessed_letters, incorrect_guesses):
    correct_guesses = set(guessed_letters).intersection(set(secret_word))
    uncovered_letters = len(set(secret_word) - set(correct_guesses))
    score = len(correct_guesses) - (0.1 * incorrect_guesses) - uncovered_letters
    return max(score, 0)

def geospatial_word_guess_game():
    user_name = input("What's your name? ")
    secret_word = choose_geospatial_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 3

    print(f"Welcome, {user_name}, to the Geospatial Word Guessing Game!")
    print(f"The geospatial term has {len(secret_word)} letters.")
    print("The geospatial term you need to guess:", display_word(secret_word, guessed_letters))

    while True:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed this letter. Try another one.")
            continue

        guessed_letters.add(guess)

        if guess not in secret_word:
            incorrect_guesses += 1
            print(f"Wrong guess! Remaining guesses: {max_incorrect_guesses - incorrect_guesses}")

        print("The geospatial term you need to guess:", display_word(secret_word, guessed_letters))

        if set(secret_word) <= guessed_letters:
            score = calculate_score(secret_word, guessed_letters, incorrect_guesses)
            print(f"Congratulations, {user_name}! You found the geospatial term. Your score: {score}")
            break

        if incorrect_guesses == max_incorrect_guesses:
            score = calculate_score(secret_word, guessed_letters, incorrect_guesses)
            print(f"Unfortunately, you've run out of guesses. The correct geospatial term was: {secret_word}")
            print(f"Your score: {score}")
            break

    if incorrect_guesses == max_incorrect_guesses:
        give_up = input("Do you want to give up? (yes/no): ").lower()
        if give_up == "yes":
            score = calculate_score(secret_word, guessed_letters, incorrect_guesses)
            print(f"Sorry to see you give up, {user_name}. The correct geospatial term was: {secret_word}")
            print(f"Your score: {score}")

if __name__ == "__main__":
    geospatial_word_guess_game()
