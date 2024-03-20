def calculate_discount(price,discount_price):
    if discount_price >=20:
        discounted_price=(price*80/100)
        print(discounted_price)
    else:
        print(price)
original_price=float(input("Enter original price:"))
discount_percentage=float(input("Enter discount_percentage:"))
final_price=calculate_discount(original_price,discount_percentage)
