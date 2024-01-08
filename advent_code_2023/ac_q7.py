import heapq

scores = {
    "PAIR": 100,
    "TWO_PAIR": 200,
    "THREE_OF_KIND": 300,
    "FULL_HOUSE": 400,
    "FOUR_OF_KIND": 500,
    "FIVE_OF_KIND": 600,
}

card_map = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,  # Often 'T' is used to represent 10
    "J": 0,  # Jack
    "Q": 12,  # Queen
    "K": 13,  # King
    "A": 14,  # Ace is typically the highest in poker
}


def parse_file():
    lines = open("ac_q7.txt", "r").readlines()
    games = []
    for line in lines:
        game = line.strip().split(" ")
        games.append((game[0], int(game[1])))
    return games


def score_hand(hand: str) -> list[int]:
    hist = {}
    j_count = 0
    for card in hand:
        if card == "J":
            j_count += 1
        hist[card] = hist.get(card, 0) + 1

    heap = []

    for card, kinds in hist.items():
        if card != "J":
            heapq.heappush(heap, (-kinds, card))

    largest = 0
    second_largest = 0

    if len(heap) > 0:
        largest = heapq.heappop(heap)
        largest = -largest[0]
    if len(heap) > 0:
        second_largest = heapq.heappop(heap)
        second_largest = -second_largest[0]

    card_values = [card_map[card] for card in hand]

    largest += j_count

    if largest == 5:
        return [scores["FIVE_OF_KIND"]] + card_values
    if largest == 4:
        return [scores["FOUR_OF_KIND"]] + card_values
    if largest == 3 and second_largest == 2:
        return [scores["FULL_HOUSE"]] + card_values
    if largest == 3:
        return [scores["THREE_OF_KIND"]] + card_values
    if largest == 2 and second_largest == 2:
        return [scores["TWO_PAIR"]] + card_values
    if largest == 2:
        return [scores["PAIR"]] + card_values

    return [0] + card_values


def process_games(games: list[tuple[str, int]]):
    games = sorted(games, key=lambda game: score_hand(game[0]))

    acc = 0
    for i, game in enumerate(games):
        acc += (i + 1) * game[1]
    print(acc)


process_games(parse_file())

# print(score_hand("KTJJT"), score_hand("QQQJA"))
