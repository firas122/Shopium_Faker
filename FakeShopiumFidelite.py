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
    T = db.fideliteData
    print("connection established")
except:
    print("cannot connect")
userIds = db.usersData.find().distinct('_id')
for i in range(100):
    fidobj = {"_id":fake.uuid4(),
              "userId":random.choice(userIds),
              "data":"619"+fake.ean(length=8),
              "format":"EAN13"}
    T.insert_one(fidobj)