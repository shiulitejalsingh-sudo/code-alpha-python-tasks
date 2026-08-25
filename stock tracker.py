"""
TASK 2: Stock Portfolio Tracker
Build a simple stock tracker that calculates total investment based on
manually defined stock prices.
"""

import csv
from datetime import datetime

# Hardcoded stock prices (in dollars)
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 145,
    "MSFT": 330,
    "NFLX": 470,
}


def display_available_stocks():
    print("Available stocks and prices:")
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol}: ${price}")
    print()


def get_portfolio_input():
    """Collect stock symbols and quantities from the user."""
    portfolio = {}

    print("Enter stock symbol and quantity (type 'done' when finished).\n")
    while True:
        symbol = input("Stock symbol: ").upper().strip()
        if symbol == "DONE":
            break

        if symbol not in STOCK_PRICES:
            print(f"'{symbol}' not found in price list. Try again.\n")
            continue

        qty_input = input(f"Quantity of {symbol}: ").strip()
        if not qty_input.isdigit():
            print("Please enter a valid whole number for quantity.\n")
            continue

        quantity = int(qty_input)
        portfolio[symbol] = portfolio.get(symbol, 0) + quantity
        print(f"Added {quantity} shares of {symbol}.\n")

    return portfolio


def calculate_total(portfolio):
    """Calculate total investment value and a per-stock breakdown."""
    breakdown = []
    total = 0
    for symbol, quantity in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = price * quantity
        total += value
        breakdown.append((symbol, quantity, price, value))
    return breakdown, total


def display_summary(breakdown, total):
    print("\n--- Portfolio Summary ---")
    print(f"{'Symbol':<8}{'Qty':<6}{'Price':<10}{'Value':<10}")
    for symbol, quantity, price, value in breakdown:
        print(f"{symbol:<8}{quantity:<6}${price:<9}${value:<9}")
    print("-" * 34)
    print(f"Total investment value: ${total}\n")


def save_to_file(breakdown, total):
    """Optionally save the results to a .txt or .csv file."""
    choice = input("Save results to a file? (y/n): ").lower().strip()
    if choice != "y":
        return

    file_format = input("Choose format - txt or csv: ").lower().strip()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    if file_format == "csv":
        filename = f"portfolio_{timestamp}.csv"
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Symbol", "Quantity", "Price", "Value"])
            for row in breakdown:
                writer.writerow(row)
            writer.writerow(["", "", "Total", total])
        print(f"Saved to {filename}")

    elif file_format == "txt":
        filename = f"portfolio_{timestamp}.txt"
        with open(filename, "w") as f:
            f.write("Portfolio Summary\n")
            f.write(f"{'Symbol':<8}{'Qty':<6}{'Price':<10}{'Value':<10}\n")
            for symbol, quantity, price, value in breakdown:
                f.write(f"{symbol:<8}{quantity:<6}${price:<9}${value:<9}\n")
            f.write(f"\nTotal investment value: ${total}\n")
        print(f"Saved to {filename}")

    else:
        print("Unrecognized format. Skipping save.")


def main():
    print("=== Stock Portfolio Tracker ===\n")
    display_available_stocks()

    portfolio = get_portfolio_input()
    if not portfolio:
        print("No stocks entered. Exiting.")
        return

    breakdown, total = calculate_total(portfolio)
    display_summary(breakdown, total)
    save_to_file(breakdown, total)


if __name__ == "__main__":
    main()
