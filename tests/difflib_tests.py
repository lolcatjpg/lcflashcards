import difflib
import sys

text1 = "parralelogram"
text2 = "parallellogram"

# text1 = input("text 1: ")
# text2 = input("text 2: ")

# add newline in arrays and put into array
compare1 = [f"{text1}\n"]
compare2 = [f"{text2}\n"]

d = difflib.Differ()

result = list(d.compare(compare1, compare2))
print(f"\n{result}\n")
sys.stdout.writelines(result)
print()


# print indexes of additions and deletions (for later use)
deletions = []
additions = []
check_index = -2
for i in result[1]:
    if i == "-":
        deletions.append(check_index)
    check_index += 1
check_index = -2
for i in result[3]:
    if i == "+":
        additions.append(check_index)
    check_index += 1

print(deletions, additions)


print()
print(f"Your answer:\n{result[0]}{result[1]}\nCorrect answer:\n{result[2]}{result[3]}")
