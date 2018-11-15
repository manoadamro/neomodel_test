import models
from neomodel import db


db.cypher_query("match(n) detach delete n;")

location = models.Location(name="thing")
location.save()

person = models.Person(uuid="1", name="dave")
person.save()

person.address.connect(location)
