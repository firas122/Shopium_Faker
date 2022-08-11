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
    T = db.reviewsData
    print("connection established")
except:
    print("cannot connect")

reviews = []
#productids = T.find().distinct('_id')
with open("./reviews.txt") as file:
    while (line := file.readline().rstrip()):
        reviews.append(line)
print(reviews)

userIds = db.usersData.find({}, {"_id": 1, "nom": 1})
offerIds = db.offresData.find().distinct('_id')

for i in range(1000):
    a = random.randint(0, 800)
    Reviewbject = {"_id": fake.uuid4(),
                   "userId": userIds[a]["_id"],
                   "offerId": random.choice(offerIds),
                   "text": random.choice(reviews),
                   "image": fake.url(),
                   "createdAt": str(fake.date_time()),
                   "userName": userIds[a]["nom"],
                   "rating": random.randint(1, 5)}
    print(Reviewbject)
    T.insert_one(Reviewbject)
#print(userIds[0]["_id"])