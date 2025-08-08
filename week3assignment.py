def calculate_discount(price, discount_percent):
    if discount_percent >=20:
        discount_amount=price*(discount_percent/100)
        new_price=price-discount_amount
        return new_price
 #input values from the user
price =float(input("Enter the original price: "))
discount_percent= float(input("Enter Discount percentage: "))

new_price= calculate_discount(price,discount_percent)

print(f"The new price is: {new_price}")


