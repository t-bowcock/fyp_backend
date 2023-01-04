import neomodel

USER = "neo4j"
PWD = "Wxb1o7yVIFYk3R-FI1_8j6jZW1X41ERP8XVV7UvoP-E"
URI = "e05b191f.databases.neo4j.io"
neomodel.config.DATABASE_URL = f"neo4j+s://{USER}:{PWD}@{URI}"


class Item(neomodel.StructuredNode):
    name = neomodel.StringProperty()
    item_id = neomodel.IntegerProperty()
    quote = neomodel.StringProperty()
    description = neomodel.StringProperty()
    quality = neomodel.IntegerProperty()
    unlock = neomodel.StringProperty()
    effects = neomodel.StringProperty()
    notes = neomodel.StringProperty()

    item_synergy = neomodel.Relationship("Item", "SYNERGY")
    trinket_synergy = neomodel.Relationship("Trinket", "SYNERGY")
    character_synergy = neomodel.Relationship("Character", "SYNERGY")
    item_interaction = neomodel.Relationship("Item", "INTERACTION")
    trinket_interaction = neomodel.Relationship("Trinket", "INTERACTION")
    character_interaction = neomodel.Relationship("Character", "INTERACTION")

    def get(self):
        return {
            "name": self.name,
            "id": self.item_id,
            "quote": self.quote,
            "description": self.description,
            "quality": self.quality,
            "unlock": self.unlock,
            "effects": self.effects,
            "notes": self.effects,
        }


class Trinket(neomodel.StructuredNode):
    name = neomodel.StringProperty()
    trinket_id = neomodel.IntegerProperty()
    pool = neomodel.StringProperty()
    quote = neomodel.StringProperty()
    description = neomodel.StringProperty()
    tags = neomodel.StringProperty()
    unlock = neomodel.StringProperty()
    effects = neomodel.StringProperty()
    notes = neomodel.StringProperty()

    trinket_synergy = neomodel.Relationship("Trinket", "SYNERGY")
    character_synergy = neomodel.Relationship("Character", "SYNERGY")
    trinket_interaction = neomodel.Relationship("Trinket", "INTERACTION")
    character_interaction = neomodel.Relationship("Character", "INTERACTION")


class Character(neomodel.StructuredNode):
    name = neomodel.StringProperty()
    character_id = neomodel.IntegerProperty()


class SynergyRel(neomodel.StructuredRel):
    source = neomodel.IntegerProperty()
    destination = neomodel.IntegerProperty()
    description = neomodel.ArrayProperty()


class InteractionRel(neomodel.StructuredRel):
    source = neomodel.IntegerProperty()
    destination = neomodel.IntegerProperty()
    description = neomodel.ArrayProperty()
