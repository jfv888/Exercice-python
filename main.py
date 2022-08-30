Prices = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]


def Buy_low_sell_high(Prices):
    Range = 0
    Diff = 0
    Buy_price = 0
    Sell_price = 0
    for x in Prices:
        Range = Range + 1
        for y in Prices[Range:len(Prices)]:
            if (y - x) > Diff:
                Buy_price = x
                Sell_price = y
                Diff = (y - x)
    print("Buy price: " + str(Buy_price))
    print("Sell price: " + str(Sell_price))
    print("Profit: " + str(Diff))


Buy_low_sell_high(Prices)



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


