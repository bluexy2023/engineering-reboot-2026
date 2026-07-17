# sales report python program
# Exercise 1 of Day 14

# create a list of sales values

sales = [120, 250, 90, 310, 175]

# calculate
# - Total Sales:
# - Average Sale:
# - Highest Sale:
# - Lowest Sale:

total_sales = sum(sales)
average_sale = total_sales / len(sales)
highest_sale = max(sales)
lowest_sale = min(sales)

print("Total Sales:", total_sales)
print("Average Sale:", average_sale)
print("Highest Sale:", highest_sale)
print("Lowest Sale:", lowest_sale)
