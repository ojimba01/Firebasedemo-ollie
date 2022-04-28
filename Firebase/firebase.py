# Phlask Firebase Database re-model
#------------------------------------------------------------------------------
# Imports
#-------------------------------------------------------------------------------
import pyrebase

# Config/Setup
#-------------------------------------------------------------------------------
firebaseConfig = {
  "apiKey": "AIzaSyBwTdRWEOBNvMfMbvHOoi9TQeUjoX5AHuc",
  "authDomain": "phlask-pyrebase.firebaseapp.com",
  "databaseURL": "https://phlask-pyrebase-default-rtdb.firebaseio.com",
  "projectId": "phlask-pyrebase",
  "storageBucket": "phlask-pyrebase.appspot.com",
  "messagingSenderId": "987505470254",
  "appId": "1:987505470254:web:bc1a7c1dd74bba39fb68bf",
  "measurementId": "G-80XFK3L26M"
}
firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

#-------------------------------------------------------------------------------
# Heiarachy
data = {
    'phlask-web-map':{
        'phlask-web-map-test': {
            'phlask-web-map-test-water': {
                'phlask-web-map-test-water-live': True,
                'phlask-web-map-test-water-verify': False,
            },
            'phlask-web-map-test-food': {
                'phlask-web-map-test-food-live': True,
                'phlask-web-map-test-food-verify': False,
            },
            'phlask-web-map-test-foraging': {
                'phlask-web-map-test-foraging-live': True,
                'phlask-web-map-test-foraging-verify': False,
            },
            'phlask-web-map-test-bathrooms': {
                'phlask-web-map-test-bathrooms-live': True,
                'phlask-web-map-test-bathrooms-verify': False,
            },
        },
    },
}
#-------------------------------------------------------------------------------
# Misc. Below
#'phlask-web-map-beta': 
#'phlask-web-map-prod':



#-------------------------------------------------------------------------------
# Create Data


#db.child("Phlask").set(data)

#-------------------------------------------------------------------------------
# Read Data

#dataread = db.child("Hotel").child("Users").get()
#print(dataread.val())
#-------------------------------------------------------------------------------
# Update Data

#db.child("Phlask").child("phlask-web-map").update({"phlask-web-map-beta": {"phlask-web-map-beta-water": {"phlask-web-map-beta-water-live": True, "phlask-web-map-beta-water-verify": True}}})
#db.child("Phlask").child("phlask-web-map").update({"phlask-web-map-prod": {"phlask-web-map-prod-water": {"phlask-web-map-prod-water-live": True, "phlask-web-map-prod-water-verify": True}}})
# db.child("Phlask").child("phlask-web-map").child("phlask-web-map-prod").update({'phlask-web-map-prod-food': {
#     'phlask-web-map-prod-food-live': True,
#     'phlask-web-map-prod-food-verify': False,
# },
#     'phlask-web-map-prod-foraging': {
#     'phlask-web-map-prod-foraging-live': True,
#     'phlask-web-map-prod-foraging-verify': False,
# },
#     'phlask-web-map-prod-bathrooms': {
#     'phlask-web-map-prod-bathrooms-live': True,
#     'phlask-web-map-prod-bathrooms-verify': False,
# }
# })
#db.child("Hotel").child("Users").child("1").update({"email": "evandoe@gmail.com"})
#-------------------------------------------------------------------------------
# Remove Data

#Delete 1 Value (from all parent nodes)
#db.child("Hotel").child("Users").child("age").remove()

# Delete whole Node
#db.child("Hotel").child("Users").remove()

#-------------------------------------------------------------------------------