from neomodel import StructuredNode, StringProperty, RelationshipTo, db


class Location(StructuredNode):
    name = StringProperty()


class Identifier:
    uuid = StringProperty()


class UserMixin:
    name = StringProperty()


class Person(Identifier, UserMixin, StructuredNode):
    address = RelationshipTo(
        "Location", "HAS_PERSONAL_ADDRESS"
    )

