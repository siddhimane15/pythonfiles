menu={
    'Pizza':70,
    'Burger':50,
    'Pasta':60,
    'Salad':40,
    'Soda':20,
}


print( "Welcome to Siddhi Restaurant" )
print("Pizza:RS 70\nBurger:RS 50\nPasta:RS 60\nSalad:RS 40\nSoda:RS 20")


order_total=0
item_1=input("Enter your first item: ")
if item_1 in menu:
    order_total+=menu[item_1]
    print(f"Your item {item_1}has been added to your order")
else:
    print(f"Ordered item (={item_1}) is not available in the menu")


another_order=input("Do you want to order another item? (yes/no): ") 
if another_order=='yes':
    item_2=input("Enter your second item: ")
    if item_2 in menu:
        order_total+=menu[item_2]
        print(f"Your item {item_2} has been added to your order")
    else:
        print(f"Ordered item (={item_2}) is not available in the menu")   


print(f"Your total order amount is: RS {order_total}")        
