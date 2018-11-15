from neomodel import StructuredNode, StringProperty, RelationshipTo, db


class Location(StructuredNode):
    name = StringProperty()


class IdentifierMixin:
    uuid = StringProperty()


class UserMixin:
    name = StringProperty()


class Patient(IdentifierMixin, UserMixin, StructuredNode):
    address = RelationshipTo(
        "Location", "HAS_ADDRESS"
    )

