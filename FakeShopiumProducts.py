import random
import pymongo as pymongo
from faker import Faker
import faker_commerce
from googletrans import Translator

translator = Translator()
fake = Faker()
fake.add_provider(faker_commerce.Provider)

def generate_products(db,prods_number):
    fabricantids = db.fabricantData.find().distinct('_id')
    categoryids = db.categoryData.find().distinct('_id')
    for i in range(prods_number):
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
                         "fabricant": random.choice(fabricantids),
                         "logo": fake.url(),
                         "isLiked": fake.boolean(),
                         "isnew": fake.boolean(),
                         "createdAt": str(fake.date_time()),
                         "updateddAt": str(fake.date_time()),
                         "barcode": "619"+fake.ean(length=8)}
        db.productsData.insert_one(ProductObject)
        print(ProductObject)

