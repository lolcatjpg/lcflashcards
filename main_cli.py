import json
import feedback
import set_edit


def practice():
    set_file = input("file: ")
    with open(set_file, "r") as f:
        flashcards = json.loads(f.read())["cards"]

    for card in flashcards:
        user_answer = input(f"{card.get('q')}: ")
        feedback_list, correct = feedback.q_a_checker(user_answer, card)
        if correct:
            print("Correct!\n")
        else:
            print(f"Incorrect!\nYour answer:\n{feedback_list[0]}\n{feedback_list[1]}\nCorrect answer:\n{feedback_list[2]}\n{feedback_list[3]}")

        card = feedback.update_rating(card, correct, 2)
        set_edit.update_set(set_file, flashcards)


def import_csv():
    in_file = input('csv file: ')
    out_file = input('output file: ')
    set_edit.csv_import(in_file, out_file)


def reset_progress():
    set_file = input("file: ")
    set_edit.reset_progress(set_file)


def main():
    print("Choose an option:\n",
    "(1) import file\n",
    "(2) practice\n",
    "(3) reset progress")
    options = {1: import_csv, 2: practice, 3: reset_progress}
    options[int(input())]()


if __name__ == "__main__":
    main()
