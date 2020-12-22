def GetLines():
    with open("day22\\entries.txt") as f:
        entries = f.readlines()
    return entries

def EntriesToDecks(entries):
    decks = list()
    for entry in entries:
        if entry.startswith('Player '):
            deck = list()
        elif entry == '\n':
            decks.append(deck)
        else:
            deck.append(int(entry))
    if deck not in decks:
        decks.append(deck)
    return decks[0], decks[1]
        
def playgame(deck_1, deck_2):
    while deck_1 and deck_2:
        deck_1, deck_2 = play_round(deck_1, deck_2)
    if deck_1:
        return deck_1
    else:
        return deck_2

def play_round(deck_1, deck_2):
    card_1 = deck_1.pop(0)
    card_2 = deck_2.pop(0)
    if card_1 > card_2:
        deck_1.append(card_1)
        deck_1.append(card_2)
    else:
        deck_2.append(card_2)
        deck_2.append(card_1)
    return deck_1, deck_2

def calculate_score(deck):
    deck = deck[::-1]
    score = 0
    for i in range(len(deck)):
        score += deck[i] * (i + 1)
    return score

if __name__ == "__main__":
    entries = GetLines()
    deck_1, deck_2 = EntriesToDecks(entries)
    winner = playgame(deck_1, deck_2)
    score = calculate_score(winner)
    print(score)