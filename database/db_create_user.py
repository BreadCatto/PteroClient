import pymongo
import bcrypt
import json

with open("config.json") as jsonfile:
    conf = json.load(jsonfile)

client = pymongo.MongoClient(conf["app"]["mongodb_url"])
db = client.get_database('pteroclient')
records = db.users
resources = db.resources

def create(email, password, username, pteroid):
    records_json = {
        "username": username,
        "email": email,
        "password": password,
        "pterodactyl_id": pteroid,
        "package": "default"
    }
    resources_json = {
        "cpu": 0,
        "ram": 0,
        "disk": 0,
        "servers": 0,
        "backups": 0,
        "databases": 0,
        "ports": 0
    }

    user_inserted = records.insert_one(records_json)
    resources_inserted = resources.insert_one(resources_json)