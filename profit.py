def profit(prices_list, day_of_purchase):
    #takes a list of prices that a product can be sold for, and a day to make an intial purchase.
    #function then scans the prices from this 'day' onwards, and returns the maximum profit that can be earned
    #if no profit to be made, or an invalid date is entered, the function returns 0
    try:
        max_profit = 0
        if (day_of_purchase + 1) > len(prices_list):
            return 0
        else:
            for i in prices_list[day_of_purchase + 1:]:
                print (i)
                if i - prices_list[day_of_purchase] > max_profit:
                    max_profit = i - prices_list[day_of_purchase]
        return max_profit
    except:
        return 0
