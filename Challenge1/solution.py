def calculate_coins(sum):
    representation_coins = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}
    COINS = (100, 50, 20, 10, 5, 2, 1)
    COINS = iter(COINS)
    coin = next(COINS)
    sum *= 100
    while sum > 0:
        if sum >= coin:
            sum -= coin
            representation_coins[coin] += 1
        else:
            coin = next(COINS)
    return representation_coins
