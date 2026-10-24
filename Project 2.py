# Stock Portfolio Tracker

# Prices of different stocks
stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 420,
    "AMZN": 200
}

total = 0
portfolio = []

print("=" * 50)
print("          STOCK PORTFOLIO TRACKER")
print("=" * 50)

print("\nAvailable Stocks:")

for name, price in stocks.items():
    print(name, "-", price)

# Ask how many stocks the user wants to add
n = int(input("\nHow many stocks do you want to add? "))

# Take stock details from the user
for i in range(n):
    print("\nStock", i + 1)

    name = input("Enter stock symbol: ").strip().upper()

    if name in stocks:
        quantity = int(input("Enter quantity: "))

        if quantity > 0:
            price = stocks[name]
            amount = price * quantity

            total = total + amount

            portfolio.append([name, quantity, price, amount])

            print("Investment for", name, "=", amount)
        else:
            print("Quantity must be greater than zero.")

    else:
        print("Stock not available!")

# Display the final portfolio
print("\n" + "=" * 50)
print("          YOUR STOCK PORTFOLIO")
print("=" * 50)

print(f"{'STOCK':<10}{'QTY':<8}{'PRICE':<12}{'TOTAL':<12}")
print("-" * 50)

for item in portfolio:
    print(f"{item[0]:<10}{item[1]:<8}{item[2]:<12}{item[3]:<12}")

print("-" * 50)
print(f"{'TOTAL INVESTMENT':<30}{total:>10}")
print("=" * 50)

# Save the portfolio in a text file
with open("portfolio.txt", "w") as file:
    file.write("STOCK PORTFOLIO TRACKER\n")
    file.write("=" * 40 + "\n\n")
    file.write(f"{'STOCK':<10}{'QTY':<8}{'PRICE':<12}{'TOTAL':<12}\n")
    file.write("-" * 40 + "\n")

    for item in portfolio:
        file.write(
            f"{item[0]:<10}{item[1]:<8}{item[2]:<12}{item[3]:<12}\n"
        )

    file.write("-" * 40 + "\n")
    file.write(f"{'TOTAL INVESTMENT':<30}{total:>10}\n")

print("\nPortfolio saved successfully in portfolio.txt")
print("Thank you for using Stock Portfolio Tracker!")
