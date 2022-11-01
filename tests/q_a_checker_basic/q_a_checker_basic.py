import difflib

from q_a_checker_basic_flashcards import flashcards_latin as flashcards
    

rchecker = difflib.Differ()

for i in range(len(flashcards)):
    question = flashcards[i]['q']
    correct_answer = flashcards[i]['a']
    user_answer = input(f"{question}: ")

    feedback = list(rchecker.compare([user_answer], [correct_answer]))
    
    if len(feedback) == 1:  # check if answer is correct, which means len(feedback) == 1
        print(f"Correct! (Your answer: {user_answer})\n")
    else:
        if len(feedback) in [2, 3]:  # this means there is no addition and/or no removal clarification line
            feedback.append(" ")  # add string with space for following check to work
            for j in range(1, 4, 2):  # check if line 2 and 4 in feedback are addition/removal clarification, if not, insert line with '?'
                if feedback[j][0] != "?":
                    feedback.insert(j, "?")
            feedback.pop(4)  # remove empty item that was added for check
        print(f"Your answer:\n{feedback[0]}\n{feedback[1]}\nCorrect answer:\n{feedback[2]}\n{feedback[3]}")
