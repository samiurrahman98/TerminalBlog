import pymongo

__author__ = 'samiurrahman98'

class Database(object): # Database class inherits properties of object
    URI = "mongodb://127.0.0.1:27017" # whole database class contains these first two variables
    DATABASE = None

    # init methods not required, static methods are used in this case and can access the first two variable using Database.'variablename'

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI) # get a client with the database URI, and get the database being used
        Database.DATABASE = client['fullstack']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)