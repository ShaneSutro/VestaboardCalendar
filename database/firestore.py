import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
import os

print(os.path.dirname(os.path.realpath(__file__)))

try:
  os.environ['FLASK_ENVIRON'] == 'production'
except KeyError:
  os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.path.dirname(__file__) + '/cred.json'

firebase_admin.initialize_app()

db = firestore.client()

