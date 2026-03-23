def card_value(card):
    rank = card[0]
    if rank in ['J', 'Q', 'K']:
        return 10
    elif rank == 'A':
        return 11  # Будем рассматривать 11, учет 1 сделаем в подсчете
    else:
        return int(rank)

def calculate_score(hand):
    # Суммируем очки, учитывая что туз = 11 или 1
    score = 0
    aces = 0
    for card in hand:
        val = card_value(card)
        score += val
        if card[0] == 'A':
            aces += 1
    # Если перебор и есть тузы, меняем их стоимость с 11 на 1
    while score > 21 and aces:
        score -= 10
        aces -= 1
    return score