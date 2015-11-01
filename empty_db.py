#Empties the information in the database

from pymongo import MongoClient

connection = MongoClient()
db = connection['data']
db.users.drop()
db.posts.drop()
db.comments.drop()