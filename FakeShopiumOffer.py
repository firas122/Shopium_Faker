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
    T = db.offresData
    print("connection established")
except:
    print("cannot connect")

productids = db.productsData.find().distinct('_id')
for i in range(50):
    offreobj = {"_id":fake.uuid4(),"startDate":str(fake.date_time()),"expirationDate":str(fake.date_time()),"condition":"conditions set by fabricant","description":"description of the offer","quantity":random.randint(1, 20),"percentage":random.randint(0, 75),"product":random.choice(productids),"isLiked":fake.boolean(chance_of_getting_true=75),"createdAt":str(fake.date_time()),"updatedAt":str(fake.date_time())}
    T.insert_one(offreobj)