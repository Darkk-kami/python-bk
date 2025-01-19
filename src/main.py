def add_to_cart(cart, item_name, price, *discounts, **kwargs):
    """
    Add an item to cart
    """
    item_exists = next((item for item in cart if item['name'] == item_name), None)

    discount_factor = 1
    for discount in discounts:
        discount_factor *= (1 - discount / 100)

    final_price = price * discount_factor

    if item_exists:
        item_exists['quantity'] += 1
        item_exists['price'] += final_price
    else:
        item = {
            "name": item_name,
            "price": final_price,
            "quantity": 1
        }
        item.update(kwargs)
        cart.append(item)

    return cart

def display_cart(cart):
    """
    Display the cart: items, final prices, and total cost.
    """
    total_cost = 0
    print("--- Cart Summary ---")
    for item in cart:
        item_details = ", ".join([f"{key}={value}" for key, value in item.items() if key not in ['name', 'price', 'quantity']])
        print(f"{item['name']} - ${item['price']:.2f} ({item_details})")
        total_cost += item['price']
    
    print(f"Total Cost: ${total_cost:.2f}")


def main():
    cart = []
    while True:
        item_name = input("Enter item name (or 'done' to finish): ").strip()
        if item_name.lower() == 'done':
            break
        if not item_name:
            print("Item name cannot be empty. Please enter a valid item name or type 'done' to finish.")
            continue

        while True:
            try:
                item_price = float(input("Enter item price: ").strip())
                if item_price <= 0:
                    raise ValueError("Price must be a positive number.")
                break
            except ValueError as e:
                print(f"Invalid input for price: {e}. Please enter a valid positive number.")

        discounts = input("Enter discounts (if any, separated by spaces): ").strip()
        discounts = []
        if discounts:
            try:
                discounts = [float(value) for value in discounts.split() if value.strip()]
                if any(d < 0 or d > 100 for d in discounts):
                    print("Discounts must be between 0 and 100. Please enter valid discounts.")
                    discounts.clear()
            except ValueError:
                print("Invalid input for discounts. Please enter valid numbers.")

        description = input("Enter item details (e.g., color=red size=large): ").strip()
        item_details = {detail.split('=')[0]: detail.split('=')[1] for detail in description.split() if '=' in detail}

        cart = add_to_cart(cart, item_name, item_price, *discounts, **item_details)

    display_cart(cart)


if __name__ == "__main__":
    main()