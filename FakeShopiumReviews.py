import random
import pymongo as pymongo
from faker import Faker
import faker_commerce
from googletrans import Translator

translator = Translator()
fake = Faker()
fake.add_provider(faker_commerce.Provider)



def generate_reviews(db,users,nbre_reviews_per_offer):
    reviews = []
    # productids = T.find().distinct('_id')
    with open("./reviews.txt") as file:
        while (line := file.readline().rstrip()):
            reviews.append(line)
    print(reviews)

    userIds = db.usersData.find({}, {"_id": 1, "nom": 1})
    offerIds = db.offresData.find().distinct('_id')
    for i in offerIds:
        a = random.randint(0, users-1)
        for x in range(nbre_reviews_per_offer):
            Reviewbject = {"_id": fake.uuid4(),
                           "userId": userIds[a]["_id"],
                           "offerId": i,
                           "text": random.choice(reviews),
                           "image": fake.url(),
                           "createdAt": str(fake.date_time()),
                           "userName": userIds[a]["nom"],
                           "rating": random.randint(1, 5)}
            print(Reviewbject)
            db.reviewsData.insert_one(Reviewbject)
#print(userIds[0]["_id"])