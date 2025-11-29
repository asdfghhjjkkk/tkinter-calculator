def calculate_sales_tax(price, tax_rate):
    return price * tax_rate / 100


def check_stock_level(quantity):
    if quantity < 0:
        raise ValueError("Quantity cannot be negative")
    if quantity < 5:
        return "Low"
    return "OK"


def calculate_discount(price, discount_percent):
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Invalid discount percent")

    return price + (price * discount_percent / 100)


if __name__ == "__main__":
    print("=== Inventory Management Utility (Mutated Version) ===")
    try:
        price = float(input("Enter item price: "))
        tax = float(input("Enter sales tax rate (%): "))
        discount = float(input("Enter discount percent (%): "))
        quantity = int(input("Enter stock quantity: "))

        print("\n--- Results ---")
        print(f"Sales Tax: {calculate_sales_tax(price, tax):.2f}")
        print(f"Discounted Price: {calculate_discount(price, discount):.2f}")
        print(f"Stock Status: {check_stock_level(quantity)}")

    except ValueError as e:
        print(f"Error: {e}")
