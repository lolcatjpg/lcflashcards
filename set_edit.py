import json

def csv_import(csv_file: str, output_set: str) -> None:
    """reads cards from csv file and outputs them to json file.
    format for csv file: question,answer"""
    import csv

    with open(csv_file, newline="") as f:
        reader = csv.reader(f)
        cards = []
        for row in reader:
            cards.append(row)

    set_json = {"cards": []}
    for card in cards:
        set_json["cards"].append({"q": card[0], "a": card[1], "competence": -1})
    
    set_json["settings"] = {"max_competence": 2}

    with open(output_set, "w") as f:
        f.write(json.dumps(set_json, indent=4))


def update_set(set_file: str, flashcards: list) -> None:
    """updates the flashcards file"""

    with open(set_file, "r") as f:
        cards_json = json.loads(f.read())
        cards_json["cards"] = flashcards
    with open(set_file, "w") as f:
        f.seek(0)
        f.write(json.dumps(cards_json, indent=4))


def reset_progress(set_file: str) -> None:
    """resets competence values of all cards in set"""

    with open(set_file, "r") as f:
        cards_json = json.loads(f.read())
        for i, _ in enumerate(cards_json["cards"]):
            cards_json["cards"][i]["competence"] = -1
    with open(set_file, "w") as f:
        f.seek(0)
        f.write(json.dumps(cards_json, indent=4))
