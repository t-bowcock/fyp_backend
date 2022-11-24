import neomodel

USER = "neo4j"
PWD = ""
URI = ""
neomodel.config.DATABASE_URL = f"neo4j+s://{USER}:{PWD}@{URI}"


class PassiveItem:
    pass


class ActiveItem:
    pass


class Trinket:
    pass


class Consumable:
    pass


class Character:
    pass


class ItemPool:
    pass


class Transformation:
    pass
