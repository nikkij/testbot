import requests
import uuid
from faker import Faker
from faker.providers import person
from faker.providers import misc

fake = Faker()
fake.add_provider(person)
fake.add_provider(misc)

short_uuid = str(uuid.uuid4().fields[0])

if fake.boolean(90) == True:
  status = "success"
else:
  status = "failed"

r = requests.get('http://testbot-prod.c5jy5nic6y.us-west-2.elasticbeanstalk.com/runs/?format=json')
#r = requests.post('http://127.0.0.1:8000/runs/?format=json', data = {
    "label": "fakebot:" + short_uuid,
    "status": status,
    "duration": fake.pyint(),
    "submitter": fake.first_name()
})
print(r.status_code)
