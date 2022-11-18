def shuffle_simple(cards: list, settings: dict) -> list:
    """returns list of card indexes to practice (simple algorithm)"""
    from random import shuffle

    card_order = []
    for i, card in enumerate(cards):
        print(i, end=" ")  # DEBUG
        if card["competence"] < settings["max_competence"]:
            card_order.append(i)
    shuffle(card_order)
    print("")  # print newline after printing card numbers
    return card_order  # DEBUG
