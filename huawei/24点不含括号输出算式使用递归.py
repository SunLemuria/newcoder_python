def calculate(card, s, t):
    if not card:
        if s == 24:
            result.append(t)
            return True
        return False
    for i in range(len(card)):
        c = d[cards[i]]
        if calculate(card[:i] + card[i + 1:], s + c, t + '+' + card[i]):
            return True
        if calculate(card[:i] + card[i + 1:], s - c, t + '-' + card[i]):
            return True
        if calculate(card[:i] + card[i + 1:], s * c, t + '*' + card[i]):
            return True
        if s % c == 0:
            if calculate(card[:i] + card[i + 1:], s / c, t + '/' + card[i]):
                return True
    return False


while True:
    try:
        cards = input().split()
        if 'joker' in cards or 'JOKER' in cards:
            print('ERROR')
            continue
        d = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
             '8': 8, '9': 0, '10': 10, 'J': 11, 'Q': 12, 'K': 13}
        result = []

        for i in range(len(cards)):
            c = d[cards[i]]
            if calculate(cards[:i] + cards[i + 1:], c, cards[i]):
                break

        if not result:
            print('NONE')
        else:
            print(result[0])

    except:
        break