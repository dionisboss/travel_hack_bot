from pymongo import MongoClient
from .cred import username, password
# username = input()
# password = input()
client_str = f'mongodb+srv://{username}:{password}@travlehack.apnll.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
client = MongoClient(client_str)
# setup db
db_name = 'travelhack'
db = client[db_name]
# setup user collection
col_users_name = 'visitors'
collection_users = db[col_users_name]

# setup admin collection
col_admins_name = "admins"
collection_admins = db[col_admins_name]

# setup exhibit collection
col_exhibit = 'exhibit'
collection_door = db[col_exhibit]

