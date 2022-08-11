import pymongo as pymongo
from faker import Faker

fake = Faker()

def generate_fabricants(db):
    arr =["Percepta",
          "Exela Movers",
          "Ibotta, Inc.",
          "Wanderu (hospitality & tourism)",
          "Aceable, Inc.",
          "Intrepid Travel",
          "Defendify",
          "Twisters Gymnastics Academy",
          "Aims Community College",
          "Kaboom Fireworks",
          "Compass Mortgage",
          "Marathon Physical Therapy",
          "Semicolon Bookstore"]
    for i in arr:
        fabobj= {"_id": fake.uuid4(),
                 "name": i,
                 "password": "",
                 "logo": fake.url(),
                 "phone": fake.phone_number(),
                 "createdAt": str(fake.date_time()),
                 "updateddAt": str(fake.date_time())}
        db.fabricantData.insert_one(fabobj)
        print(fabobj)