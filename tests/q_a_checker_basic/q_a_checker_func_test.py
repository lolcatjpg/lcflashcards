# imports (https://www.geeksforgeeks.org/python-import-from-parent-directory/) #
import sys

sys.path.append("../quizlet_learn_mode")

from feedback import q_a_checker
from set_edit import csv_import
from q_a_checker_basic_flashcards import flashcards_latin as flashcards


if __name__ == "__main__":
    for i, card in enumerate(flashcards):
        user_answer = input(f"{card.get('q')}: ")
        feedback, correct = q_a_checker(user_answer, card)
        if correct:
            print("Correct!\n")
        else:
            print(f"Incorrect!\nYour answer:\n{feedback[0]}\n{feedback[1]}\nCorrect answer:\n{feedback[2]}\n{feedback[3]}")