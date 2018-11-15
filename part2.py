from neomodel import db
import models

query = """
    match (p:Patient)-[r:HAS_ADDRESS]-(l:Location {name: {location_id}})
    return p
"""

results, meta = db.cypher_query(
    query, {"location_id": "thing"}
)

patients = [models.Patient.inflate(row[0]) for row in results]

print(patients)
print([patient.address.single() for patient in patients])
