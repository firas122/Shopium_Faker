
import random
import pymongo as pymongo
from faker import Faker
import faker_commerce
from googletrans import Translator

translator = Translator()
fake = Faker(["fr_FR"])
fake.add_provider(faker_commerce.Provider)
try:
    client = pymongo.MongoClient("mongodb://firas:islamislam1@cluster0-shard-00-00.mnvbj.mongodb.net:27017,cluster0-shard-00-01.mnvbj.mongodb.net:27017,cluster0-shard-00-02.mnvbj.mongodb.net:27017/?ssl=true&replicaSet=atlas-6o1kj8-shard-0&authSource=admin&retryWrites=true&w=majority")
    db = client.API_Fake_Tickets
    T = db.ticketsData
    print("connection established")
except:
    print("cannot connect")
for x in range(2):
    products = []
    total = 0
    for y in range(random.randint(1, 9)):
        pquantity = random.randint(1, 9)
        pupri = round(random.uniform(100, 9999), 0)
        ptotal = pquantity * pupri
        trans = translator.translate(fake.ecommerce_name(), dest="fr")
        products.append({"pname": trans.text,"pquantity": pquantity,"pupri":pupri,"ptotal":ptotal})
        total += ptotal
    mainobject = {"name": random.choice(["MONOPRIX", "CARREFOUR", "AZIZA", "CITY MARKET"]),
                  "_id": fake.uuid4(),
                  "total": total,
                  "date": str(fake.date()),
                  "time": str(fake.time()),
                  "extractiondate": str(fake.date_time().strftime("%m/%d/%Y, %H:%M:%S")),
                  "userobj": fake.simple_profile(),
                  "prods":products}

    #print(json_normalize(mainobject["prods"]))
    T.insert_one(mainobject)
    #print(mainobject)