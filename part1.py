import models


location = models.Location(name="thing")
location.save()

person = models.Person(uuid="1", name="dave")
person.save()

person.address.connect(location)
