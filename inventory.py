
inventory = {
    "laptop": {"price": 999.99, "quantity": 15},
    "mouse": {"price": 29.99, "quantity": 50},
    "keyboard": {"price": 25.19, "quantity": 40},
    "phone": {"price": 849.99, "quantity": 10}
}

# Print products in formatted display

print("=" * 40)
print("                Inventory")
print("=" * 40 + "\n")

for key, info in inventory.items(): 
    print(key)
    print(f" Price: {info['price']}")
    print(f" Quantity: {info['quantity']}\n")


# Inventory Calculations
laptop_total = inventory["laptop"]["price"] * inventory["laptop"]["quantity"]
mouse_total = inventory["mouse"]["price"] * inventory["mouse"]["quantity"]
keyboard_total = inventory["keyboard"]["price"] * inventory["keyboard"]["quantity"]
phone_total = inventory["phone"]["price"] * inventory["phone"]["quantity"]

inventory_total = laptop_total + mouse_total + keyboard_total + phone_total

# Display inventory total value

print("----- Price x Quantity -----\n")


print(f"Laptop: ${inventory["laptop"]["price"]} * {inventory["laptop"]["quantity"]} = ${laptop_total}")
print(f"Mouse: ${inventory["mouse"]["price"]} * {inventory["mouse"]["quantity"]} = ${mouse_total}")
print(f"Keyboard: ${inventory["keyboard"]["price"]} * {inventory["keyboard"]["quantity"]} = ${keyboard_total}")
print(f"Phone: ${inventory["phone"]["price"]} * {inventory["phone"]["quantity"]} = ${phone_total}\n")

print(f"Sum Total: ${inventory_total}\n")

#Look up specific product

search = input("Look up a product (enter name): ")

product = inventory.get(search)

if product:
    print(f"\nFound: {product}")
else:
    print(f"No product found for {search}.\n")

#Update inventory
print("----- Update Product Quantity -----\n")

update_product = input("Enter a product to update: ")

if update_product in inventory:
    new_quantity = int(input("Enter the new quantity: "))
    inventory[update_product]["quantity"] = new_quantity
    print(f"{update_product} quantity to {inventory[update_product]["quantity"]}")
    
else:
    print("Prodcut not found.")

for key, info in inventory.items(): 
    print(key)
    print(f" Price: {info['price']}")
    print(f" Quantity: {info['quantity']}\n")

print(f"{update_product} quantity updated successfully!")

# Low-stock alert
low_stock = set()

for name, info in inventory.items():
    if info["quantity"] < 10:
        low_stock.add(name)



