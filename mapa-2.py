# File for Map

from beautifultable import BeautifulTable

# Layout of Monu Territory (South Side 4x4 grid)
# MonuBorder is the starting base of the first quest
# MoNO is an area filled with hidden enemies
# MV is an empty area
# Mource is where you can find weapons, food and treatment
# Mountik is the mountain where the first amulet is hidden
# MonuLiberty is where the first quest is completed

table = BeautifulTable()
table.rows.append(["MonuBorder", "MoNo", "MoNo", "MV"])
table.rows.append(["MoNo", "MoNo", "MV",  "MoNo"])
table.rows.append(["MoNo", "Monurce", "MoNo", "MV"])
table.rows.append(["MonuLiberty", "Mountik", "MoNo",  "MoNo"])
table.set_style(BeautifulTable.STYLE_BOX_DOUBLED)


def monu_ter():
    """" Output Monu Territory"""
    print("\n")
    print("MONU VILLAGE: ")
    print(table)

print("The Monu Village Map!")

