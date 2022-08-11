import pymongo
import time
from FakeShopiumribs import generate_rib_per_user
from FakeShopiumProducts import generate_products
from FakeShopiumOffer import generate_offers
from FakeShopiumCategory import generate_categories
from FakeShopiumFabricant import generate_fabricants
from FakeShopiumFidelite import generate_fidelite
from FakeShopiumReviews import generate_reviews
from fakeShopiumUsers import generate_users

try:
    client = pymongo.MongoClient("mongodb://firas:islamislam1@cluster0-shard-00-00.mnvbj.mongodb.net:27017,cluster0-shard-00-01.mnvbj.mongodb.net:27017,cluster0-shard-00-02.mnvbj.mongodb.net:27017/?ssl=true&replicaSet=atlas-6o1kj8-shard-0&authSource=admin&retryWrites=true&w=majority")
    db = client.Test
    print("connection established Now sit back and watch ")
except:
    print("cannot connect")

def main(users,products,offers,reviews_per_offer,rib_per_user):
    print("generating users")
    generate_users(db,users)
    print("generating fabricants")
    time.sleep(2)
    generate_fabricants(db)
    print("generating categories")
    time.sleep(2)
    generate_categories(db)
    print("generating products")
    time.sleep(2)
    generate_products(db,products)
    print("generating offers")
    time.sleep(2)
    generate_offers(db,offers)
    print("generating reviews")
    time.sleep(2)
    generate_reviews(db,users,reviews_per_offer)
    print("generating ribs")
    time.sleep(2)
    generate_rib_per_user(db,rib_per_user)
    print("Database created Thanks for waiting")

main(100,50,10,5,2)