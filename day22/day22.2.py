def GetLines():
    with open("day22\\entries.txt") as f:
        entries = f.readlines()
    return entries

def CheckRoundHistory(deck_1, deck_2, round_history):
    round_string_1 = ''
    for n in deck_1:
        round_string_1 += ' '
        round_string_1 += str(n)

    round_string_2 = ''
    for n in deck_2:
        round_string_2 += ' '
        round_string_2 += str(n)

    isPresent = False
    if round_string_1 in round_history:
        if round_string_2 in round_history[round_string_1]:
            isPresent = True
        else:
            round_history[round_string_1].append(round_string_2)
    else:
        round_history[round_string_1] = list()
        round_history[round_string_1].append(round_string_2)
    return round_history, isPresent


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
    # print('New game')
    history = {}
    deck_1_c = deck_1.copy()
    deck_2_c = deck_2.copy()
    winner = None
    while winner is None:
        deck_1_c, deck_2_c, winner = play_round(deck_1_c, deck_2_c, history)
    return deck_1_c, deck_2_c, winner

def play_round(deck_1, deck_2, history):
    history, already_played = CheckRoundHistory(deck_1, deck_2, history)
    if already_played:
        # print('AlreadyPlayed', deck_1, deck_2)
        return deck_1, deck_2, 1
   
    # print('Player 1 deck:', deck_1)
    # print('Player 2 deck:', deck_2)
    card_1 = deck_1.pop(0)
    card_2 = deck_2.pop(0)
    # print('Player 1 card:', card_1)
    # print('Player 2 card:', card_2)
    if len(deck_1) >= card_1 and len(deck_2) >= card_2:
        _, _, winner = playgame(deck_1[:card_1], deck_2[:card_2])
        # print()
    else:
        if card_1 > card_2:
            winner = 1
        else:
            winner = 2
    if winner == 1:
        deck_1.append(card_1)
        deck_1.append(card_2)
    else:
        deck_2.append(card_2)
        deck_2.append(card_1)
    # print(winner)
    if deck_1 and deck_2:
        return deck_1, deck_2, None
    else:
        # print('Winner:', winner)
        return deck_1, deck_2, winner

def calculate_score(deck):
    deck = deck[::-1]
    score = 0
    for i in range(len(deck)):
        score += deck[i] * (i + 1)
    return score

if __name__ == "__main__":
    entries = GetLines()
    deck_1, deck_2 = EntriesToDecks(entries)
    deck_1, deck_2, winner = playgame(deck_1, deck_2)
    if winner == 1:
        score = calculate_score(deck_1)
    else:
        score = calculate_score(deck_2)
    print(score)