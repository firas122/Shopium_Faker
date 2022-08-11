import random
import pymongo as pymongo
from faker import Faker
import faker_commerce
from googletrans import Translator

translator = Translator()
fake = Faker()
fake.add_provider(faker_commerce.Provider)
try:
    client = pymongo.MongoClient("mongodb://firas:islamislam1@cluster0-shard-00-00.mnvbj.mongodb.net:27017,cluster0-shard-00-01.mnvbj.mongodb.net:27017,cluster0-shard-00-02.mnvbj.mongodb.net:27017/?ssl=true&replicaSet=atlas-6o1kj8-shard-0&authSource=admin&retryWrites=true&w=majority")
    db = client.Shopium_Fake_Data
    T = db.ribsData
    print("connection established")
except:
    print("cannot connect")

userIds = db.usersData.find().distinct('_id')
types = ["paypal","payoneer","google pay","skrill","stripe"]
banks = ["Société Tunisienne de Banque « STB »",
"Banque Nationale Agricole « BNA »",
"Banque de l’Habitat « BH »",
"Banque de Financement des Petites et Moyennes entreprises « BFPME »",
"Banque Tunisienne de Solidarité « BTS »",
"Banque de Tunisie et des Emirats « BTE »",
"Banque Tuniso-Libyenne « BTL »",
"Tunisian Saudi Bank « TSB »",
"Banque Zitouna",
"Al Baraka Bank",
"Al Wifak International Bank",
"Amen Bank",
"Attijari Bank",
"Arab Tunisian Bank « ATB »",
"Arab Banking Corporation « ABC »",
"Banque Internationale Arabe de Tunisie «  BIAT »",
"Banque de Tunisie « BT »"]

for i in userIds:
    ribobj = {"_id":fake.uuid4(),
              "userId": i,
              "numero": fake.iban(),
              "type": random.choice(types),
              "banque": random.choice(banks),
              "createdAt": str(fake.date_time()),
              "updateddAt": str(fake.date_time())}
    T.insert_one(ribobj)
#print(userIds)