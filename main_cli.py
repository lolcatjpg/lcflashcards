import json
import feedback
import set_edit
import card_feeder


def practice():
    set_file = input("file: ")
    with open(set_file, "r") as f:
        f_content = json.loads(f.read())
        cards_raw = f_content["cards"]
        settings = f_content["settings"]

    cards = card_feeder.simple(cards_raw, settings)
    for flashcard in cards:
        user_answer = input(f"{flashcard.get('q')}: ")
        feedback_list, correct = feedback.check_answer(user_answer, flashcard)
        if correct:
            print("Correct!\n")
        else:
            print(f"Incorrect!\nYour answer:\n{feedback_list[0]}\n{feedback_list[1]}\nCorrect answer:\n{feedback_list[2]}\n{feedback_list[3]}")

        flashcard = feedback.update_rating(flashcard, correct, settings["max_competence"])
        set_edit.update_set(set_file, cards_raw)


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
