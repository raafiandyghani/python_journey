order_list = []
menu = {
    "mie ayam": 15000,
    "bakso bakar": 5000,
    "sate solo": 3000,
    "gultik": 10000,
    "air mineral": 5000,
    "es teh": 3000
}
print("Menu Hari ini: ")
for item, harga in menu.items():
    print(f"{item}: {harga}")

def order_food():
    while True:
        item = input("What do you want to order: ").lower().strip()
        if item == "done":
            print("Everything is done")
            break
        elif item in menu:
            order_list.append(item)
            print(f"{item} added to your order! Anything else? ")
        else:
            print("wrong input")
order_food()

def bon():
    total = 0
    for item in order_list:
        menu[item]
        total += menu[item]
        print(f"{item}: {menu[item]}")
    print("Total harga: ", total)
    return total

bon()

def payment():
    total = bon()
    pay = input (f"Your total is {total} Do you want to pay now yes/no?: ").lower()
    if pay == "yes":
        print("Payment successful. Thank you!")
    else:
        print("Okay, please pay later")

payment()