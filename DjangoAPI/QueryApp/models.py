import neomodel

USER = "neo4j"
PWD = "Wxb1o7yVIFYk3R-FI1_8j6jZW1X41ERP8XVV7UvoP-E"
URI = "e05b191f.databases.neo4j.io"
neomodel.config.DATABASE_URL = f"neo4j+s://{USER}:{PWD}@{URI}"


class SynergyRel(neomodel.StructuredRel):
    source = neomodel.StringProperty()
    destination = neomodel.StringProperty()
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


class InteractionRel(neomodel.StructuredRel):
    source = neomodel.StringProperty()
    destination = neomodel.StringProperty()
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


class Item(neomodel.StructuredNode):
    name = neomodel.StringProperty()
    id = neomodel.StringProperty()
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
    
    @staticmethod
    def get_all():
        results, _ = neomodel.db.cypher_query(
            "MATCH (n:Item) RETURN n"
        )
        items = []
        for row in results:
            items.append(
                {
                    "name": row[0]["name"],
                    "id": row[0]["id"],
                    "quote": row[0]["quote"],
                    "description": row[0]["description"],
                    "quality": row[0]["quality"],
                    "unlock": row[0]["unlock"],
                    "effects": row[0]["effects"],
                    "notes": row[0]["notes"],
                    "nodeType": "Item",
                }
            )
        return items
    
    @staticmethod
    def get(item_id: str):
        results, _ = neomodel.db.cypher_query(
            f"MATCH (n{{id:'{item_id}'}}) RETURN n"
        )
        return {
            "name": results[0][0]["name"],
            "id": results[0][0]["id"],
            "quote": results[0][0]["quote"],
            "description": results[0][0]["description"],
            "quality": results[0][0]["quality"],
            "unlock": results[0][0]["unlock"],
            "effects": results[0][0]["effects"],
            "notes": results[0][0]["notes"],
            "nodeType": "Item",
        }


class Trinket(neomodel.StructuredNode):
    name = neomodel.StringProperty()
    id = neomodel.StringProperty()
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

    @staticmethod
    def get_all():
        results, _ = neomodel.db.cypher_query(
            "MATCH (n:Trinket) RETURN n"
        )
        trinkets = []
        for row in results:
            trinkets.append(
                {
                    "name": row[0]["name"],
                    "id": row[0]["id"],
                    "pool": row[0]["pool"],
                    "quote": row[0]["quote"],
                    "description": row[0]["description"],
                    "tags": row[0]["tags"],
                    "unlock": row[0]["unlock"],
                    "effects": row[0]["effects"],
                    "notes": row[0]["notes"],
                    "nodeType": "Trinket",
                }
            )
        return trinkets
    
    @staticmethod
    def get(trinket_id: str):
        results, _ = neomodel.db.cypher_query(
            f"MATCH (n{{id:'{trinket_id}'}}) RETURN n"
        )
        return {
            "name": results[0][0]["name"],
            "id": results[0][0]["id"],
            "pool": results[0][0]["pool"],
            "quote": results[0][0]["quote"],
            "description": results[0][0]["description"],
            "tags": results[0][0]["tags"],
            "unlock": results[0][0]["unlock"],
            "effects": results[0][0]["effects"],
            "notes": results[0][0]["notes"],
            "nodeType": "Trinket",
        }


class Character(neomodel.StructuredNode):
    name = neomodel.StringProperty()
    id = neomodel.StringProperty()

    @staticmethod
    def get_all():
        results, _ = neomodel.db.cypher_query(
            "MATCH (n:Character) RETURN n"
        )
        characters = []
        for row in results:
            characters.append(
                {
                    "name": row[0]["name"],
                    "id": row[0]["id"],
                }
            )
        return characters
    
    @staticmethod
    def get(character_id: str):
        results, _ = neomodel.db.cypher_query(
            f"MATCH (n{{id:'{character_id}'}}) RETURN n"
        )
        return {
            "name": results[0][0]["name"],
            "id": results[0][0]["id"],
        }


def get_all():
    return custom_query("MATCH (n)-[r]-(m) RETURN n.id,n.name,labels(n),m.id,m.name,labels(m)")


def get_all_names():
    results, _ = neomodel.db.cypher_query("MATCH (n) RETURN n.name, n.id", resolve_objects=False)
    return {"names": [{"name": result[0], "id": result[1]} for result in results]}


def custom_query(query: str):
    results, _ = neomodel.db.cypher_query(query, resolve_objects=False)
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


def get_rel(source, target):
    results, _ = neomodel.db.cypher_query(
        f"MATCH (n{{id:'{source}'}})-[r]-(m{{id:'{target}'}}) RETURN n.name, r.description, m.name"
    )
    return {"source": results[0][0], "description": results[0][1], "target": results[0][2]}
