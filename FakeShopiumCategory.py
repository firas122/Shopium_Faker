from faker import Faker
fake = Faker()

def generate_categories(db):
    categoryname = ["Apparel", "Footwear", "Bags", "Accessories", "Jewelry", "Eyewear", "Cosmetics", "Beauty",
                    "Electronics", "Sports", "Health"]
    for i in range(len(categoryname)):
        catobj = {"_id":fake.uuid4(),
                  "name":categoryname[i],
                  "createdAt":str(fake.date_time()),
                  "updatedAt":str(fake.date_time())}
        print(catobj)
        db.categoryData.insert_one(catobj)