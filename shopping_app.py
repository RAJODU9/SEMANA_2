from customer import Customer
from item import Item
from seller import Seller

seller = Seller("DIC Store")
for i in range(10):
    Item("CPU", 40830, seller)
    Item("Memory", 13880, seller)
    Item("Motherboard", 28980, seller)
    Item("Power supply unit", 8980, seller)
    Item("PC case", 8727, seller)
    Item("3.5 inch HDD", 10980, seller)
    Item("2.5 inch SSD", 13370, seller)
    Item("M.2 SSD", 12980, seller)
    Item("CPU cooler", 13400, seller)
    Item("Graphic board", 23800, seller)

print("🤖 Please tell me your name")
customer = Customer(input())

print("🏧 Please enter the amount to charge to your wallet")
customer.wallet.deposit(int(input()))

print("🛍️ Start shopping")
end_shopping = False
while not end_shopping:
    print("📜Product List")
    seller.show_items()

    print("️️⛏ Please enter the product number")
    number = int(input())

    print("⛏ Please enter the product quantity")
    quantity = int(input())

    items = seller.pick_items(number, quantity)
    for item in items:
        customer.cart.add(item)
    print("🛒 Cart contents")
    customer.cart.show_items()
    print(f"🤑 Total amount: {customer.cart.total_amount()}")

    print("😭 Do you want to finish shopping? (yes/no)")
    end_shopping = input() == "yes"

print("💸 Do you want to confirm the purchase? (yes/no)")
if input() == "yes":
    seller.wallet.deposit(customer.cart.total_amount())
    customer.cart.check_out()

print("୨୧┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈Result┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈୨୧")
print(f"️🛍️ ️Property of {customer.name}")
customer.show_items()
print(f"😱👛 {customer.name}'s wallet balance: {customer.wallet.balance}")

print(f"📦 Inventory status of {seller.name}")
seller.show_items()
print(f"😻👛 {seller.name}'s wallet balance: {seller.wallet.balance}")

print("🛒 Cart contents")
customer.cart.show_items()
print(f"🌚 Total amount: {customer.cart.total_amount()}")
if (customer.wallet.balance - seller.wallet.balance) > 0:
    print(f"In your wallet: {customer.wallet.balance - seller.wallet.balance}")
else:
    print("Insufficient founds")


print("🎉 Finished")
