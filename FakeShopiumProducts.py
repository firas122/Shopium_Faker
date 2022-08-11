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
    db = client.Shopium_Fake_Data
    T = db.productsData
    print("connection established")
except:
    print("cannot connect")
categoryids = db.categoryData.find().distinct('_id')

for i in range(500):
    trans = translator.translate(fake.ecommerce_name(), dest="fr")
    offers = []
    photos = []
    for y in range(random.randint(1, 3)):
        offers.append(str(fake.uuid4()))
    for x in range(3):
        photos.append(str(fake.url()))
    ProductObject = {"_id": fake.uuid4(),
                     "name": trans.text,
                     "price": round(random.uniform(100, 9999), 0),
                     "photo": photos,
                     "categoryId": random.choice(categoryids),
                     "fabricant": fake.uuid4(),
                     "offer": offers,
                     "logo": fake.url(),
                     "isLiked": fake.boolean(),
                     "isnew": fake.boolean(),
                     "createdAt": str(fake.date_time()),
                     "updateddAt": str(fake.date_time()),
                     "barcode": "619"+fake.ean(length=8)}
    T.insert_one(ProductObject)
    print(ProductObject)

