# temperature analysis program
# exercise 3 of Day 14

# This exercise reinforces:
# • Aggregation
# • Statistical Analysis
# • Collection Traversal
# • Conditional Counting

temperatures = [72, 75, 71, 78, 80, 74, 69]

# calculate:
# - Average Temperature
# - Highest Temperature
# - Lowest Temperature

# extension -- number temperature above average

avg_temp = sum(temperatures) / len(temperatures)
highest_temp = max(temperatures)
lowest_temp = min(temperatures)
num_above_avg = 0
for temp in temperatures:
    if temp > avg_temp:
        num_above_avg += 1

print("Average Temperature:", avg_temp)
print("Highest Temperature:", highest_temp)
print("Lowest Temperature:", lowest_temp)
print("# Above Average Temperature:", num_above_avg)