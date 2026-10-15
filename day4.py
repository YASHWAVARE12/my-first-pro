print("Wellcome to harshu RESTURENT")

MENU = {
    'panner': 140,
    'pasta': 60,
    'roti': 25
}

print(MENU)

oder_total = 0
 
item_1 = input("enter item name : ")

if item_1 in MENU:
    oder_total += MENU[item_1]
    print("item 1 is added in card succesfully")
else:
    print("item 1 is not avilable in menu ") 

another_item = input("enter the name of another item you want to order :yes or no ")
if another_item == "yes":
    item_2 = input("aname of another item from menu :")
    if item_2 in MENU: 
        oder_total += MENU[item_2]                      #+= is same as a + b 
        print("item 2 is addeed in card succesfully ")

    else:
        print("item 2 is not avilable in menu ")

else:
    print("okay, than you for visting your resturant ")
    

print(f"total price of item is {oder_total}")      #f is used to show value in string 
