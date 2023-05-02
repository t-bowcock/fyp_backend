import neomodel

USER = "neo4j"
PWD = "Wxb1o7yVIFYk3R-FI1_8j6jZW1X41ERP8XVV7UvoP-E"
URI = "e05b191f.databases.neo4j.io"
neomodel.config.DATABASE_URL = f"neo4j+s://{USER}:{PWD}@{URI}"


class SynergyRel(neomodel.StructuredRel):
    source = neomodel.IntegerProperty()
    destination = neomodel.IntegerProperty()
    description = neomodel.StringProperty()

    @staticmethod
    def get_all():
        results, _ = neomodel.db.cypher_query(
            "MATCH (n)-[r:Synergy]->(m) RETURN n.id, n.name, r.description, m.id, m.name"
        )
        rels = []
        for row in results:
            rels.append(
                {
                    "source_id": row[0],
                    "source": row[1],
                    "destination_id": row[3],
                    "destination": row[4],
                    "description": row[2],
                }
            )
        return rels

    @staticmethod
    def get(source, target):
        results, _ = neomodel.db.cypher_query(
            f"MATCH (n{{name:'{source}'}})-[r:Synergy]-(m{{name:'{target}'}}) RETURN r.description"
        )
        return {"description": results[0][0]}


class InteractionRel(neomodel.StructuredRel):
    source = neomodel.IntegerProperty()
    destination = neomodel.IntegerProperty()
    description = neomodel.StringProperty()

    @staticmethod
    def get_all():
        results, _ = neomodel.db.cypher_query(
            "MATCH (n)-[r:Interaction]->(m) RETURN n.id, n.name, r.description, m.id, m.name"
        )
        rels = []
        for row in results:
            rels.append(
                {
                    "source_id": row[0],
                    "source": row[1],
                    "destination_id": row[3],
                    "destination": row[4],
                    "description": row[2],
                }
            )
        return rels

    @staticmethod
    def get(source, target):
        results, _ = neomodel.db.cypher_query(
            f"MATCH (n{{name:'{source}'}})-[r:Interaction]-(m{{name:'{target}'}}) RETURN r.description"
        )
        return {"description": results[0][0]}


class Item(neomodel.StructuredNode):
    name = neomodel.StringProperty()
    id = neomodel.IntegerProperty()
    quote = neomodel.StringProperty()
    description = neomodel.StringProperty()
    quality = neomodel.IntegerProperty()
    unlock = neomodel.StringProperty()
    effects = neomodel.StringProperty()
    notes = neomodel.StringProperty()

    item_synergy = neomodel.Relationship("Item", "Synergy", model=SynergyRel)
    trinket_synergy = neomodel.Relationship("Trinket", "Synergy", model=SynergyRel)
    item_interaction = neomodel.Relationship("Item", "Interaction", model=InteractionRel)
    trinket_interaction = neomodel.Relationship("Trinket", "Interaction", model=InteractionRel)
    character_interaction = neomodel.Relationship("Character", "Interaction", model=InteractionRel)

    def format(self):
        return {
            "name": self.name,
            "id": self.id,
            "quote": self.quote,
            "description": self.description,
            "quality": self.quality,
            "unlock": self.unlock,
            "effects": self.effects,
            "notes": self.notes,
            "nodeType": "Item",
        }

    def get_basic(self):
        return {"data": {"id": self.id, "name": self.name}}


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

    trinket_synergy = neomodel.Relationship("Trinket", "Synergy", model=SynergyRel)
    trinket_interaction = neomodel.Relationship("Trinket", "Interaction", model=InteractionRel)
    character_interaction = neomodel.Relationship("Character", "Interaction", model=InteractionRel)

    def format(self):
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
        return {"data": {"id": self.id, "name": self.name}}


class Character(neomodel.StructuredNode):
    name = neomodel.StringProperty()
    id = neomodel.IntegerProperty()

    def format(self):
        return {"name": self.name, "id": self.id}

    def get_basic(self):
        return {"data": {"id": self.id, "name": self.name}}


def get_all():
    results, _ = neomodel.db.cypher_query(
        "MATCH (n) OPTIONAL MATCH (n)-[r]-(m) RETURN n.id,n.name,labels(n),m.id,m.name,labels(m)", resolve_objects=False
    )
    nodes = []
    elements = {"nodes": [], "edges": []}
    for result in results:
        if result[3] is None:
            elements["nodes"].append({"data": {"id": str(result[0]), "name": result[1], "nodeType": result[2][0]}})
            nodes.append((result[0], result[2][0]))
        else:
            elements["edges"].append(
                {
                    "data": {
                        "id": f"{result[0]}{result[3]}",
                        "source": str(result[0]),
                        "target": str(result[3]),
                        "name": f"{result[1]} (cc) {result[4]}",
                    }
                }
            )
            if (result[0], result[2][0]) not in nodes:
                elements["nodes"].append({"data": {"id": str(result[0]), "name": result[1], "nodeType": result[2][0]}})
                nodes.append((result[0], result[2][0]))
            if (result[3], result[5][0]) not in nodes:
                elements["nodes"].append({"data": {"id": str(result[3]), "name": result[4], "nodeType": result[5][0]}})
                nodes.append((result[3], result[5][0]))
    return elements
