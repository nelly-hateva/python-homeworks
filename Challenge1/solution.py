COINS = (100, 50, 20, 10, 5, 2, 1)


def calculate_coins(amount):
    coins_representation = {}
    amount_in_coins = round(amount*100)
    for coin in sorted(COINS, reverse=True):
        coins_representation[coin] = amount_in_coins // coin
        amount_in_coins %= coin
    return coins_representation
