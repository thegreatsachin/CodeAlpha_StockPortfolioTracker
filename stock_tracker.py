import csv

def stock_portfolio_tracker():
    """
    A simple stock portfolio tracker that calculates the total investment value
    based on user input and a hardcoded price list.
    """
    # Hardcoded dictionary of stock prices
    stock_prices = {
        "AAPL": 180.00,
        "GOOGL": 140.50,
        "TSLA": 250.75,
        "MSFT": 330.20,
        "AMZN": 135.00
    }
    
    portfolio = {}
    total_investment = 0.0
    
    print("Welcome to the Stock Portfolio Tracker!")
    print("Enter 'done' when you have finished adding stocks.")
    
    while True:
        # User inputs stock names and quantity
        ticker = input("Enter stock ticker (e.g., AAPL): ").upper()
        
        if ticker == 'DONE':
            break
        
        if ticker not in stock_prices:
            print("Sorry, this stock is not in our price list. Please try another.")
            continue
            
        try:
            quantity = int(input(f"Enter quantity for {ticker}: "))
            if quantity <= 0:
                print("Quantity must be a positive number.")
                continue
        except ValueError:
            print("Invalid quantity. Please enter a whole number.")
            continue
            
        # Add to portfolio
        if ticker in portfolio:
            portfolio[ticker] += quantity
        else:
            portfolio[ticker] = quantity
            
        print(f"Added {quantity} shares of {ticker} to your portfolio.")

    # Calculate total investment value using basic arithmetic
    if not portfolio:
        print("No stocks were added to the portfolio.")
        return

    print("\n--- Your Portfolio ---")
    for ticker, quantity in portfolio.items():
        price = stock_prices[ticker]
        value = price * quantity
        total_investment += value
        print(f"{ticker}: {quantity} shares @ ${price:.2f} each, Value: ${value:.2f}")
    
    # Display total investment value
    print("----------------------")
    print(f"Total Investment Value: ${total_investment:.2f}")
    print("----------------------")

    # Optional: Save the result to a file
    save_file = input("\nDo you want to save the portfolio to a file? (yes/no): ").lower()
    if save_file == 'yes':
        file_format = input("Choose format (.txt or .csv): ").lower()
        if file_format == '.csv':
            filename = 'portfolio.csv'
            with open(filename, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['Ticker', 'Quantity', 'Price_per_Share', 'Total_Value'])
                for ticker, quantity in portfolio.items():
                    price = stock_prices[ticker]
                    value = price * quantity
                    writer.writerow([ticker, quantity, f"${price:.2f}", f"${value:.2f}"])
                writer.writerow(['TOTAL', '', '', f"${total_investment:.2f}"])
            print(f"Portfolio saved to {filename}")
        else:
            filename = 'portfolio.txt'
            with open(filename, 'w') as f:
                f.write("--- Your Portfolio ---\n")
                for ticker, quantity in portfolio.items():
                    price = stock_prices[ticker]
                    value = price * quantity
                    f.write(f"{ticker}: {quantity} shares @ ${price:.2f} each, Value: ${value:.2f}\n")
                f.write("----------------------\n")
                f.write(f"Total Investment Value: ${total_investment:.2f}\n")
            print(f"Portfolio saved to {filename}")

# Run the tracker
if __name__ == "__main__":
    stock_portfolio_tracker()
