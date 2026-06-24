stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "MSFT": 300
}
print("Stock Portfolio Tracker")
stock_name = input("Enter stock name (AAPL, TSLA, GOOG, MSFT): ").upper()
quantity = int(input("Enter quantity: "))
if stock_name in stock_prices:
    total_value = stock_prices[stock_name] * quantity
    print("\nStock:", stock_name)
    print("Price per share:", stock_prices[stock_name])
    print("Quantity:", quantity)
    print("Total Investment Value: $", total_value)
else:
    print("Stock not found!")