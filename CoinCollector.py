class CoinCollector:
    # constructor so you cannot instantiate this class
    def __init__(self):
        pass

    def parseChange(coins):
        """
        Takes in coins entered by the user and adds the coin
        count to the respective variables
        """
        penny_count = 0
        nickle_count = 0
        dime_count = 0
        quarter_count = 0
        half_dollar_count = 0
        whole_dollar_count = 0
        total_coin_amount_count = 0
        invalid_coins = []
        for coin in coins:
            if coin.upper() == 'P':
                penny_count += 1
            elif coin.upper() == 'N':
                nickle_count += 1
            elif coin.upper() == 'D':
                dime_count += 1
            elif coin.upper() == 'Q':
                quarter_count += 1
            elif coin.upper() == 'H':
                half_dollar_count += 1
            elif coin.upper() == 'W':
                whole_dollar_count += 1
            else:
                invalid_coins.append(coin)
        if invalid_coins:
            print(f"Invalid coin found: {' '.join(invalid_coins)}")
        penny_total = penny_count * 1
        nickel_total = nickle_count * 5
        dime_total = dime_count * 10
        quarter_total = quarter_count * 25
        half_dollar_total = half_dollar_count * 50
        whole_dollar_total = whole_dollar_count * 100
        total_coin_amount_count = penny_total + nickel_total + dime_total + \
            quarter_total + half_dollar_total + whole_dollar_total

        return total_coin_amount_count
