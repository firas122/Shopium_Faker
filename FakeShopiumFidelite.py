import random
from faker import Faker
fake = Faker()
def generate_fidelite(db,cards_number):
    userIds = db.usersData.find().distinct('_id')
    for i in range(cards_number):
        fidobj = {"_id": fake.uuid4(),
                  "userId": random.choice(userIds),
                  "data": "619"+fake.ean(length=8),
                  "format": "EAN13"}
        db.fideliteData.insert_one(fidobj)