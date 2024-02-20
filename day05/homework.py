# Define variables for book names and prices
book_1_name = "Book 1"
book_1_price = 20.0

book_2_name = "Book 2"
book_2_price = 25.0

book_3_name = "Book 3"
book_3_price = 30.0

book_4_name = "Book 4"
book_4_price = 18.0

book_5_name = "Book 5"
book_5_price = 22.0

book_6_name = "Book 6"
book_6_price = 27.0

book_7_name = "Book 7"
book_7_price = 35.0

book_8_name = "Book 8"
book_8_price = 40.0

book_9_name = "Book 9"
book_9_price = 32.0

book_10_name = "Book 10"
book_10_price = 38.0

# Apply discounts
# 10% discount for 5 books
book_1_price *= 0.9
book_2_price *= 0.9
book_3_price *= 0.9
book_4_price *= 0.9
book_5_price *= 0.9

# 20% discount for 5 books
book_6_price *= 0.8
book_7_price *= 0.8
book_8_price *= 0.8
book_9_price *= 0.8
book_10_price *= 0.8

# Print the discounted prices
print("Discounted prices after applying 10% discount:")
print(book_1_name, ": $", book_1_price)
print(book_2_name, ": $", book_2_price)
print(book_3_name, ": $", book_3_price)
print(book_4_name, ": $", book_4_price)
print(book_5_name, ": $", book_5_price)

print("\nDiscounted prices after applying 20% discount:")
print(book_6_name, ": $", book_6_price)
print(book_7_name, ": $", book_7_price)
print(book_8_name, ": $", book_8_price)
print(book_9_name, ": $", book_9_price)
print(book_10_name, ": $", book_10_price)