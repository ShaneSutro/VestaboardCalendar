import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
import os

print(os.path.dirname(os.path.realpath(__file__)))

# cred = credentials.Certificate(os.path.dirname(os.path.realpath(__file__)) + '/cred.json')

firebase_admin.initialize_app()

db = firestore.client()

