def max_profit(prices):
    if len(prices) <= 1:
        return 0

    mid = len(prices) // 2
    left_prices = prices[:mid]
    right_prices = prices[mid:]
    print(f"  Divide: {prices} -> {left_prices} | {right_prices}")

    left_profit = max_profit(left_prices)
    right_profit = max_profit(right_prices)

    min_left = min(left_prices)
    max_right = max(right_prices)
    cross_profit = max_right - min_left

    best_profit = max(left_profit, right_profit, cross_profit, 0)

    print(f"  Conquer: Left={left_profit}, Right={right_profit}, Cross={cross_profit} -> Best={best_profit}")

    return best_profit

def get_prices():
    raw = input("Enter stock prices: ")
    try:
        return [int(x) for x in raw.split()]
    except ValueError:
        print("Invalid input. Please use numbers only.")
        return []

if __name__ == "__main__":
    prices = get_prices()
    if prices:
        print("\nTracking Division and Conquer Steps:")
        print("-" * 50)
        result = max_profit(prices)
        print("-" * 50)
        print(f"Final Max Profit: {result}\n")