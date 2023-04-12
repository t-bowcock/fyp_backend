import neomodel

USER = "neo4j"
PWD = "Wxb1o7yVIFYk3R-FI1_8j6jZW1X41ERP8XVV7UvoP-E"
URI = "e05b191f.databases.neo4j.io"
neomodel.config.DATABASE_URL = f"neo4j+s://{USER}:{PWD}@{URI}"


class Item(neomodel.StructuredNode):
    name = neomodel.StringProperty()
    id = neomodel.IntegerProperty()
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
            "id": self.id,
            "quote": self.quote,
            "description": self.description,
            "quality": self.quality,
            "unlock": self.unlock,
            "effects": self.effects,
            "notes": self.notes,
        }

    def get_basic(self):
        return {"data": {"id": self.id}}


class Trinket(neomodel.StructuredNode):
    name = neomodel.StringProperty()
    id = neomodel.IntegerProperty()
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

    def get(self):
        return {
            "name": self.name,
            "id": self.id,
            "pool": self.pool,
            "quote": self.quote,
            "description": self.description,
            "tags": self.tags,
            "unlock": self.unlock,
            "effects": self.effects,
            "notes": self.notes,
        }

    def get_basic(self):
        return {"id": self.id}


class Character(neomodel.StructuredNode):
    name = neomodel.StringProperty()
    id = neomodel.IntegerProperty()

    def get(self):
        return {"name": self.name, "id": self.id}

    def get_basic(self):
        return {"id": self.id}


class SynergyRel(neomodel.StructuredRel):
    source = neomodel.IntegerProperty()
    destination = neomodel.IntegerProperty()
    description = neomodel.StringProperty()

    def get_all(self):
        results, _ = neomodel.db.cypher_query("MATCH (n)-[r:Synergy]->(m) RETURN n, r, m")
        rels = []
        for row in results:
            rel = self.inflate(row[1])
            rels.append(
                {
                    "source_id": rel.start_node().id,
                    "source": rel.start_node().name,
                    "destination_id": rel.end_node().id,
                    "destination": rel.end_node().name,
                    "description": rel.description,
                }
            )
        return rels

    def get_all_basic(self):
        results, _ = neomodel.db.cypher_query("MATCH (n)-[r:Synergy]->(m) RETURN n, r, m")
        rels = []
        for row in results:
            rel = self.inflate(row[1])
            rels.append(
                {
                    "id": f"{rel.start_node().id}{rel.end_node().id}",
                    "source": rel.start_node().id,
                    "target": rel.end_node().id,
                }
            )
        return rels


class InteractionRel(neomodel.StructuredRel):
    source = neomodel.IntegerProperty()
    destination = neomodel.IntegerProperty()
    description = neomodel.StringProperty()

    def get_all(self):
        results, _ = neomodel.db.cypher_query("MATCH (n)-[r:Interaction]->(m) RETURN n, r, m")
        rels = []
        for row in results:
            rel = self.inflate(row[1])
            rels.append(
                {
                    "source_id": rel.start_node().id,
                    "source": rel.start_node().name,
                    "destination_id": rel.start_node().id,
                    "destination": rel.end_node().name,
                    "description": rel.description,
                }
            )
        return rels

    def get_all_basic(self):
        results, _ = neomodel.db.cypher_query("MATCH (n)-[r:Synergy]->(m) RETURN n, r, m")
        rels = []
        for row in results:
            rel = self.inflate(row[1])
            rels.append(
                {
                    "id": f"{rel.start_node().id}{rel.end_node().id}",
                    "source": rel.start_node().id,
                    "target": rel.end_node().id,
                }
            )
        return rels
