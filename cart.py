from ownable import Ownable


class Cart(Ownable):
    from item_manager import show_items

    def __init__(self, owner):
        super().__init__()
        self.set_owner(owner)
        self.items = []

    def items_list(self):
        return self.items

    def add(self, item):
        self.items.append(item)

    def total_amount(self):
        price_list = []
        for item in self.items:
            price_list.append(item.price)
        return sum(price_list)

    def clear_cart(self):
        self.items = []

    def check_out(self):
        if self.owner.wallet.balance >= self.total_amount():
            self.owner.wallet.balance -= self.total_amount()
            self.owner.cart.owner.wallet.deposit(self.total_amount())
            for item in self.items:
                item.set_owner(self.owner)
            self.clear_cart()
        else:
            print("You can't purchese any product")
        # Delete pass when coding the check_out method.
        # Requirements
        # - The purchase amount of all items in the cart (Cart#items) is transferred from the cart owner's wallet to the item owner's wallet.
        # - Ownership of all items in the cart (Cart#items) is transferred to the cart owner.
        # - The contents of the cart (Cart#items) are empty.
        # Tip
        # - Cart owner's wallet ==> self.owner.wallet
        # - Item owner's wallet ==> item.owner.wallet
        # - Money will be transferred ==> That amount will be withdrawn from (?)'s wallet and deposited into (?)'s wallet.
        # - Item ownership is transferred to the cart owner ==> Rewrite owner (item.owner = ?)
