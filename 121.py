prices = [7,1,5,3,6,4]

# min = min(prices)
# day_of_buy = prices.index(min)

# day_of_sell = day_of_buy
# max = min

# for i in range(min,len(prices)):
#     if(prices[i] > max):
#         max = prices[i]
#         day_of_sell = prices.index(max)

# max_profit = max - min
# print(max_profit)

min_price = prices[0]
day_of_buy = 0

max_profit = 0
buy = sell = 0

for i in range(1, len(prices)):
    if prices[i] < min_price:
        min_price = prices[i]
        day_of_buy = i
    elif prices[i] - min_price > max_profit:
        max_profit = prices[i] - min_price
        buy = day_of_buy
        sell = i
print(max_profit)   # 5
print(buy, sell)    # 1 4