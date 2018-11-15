from neomodel import StructuredNode, StringProperty, RelationshipTo


class Location(StructuredNode):
    name = StringProperty()


class Identifier:
    uuid = StringProperty()


class UserMixin:
    name = StringProperty()


class Person(Identifier, UserMixin, StructuredNode):
    address = RelationshipTo(
        ".personal_address.PersonalAddress", "HAS_PERSONAL_ADDRESS"
    )

