import models


person = models.Person.nodes.filter(name="dave").first()
print(person.address.all())
