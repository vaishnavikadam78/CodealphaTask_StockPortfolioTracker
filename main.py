import csv
import datetime

def stock_portfolio_tracker():
    print("📊 Welcome to Stock Portfolio Tracker")
    print("Enter stock symbols and quantities. Type 'done' when finished.\n")

    # Hardcoded stock prices (you can expand this list)
    stock_prices = {
        "AAPL": 180,   # Apple
        "TSLA": 250,   # Tesla
        "GOOGL": 135,  # Google
        "MSFT": 320,   # Microsoft
        "AMZN": 140    # Amazon
    }

    portfolio = {}  # to store user inputs

    
    while True:
        stock = input("Enter stock symbol (or 'done' to finish): ").upper().strip()

        if stock == "DONE":
            break

        if stock not in stock_prices:
            print("❌ Stock not found in database. Available:", ", ".join(stock_prices.keys()))
            continue

        try:
            qty = int(input(f"Enter quantity of {stock}: "))
            if qty <= 0:
                print("⚠ Quantity must be positive.")
                continue
            # add to portfolio
            portfolio[stock] = portfolio.get(stock, 0) + qty
        except ValueError:
            print("⚠ Please enter a valid number for quantity.")

    
    total_value = 0
    print("\n📌 Your Portfolio Summary:")
    print("-" * 40)
    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        value = qty * price
        total_value += value
        print(f"{stock} - Quantity: {qty}, Price: ${price}, Value: ${value}")
    print("-" * 40)
    print(f"💰 Total Investment Value: ${total_value}")

    
    save_choice = input("\nDo you want to save portfolio to file? (yes/no): ").lower()
    if save_choice == "yes":
        filename = f"portfolio_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Stock", "Quantity", "Price", "Value"])
            for stock, qty in portfolio.items():
                writer.writerow([stock, qty, stock_prices[stock], qty * stock_prices[stock]])
            writer.writerow(["Total", "", "", total_value])
        print(f"✅ Portfolio saved to {filename}")



if __name__ == "__main__":
    stock_portfolio_tracker()


