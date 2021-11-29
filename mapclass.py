# File for map class

# Parent Class
class Map:
    """ Class map and its info"""

    def __init__(self, mapinfo):
        self.mapinfo = mapinfo

    def territories(self):
        print("This area is", self.mapinfo)


# Child Class
class Mapinfo(Map):
    """Represent info of each map tile"""

MonuBorder = Map("the starting base.")
MoNo = Map("the enemy zone. WATCH OUT! Enemies ahead!!")
MV = Map("empty.")
Monurce = Map("where you can find food and treatment.")
Mountik = Map("where the amulet is! You found it!")
MonuLiberty = Map("the ending base. Victory! You destroyed Zuko!")

