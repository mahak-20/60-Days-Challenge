prices = [7, 1, 5, 3, 6, 4]

min_price = prices[0]
max_profit = 0

buy_day = 0
sell_day = 0
temp_buy_day = 0

for i in range(1, len(prices)):
    if prices[i] < min_price:
        min_price = prices[i]
        temp_buy_day = i
    profit = prices[i] - min_price

    if profit > max_profit:
        max_profit = profit
        buy_day = temp_buy_day
        sell_day = i

print("Max Profit:", max_profit)

if max_profit > 0:
    print("Buy on day", buy_day +1)
    print("Sell on day", sell_day + 1)
else:
    print("No profit possible.")