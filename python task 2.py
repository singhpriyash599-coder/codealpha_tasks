stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 300,
    "GOOGL": 140,
    "AMZN": 130
}

def stock_tracker():
    portfolio = {}
    total_investment = 0

    print("Welcome to the Stock Portfolio Tracker!")
    print("Available stocks:", ", ".join(stock_prices.keys()))

    while True:
        stock = input("Enter stock symbol (or 'done' to finish): ").upper()
        if stock == "DONE":
            break
        if stock not in stock_prices:
            print("Stock not found in price list. Try again.")
            continue

        try:
            quantity = int(input(f"Enter quantity of {stock}: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        portfolio[stock] = portfolio.get(stock, 0) + quantity
        total_investment += stock_prices[stock] * quantity

    print("\nYour Portfolio Summary:")
    for stock, qty in portfolio.items():
        print(f"{stock}: {qty} shares @ ${stock_prices[stock]} each = ${stock_prices[stock] * qty}")

    print("\nTotal Investment Value: $", total_investment)

    save = input("Do you want to save the result to a file? (y/n): ").lower()
    if save == "y":
        with open("portfolio.txt", "w") as f:
            f.write("Portfolio Summary:\n")
            for stock, qty in portfolio.items():
                f.write(f"{stock}: {qty} shares @ ${stock_prices[stock]} each = ${stock_prices[stock] * qty}\n")
            f.write(f"\nTotal Investment Value: ${total_investment}\n")
        print("Portfolio saved to portfolio.txt")
stock_tracker()