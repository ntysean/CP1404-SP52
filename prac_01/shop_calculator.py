number_of_items = int(input("How many items: "))
while number_of_items <= 0:
    print("Invalid number of items.")
    number_of_items = int(input("How many items: "))


total_price = 0
for i in range(0,number_of_items):
    price_of_item = float(input("How much is item: $"))
    while price_of_item <= 0:
        print("Price of item invalid")
        price_of_item = float(input("How much is item: $"))
    total_price += price_of_item
if total_price > 100:
    total_price = 0.9*total_price
print("Total price is $"+str(total_price))



