import random
import pymongo as pymongo
from faker import Faker

fake = Faker()

def generate_rib_per_user(db,rib_per_user):
    userIds = db.usersData.find().distinct('_id')
    types = ["paypal", "payoneer", "google pay", "skrill", "stripe"]
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
        for r in range(rib_per_user):
            ribobj = {"_id":fake.uuid4(),
                      "userId": i,
                      "numero": fake.iban(),
                      "type": random.choice(types),
                      "banque": random.choice(banks),
                      "createdAt": str(fake.date_time()),
                      "updateddAt": str(fake.date_time())}
            print(ribobj)
            db.ribsData.insert_one(ribobj)
#print(userIds)