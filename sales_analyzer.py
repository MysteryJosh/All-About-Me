import csv

#To store our caluclations 
total_revenue = 0
product_quantity = {}
product_revenue = {}
daily_revenue = {}


with open("sales_data.csv", "r") as file:
    reader = csv.DictReader(file)
    print(reader.fieldnames)
    for row in reader:
        date = row["date"]
        product = row["product"]
        quantity = int(row["quantity"])
        price = float(row["price"])

# Revenue calculations
revenue = quantity * price

total_revenue += revenue

#Product Revenue
if product not in product_revenue:
    product_revenue[product] = 0
    product_quantity[product] = 0
    product_revenue[product] += revenue
    product_quantity[product] += quantity

#Revenue during the day
if date not in daily_revenue:
    daily_revenue[date] = 0
    daily_revenue[date] += revenue

#Day of highest revenue
highest_revenue_day = max(daily_revenue, key=daily_revenue.get)


#formatted report
with open("sales_report.txt", "w") as file:
    file.write("SALES REPORT\n")
    file.write("=" * 40 + "\n\n")
    file.write(f"Total Revenue: $ {total_revenue:.2f}\n\n")
    file.write("Revenue by Product:\n")
    file.write("_" * 40 + "\n")

    for product in product_revenue:
        file.write(f"{product}: "f"Quantity Sold = {product_quantity[product]}, "f"Revenue = $ {product_revenue[product]:.2f}\n")

    file.write("\n")
    file.write(f"Highest Revenue Day:{highest_revenue_day}\n")
    file.write(f"Revenue on Highest Day: "f"${daily_revenue[highest_revenue_day]:.2f}\n")


#Write Product Summary
with open("product_summary.csv", "w", newline="") as file:
    fieldnames = ["product", "total_quantity", "total_revenue"]

    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

    for product in product_revenue:
        writer.writerow({"product": product, "total_quantity": product_quantity[product], "total_revenue": f"{product_revenue[product]:.2f}"})

print("Sales analysis complete!")
print("Created sales_report.txt")
print("Created product_summary.csv")


    
   