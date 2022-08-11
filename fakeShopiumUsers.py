import pymongo as pymongo
from faker import Faker
import faker_commerce
from googletrans import Translator
import random
translator = Translator()
fake = Faker(["fr_FR"])
fake.add_provider(faker_commerce.Provider)
try:
    client = pymongo.MongoClient("mongodb://firas:islamislam1@cluster0-shard-00-00.mnvbj.mongodb.net:27017,cluster0-shard-00-01.mnvbj.mongodb.net:27017,cluster0-shard-00-02.mnvbj.mongodb.net:27017/?ssl=true&replicaSet=atlas-6o1kj8-shard-0&authSource=admin&retryWrites=true&w=majority")
    db = client.Shopium_Fake_Data
    T = db.usersData
    print("connection established")
except:
    print("cannot connect")
pays = ["kairouan","sousse","monastir","sfax","tunis","kasserine","tozeur","gafsa","gabes","benzart","tataouine"]

passwords=["bf3036a510f66b83ca809f0107a6863ed63aebd7d10b96fdc14b3d8c90d6485b",
"55f833889da65b1685e50ec988165f10cafb9650d4f7e8328e69d7b88a87afbe",
"41d79bb71b785d365fa055da50e12acba6dd5ee6fab262574df35e66fa55f36a",
"e637d09e2c53f1689a80b6d2e8748c879258aac95d0b48efde62e9d44b2d6733",
"9c9413e2b3c4216801dcfa444fef575d34cb9b15ceec38238c979b416fbcc0bc",
"88d548fc5ceb0aa7f52de21724530ad3beaa8c18c1165cb8cff7acbae1362368",
"be62762170fc4c7424236309c6b55eda012d5c6da13270be54675db6eea29232",
"3c2f485ce61739b2aff4be4419825860d2f61501c88a0aad405145d73937661a",
"6a8af079251aca03be292400d30ed9ab39c1358fa33ce365963d76bc359bd522",
"179b7eebd60e0ea98cab76dd9ee479d37b407c4c0315d518824cf141b1d6a9d2"]
for i in range(1000):
    amis = []
    friendRequest = []
    sendRequest = []
    for y in range(random.randint(1, 4)):
        amis.append({"_id":fake.uuid4(),"nom":fake.name(),"prenom":fake.name()})
    for x in range(random.randint(1, 4)):
        friendRequest.append({"_id":fake.uuid4(),"nom":fake.name(),"prenom":fake.name()})
    for z in range(random.randint(1, 4)):
        sendRequest.append({"_id":fake.uuid4(),"nom":fake.name(),"prenom":fake.name()})
    userobj={"_id":fake.uuid4(),
             "nom":fake.name(),
             "prenom":fake.name(),
             "pays":"tunisie",
             "ville":random.choice(pays),
             "email":fake.email(),
             "password":random.choice(passwords),
             "role":random.choice(["admin","subscriber"]),
             "photo":fake.url(),
             "cloudinary_id":fake.uuid4(),
             "verified":fake.boolean(chance_of_getting_true=75),
             "codeParrainage":random.randint(10000, 99999),
             "amis":amis,
             "friendRequest":friendRequest,
             "sendRequest":sendRequest,
             "createdAt":str(fake.date_time()),
             "updatedAt":str(fake.date_time()),
             "date":str(fake.date()),
             "genre":random.choice(["H","F"])}
    T.insert_one(userobj)
    print(userobj)