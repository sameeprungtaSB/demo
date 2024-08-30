import uuid
from cassandra.cqlengine import columns
from django_cassandra_engine.models import DjangoCassandraModel
import hashlib


class ExampleModel(DjangoCassandraModel):
     example_id    = columns.UUID(primary_key=True, default=uuid.uuid4)
     example_type  = columns.Integer(index=True)
     created_at    = columns.DateTime()
     description   = columns.Text(required=False)

class User(DjangoCassandraModel):
    email = columns.Text(primary_key=True)
    username = columns.Text()
    password = columns.Text()
    phone_number = columns.Text()