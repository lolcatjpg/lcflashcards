def q_a_checker(user_input: str, flashcard: dict) -> tuple[list, bool]:
    """returns tuple with feedback (list) and True/False for correct/incorrect answer"""
    from difflib import Differ

    d = Differ()

    correct_answer = flashcard.get("a")

    feedback = list(d.compare([user_input], [correct_answer]))
    
    if len(feedback) == 1:  # check if answer is correct, which means len(feedback) == 1
        return feedback, True
    else:
        if len(feedback) in (2, 3):  # this means there is no addition and/or no removal clarification line
            feedback.append(" ")  # add string with space for following check to work
            for j in range(1, 4, 2):  # check if line 2 and 4 in feedback are addition/removal clarification, if not, insert line with '?'
                if feedback[j][0] != "?":
                    feedback.insert(j, "?\n")
            feedback.pop(4)  # remove empty item that was added for check
        return feedback, False


def update_rating(flashcard: dict, correct: bool, max_competence: int) -> dict:
    """update competence rating of flashcard, based on if user was correct.
    returns the updated flashcard"""
    if flashcard.get("competence") == -1:
        if correct:
            flashcard["competence"] = max_competence
        else:
            flashcard["competence"] = 0
    else:
        if correct and flashcard["competence"] < max_competence:
            flashcard["competence"] += 1
        elif not correct and flashcard["competence"] > 0:
            flashcard["competence"] = 0

    return flashcard
