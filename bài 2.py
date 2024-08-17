def buy_icecream(budget, prices):
    a = {}

    position = 0
    
    for i in prices:
        x = budget - i 
        if x in a:
            return a[x], position
        else:
            a[i] = position
            position += 1
