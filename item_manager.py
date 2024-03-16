# Including this module will allow you to manipulate your own Item instances.

from item import Item
from tabulate import tabulate
from itertools import groupby


def items_list(
    self,
):  # Return all Item instances owned by this item.
    items = [item for item in Item.item_all() if item.owner == self]
    return items


def pick_items(
    self, number, quantity
):  # Returns the specified quantitiy of the own Item instances corresponding to number.
    items = filter(lambda num: num["number"] == number, _stock(self))
    items = list(items)
    if len(items) == 0:
        return []
    elif len(items[0]["items"]) < quantity:
        return []
    else:
        return items[0]["items"][0:quantity]


def show_items(
    self,
):  # Output the inventory status of the Item instance you own in table format with the columns ["Number", "Product Name", "Amount", "Quantity"].
    table_data = []
    for stock in _stock(self):
        table_data.append(
            [
                stock["number"],
                stock["label"]["name"],
                stock["label"]["price"],
                len(stock["items"]),
            ]
        )
    print(
        tabulate(
            table_data,
            headers=["number", "product name", "amount", "quantity"],
            tablefmt="grid",
        )
    )  # Output results in table format using tabulate module


def _stock(self):  # Return the stock status of the Item instance you own.
    item_ls = self.items_list()
    item_ls.sort(key=lambda m: m.name)
    group_list = []
    for key, group in groupby(
        item_ls, key=lambda m: m.name
    ):  # Sort by Item instances that return the same value in Item#name.
        group_list.append(list(group))
    stock = []
    for index, item in enumerate(group_list):
        stock.append(
            {
                "number": index,
                "label": {"name": item[0].name, "price": item[0].price},
                "items": item,
            }
        )  # The classified Item instances are stored in items.
    return stock
