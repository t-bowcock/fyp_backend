import neomodel

USER = "neo4j"
PWD = "WQx-anGO1rkQ-Ua4JVDMKCKEf2hH9vqDDL-Ub0yd26A"
URI = "8d635bf0.databases.neo4j.io"
neomodel.config.DATABASE_URL = f"neo4j+s://{USER}:{PWD}@{URI}"


class Movie(neomodel.StructuredNode):
    released = neomodel.IntegerProperty()
    tagline = neomodel.StringProperty()
    title = neomodel.StringProperty()


class Person(neomodel.StructuredNode):
    name = neomodel.StringProperty()
    born = neomodel.IntegerProperty()

    acted_in = neomodel.RelationshipTo("Movie", "ACTED_IN")
    directed = neomodel.RelationshipTo("Movie", "DIRECTED")
    follows = neomodel.RelationshipTo("Person", "ACTED_IN")
    produced = neomodel.RelationshipTo("Movie", "PRODUCED")
    reviewed = neomodel.RelationshipTo("Movie", "REVIEWED")
    wrote = neomodel.RelationshipTo("Movie", "WROTE")


class ActedInRel(neomodel.StructuredRel):
    roles = neomodel.ArrayProperty(neomodel.StringProperty())


class ReviewedRel(neomodel.StructuredRel):
    rating = neomodel.IntegerProperty()
    summary = neomodel.StringProperty()
