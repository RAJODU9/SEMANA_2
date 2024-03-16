from ownable import Ownable


class Item(Ownable):
    instances = []

    def __init__(self, name, price, owner=None):
        super().__init__()
        self.name = name
        self.price = price
        self.set_owner(owner)
        # When an Item instance is created, the Item instance (self) is stored in a class variable called instances.
        Item.instances.append(self)

    def label(self):
        return {"name": self.name, "price": self.price}

    @staticmethod
    def item_all():
        # Return instances ==> Item.item_all() returns all Item instances that have been generated so far.
        return Item.instances
