# format specifiers = {:flags} format a value based on what flags are inserted

#.numberf = round to that many decimal places (fixed point)
#:(number) = allocated that many spaces
#:03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indticate positive value
# := = place sign to leftmost postion
# :  = insert a space before positive numbers
# :, = comma separator

price1 = 3432.14159
price2 = -9876.6554
price3 = 12976.3434

print(f"Price 1 is ${price1:+,.2f}")
print(f"Price 2 is ${price2:+,.2f}")
print(f"Price 3 is ${price3:+,.2f}")
