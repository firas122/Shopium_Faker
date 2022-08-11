import random
from faker import Faker

fake = Faker()

def generate_offers(db,offers_number):
    productids = db.productsData.find().distinct('_id')
    for i in range(offers_number):
        offreobj = {"_id": fake.uuid4(),
                    "startDate": str(fake.date_time()),
                    "expirationDate": str(fake.date_time()),
                    "condition": "conditions set by fabricant",
                    "description": "description of the offer",
                    "quantity": random.randint(1, 20),
                    "percentage": random.randint(0, 75),
                    "product": random.choice(productids),
                    "isLiked": fake.boolean(chance_of_getting_true=75),
                    "createdAt": str(fake.date_time()),
                    "updatedAt": str(fake.date_time()),
                    "avgReviews": random.randint(0, 6)}
        print(offreobj)
        db.offresData.insert_one(offreobj)