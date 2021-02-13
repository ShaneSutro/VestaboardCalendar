import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
import os

print(os.path.dirname(os.path.realpath(__file__)))

# cred = credentials.Certificate(os.path.dirname(os.path.realpath(__file__)) + '/cred.json')
cred = credentials.Certificate(os.environ['GOOGLE_APPLICATION_CREDENTIALS'])
firebase_admin.initialize_app(cred)

db = firestore.client()

