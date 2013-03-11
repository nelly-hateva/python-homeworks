def calculate_coins(sum_):
    COINS_NOMINAL = (100, 50, 20, 10, 5, 2, 1)
    coin_distribution = {}
    sum_ = round(sum_*100)
    for coin in COINS_NOMINAL:
        coin_distribution[coin] = sum_ // coin
        sum_ %= coin
    return coin_distribution
