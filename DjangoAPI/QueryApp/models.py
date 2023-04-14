import neomodel
import tqdm
import json

USER = "neo4j"
PWD = "Wxb1o7yVIFYk3R-FI1_8j6jZW1X41ERP8XVV7UvoP-E"
URI = "e05b191f.databases.neo4j.io"
neomodel.config.DATABASE_URL = f"neo4j+s://{USER}:{PWD}@{URI}"


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
                    "data": {
                        "id": f"{rel.start_node().id}{rel.end_node().id}",
                        "source": rel.start_node().id,
                        "target": rel.end_node().id,
                        "name": "Synergy",
                    }
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
                    "data": {
                        "source_id": rel.start_node().id,
                        "source": rel.start_node().name,
                        "destination_id": rel.start_node().id,
                        "destination": rel.end_node().name,
                        "description": rel.description,
                    }
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
                    "data": {
                        "id": f"{rel.start_node().id}{rel.end_node().id}",
                        "source": rel.start_node().id,
                        "target": rel.end_node().id,
                        "name": "interaction",
                    }
                }
            )
        return rels


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
        return {"data": {"id": self.id, "name": self.name}}


class Character(neomodel.StructuredNode):
    name = neomodel.StringProperty()
    id = neomodel.IntegerProperty()

    def get(self):
        return {"name": self.name, "id": self.id}

    def get_basic(self):
        return {"data": {"id": self.id, "name": self.name}}


def get_all():
    results, _ = neomodel.db.cypher_query("MATCH (n) OPTIONAL MATCH (n)-[r]-(m) RETURN n,r,m", resolve_objects=True)
    nodes = []
    elements = {"nodes": [], "edges": []}
    for result in tqdm.tqdm(results):
        if result[1] is None:
            elements["nodes"].append({"data": {"id": str(result[0].id), "name": result[0].name}})
            nodes.append(result[0].id)
        else:
            elements["edges"].append(
                {
                    "data": {
                        "id": f"{result[1].start_node().id}{result[1].end_node().id}",
                        "source": str(result[1].start_node().id),
                        "target": str(result[1].end_node().id),
                        "name": f"{result[1].start_node().name} (cc) {result[1].end_node().name}",
                    }
                }
            )
            if result[0].id not in nodes:
                elements["nodes"].append({"data": {"id": result[0].id, "name": result[0].name}})
                nodes.append(result[0].id)
    with open("result.json", "w") as f:
        json.dump(elements, f)
    return elements
