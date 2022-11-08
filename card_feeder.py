def simple(cards: list, settings: dict) -> list:
    """returns list of card indexes to practice (simple algorithm)"""
    from random import shuffle

    card_order = []
    for i, card in enumerate(cards):
        print(i)
        if card["competence"] == settings["max_competence"]:
            cards.pop(i)
        else:
            card_order.append(i)
    shuffle(card_order)
    return card_order
