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

    while True:
        cards = card_feeder.shuffle_simple(cards_raw, settings)
        if len(cards = 0):
            print("Practice finished!")
            break
        for flashcard_index in cards:
            user_answer = input(f"{cards_raw[flashcard_index].get('q')}: ")
            feedback_list, correct = feedback.check_answer(user_answer, cards_raw[flashcard_index])
            if correct:
                print("Correct!\n")
            else:
                print(f"Incorrect!\nYour answer:\n{feedback_list[0]}\n{feedback_list[1]}\nCorrect answer:\n{feedback_list[2]}\n{feedback_list[3]}")

            cards_raw[flashcard_index] = feedback.update_rating(cards_raw[flashcard_index], correct, settings["max_competence"])
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
