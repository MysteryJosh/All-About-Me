

item1_name = "Notebook"
item1_price = "4.99"
item1_qty = "2"

item2_name = "Pen Pack"
item2_price = "7.50"
item2_qty = "1"

item3_name = "Backpack"
item3_price = "34.99"
item3_qty = "1"

tax_rate = "0.075"   # 7.5% sales tax

# Change in Variables starts here

price_item1 = float(item1_price)
qty_item1 = int(item1_qty)
item1_total = price_item1 * qty_item1

price_item2 = float(item2_price)
qty_item2 = int(item2_qty)
item2_total = price_item2 * qty_item2

price_item3 = float(item3_price)
qty_item3 = int(item3_qty)
item3_total = price_item3 * qty_item3

rate_tax = float(tax_rate)

subtotal = item1_total + item2_total + item3_total
tax = subtotal * rate_tax
total = subtotal + tax

# Project starts here

print("=" * 40)
print("         STORE RECEIPT")
print("=" * 40)

print(f"Notebook:    ${price_item1} x {qty_item1}          ${item1_total}")
print(f"Pen Pack:    ${price_item2} x {qty_item2}           ${item2_total}")
print(f"Backpack:    ${price_item3} x {qty_item3}         ${item3_total}")
print("-" * 40)

print(f"Subtotal:                       ${subtotal:.2f}")
print(f"Tax(7.5%):                      ${tax:.2f}")
print("=" * 40)
print(f"TOTAL:                          ${total:.2f}")
print("=" * 40)

# And we are done