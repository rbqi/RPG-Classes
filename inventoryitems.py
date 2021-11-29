# File for inventories

from beautifultable import BeautifulTable

# List of inventories for healing and comsuming items
healing_items = ["bandages", "medical kit"]
consumables_items = ["apples", "water", "soda"]

# Table for inventory healing items
healing = BeautifulTable()
healing.rows.append([3, "bandages"])
healing.rows.append([1, "medical kit"])
healing.columns.header = ["In stock", "Items"]
healing.set_style(BeautifulTable.STYLE_COMPACT)
print("\n")
# Table for inventory consumables items
consumables = BeautifulTable()
consumables.rows.append([2, "apples"])
consumables.rows.append([2, "water"])
consumables.rows.append([0, "soda"])
consumables.columns.header = ["In stock", "Items"]
consumables.set_style(BeautifulTable.STYLE_COMPACT)


def healing_inv():
    """" Output healing inventory"""
    print("HEALING ITEMS: \n")
    print(healing)


def consumables_inv():
    """" Output consumables inventory"""
    print("CONSUMABLE ITEMS:\n")
    print(consumables)

