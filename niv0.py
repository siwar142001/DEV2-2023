import json




dictionnaire={
  "parking": {
    "total_places": 50,
    "available_places": 50,
    "occupied_places": 0,
    "regular_places": [
      {"id": 1, "status": "available", "car_license_plate": None,"entry_time":None},
      {"id": 2, "status": "available", "car_license_plate": None,"entry_time":None},
      {"id": 3, "status": "available", "car_license_plate": None,"entry_time":None},
      {"id": 4, "status": "available", "car_license_plate": None,"entry_time":None},
      {"id": 5, "status": "available", "car_license_plate": None,"entry_time":None},
      {"id": 6, "status": "available", "car_license_plate": None,"entry_time":None},
      {"id": 7, "status": "available", "car_license_plate": None,"entry_time":None},
      {"id": 8, "status": "available", "car_license_plate": None,"entry_time":None},
      {"id": 9, "status": "available", "car_license_plate": None,"entry_time":None},
      {"id": 10, "status": "available", "car_license_plate": None,"entry_time":None},
       {"id": 11, "status": "available", "car_license_plate": None,"entry_time":None},
       {"id": 12, "status": "available", "car_license_plate": None,"entry_time":None},
         {"id": 13, "status": "available", "car_license_plate": None,"entry_time":None},
      {"id": 14, "status": "available", "car_license_plate": None,"entry_time":None},
      {"id": 15, "status": "available", "car_license_plate": None,"entry_time":None},
      {"id": 16, "status": "available", "car_license_plate": None,"entry_time":None},
      {"id": 17, "status": "available", "car_license_plate": None,"entry_time":None},
      {"id": 18, "status": "available", "car_license_plate": None,"entry_time":None},
      {"id": 19, "status": "available", "car_license_plate": None,"entry_time":None},
      {"id": 20, "status": "available", "car_license_plate": None,"entry_time":None},
      {"id": 21, "status": "available", "car_license_plate": None,"entry_time":None},
      {"id": 22, "status": "available", "car_license_plate": None,"entry_time":None},
       {"id": 23, "status": "available", "car_license_plate": None,"entry_time":None},
       {"id": 24, "status": "available", "car_license_plate": None,"entry_time":None},
         {"id": 25, "status": "available", "car_license_plate": None,"entry_time":None},
      {"id": 26, "status": "available", "car_license_plate": None,"entry_time":None},
      {"id": 27, "status": "available", "car_license_plate": None,"entry_time":None},
      {"id": 28, "status": "available", "car_license_plate": None,"entry_time":None},
      {"id": 29, "status": "available", "car_license_plate": None,"entry_time":None},
      {"id": 30, "status": "available", "car_license_plate": None,"entry_time":None},
      {"id": 31, "status": "available", "car_license_plate": None,"entry_time":None},
      {"id": 32, "status": "available", "car_license_plate": None,"entry_time":None},
      {"id": 33, "status": "available", "car_license_plate": None,"entry_time":None},
      {"id": 34, "status": "available", "car_license_plate": None,"entry_time":None},
       {"id": 35, "status": "available", "car_license_plate": None,"entry_time":None},
       {"id": 36, "status": "available", "car_license_plate": None,"entry_time":None},
         {"id": 37, "status": "available", "car_license_plate": None,"entry_time":None},
      {"id": 38, "status": "available", "car_license_plate": None,"entry_time":None},
      {"id": 39, "status": "available", "car_license_plate": None,"entry_time":None},
      {"id": 40, "status": "available", "car_license_plate": None,"entry_time":None},
      {"id": 41, "status": "available", "car_license_plate": None,"entry_time":None},
      {"id": 42, "status": "available", "car_license_plate": None,"entry_time":None},
      {"id": 43, "status": "available", "car_license_plate": None,"entry_time":None},
      {"id": 44, "status": "available", "car_license_plate": None,"entry_time":None},
      {"id": 45, "status": "available", "car_license_plate": None,"entry_time":None},
      {"id": 46, "status": "available", "car_license_plate": None,"entry_time":None}
    ],
    "handicap_places": [
      {"id": 47, "status": "available", "car_license_plate": None},
      {"id": 48, "status": "available", "car_license_plate": None},
      {"id": 49, "status": "available", "car_license_plate": None},
      {"id": 50, "status": "available", "car_license_plate": None}
    ]
  }
}
nom_fichier = "projet-PM/Niveau1.json"

with open(nom_fichier, 'w') as fichier:
    json.dump(dictionnaire, fichier, indent=2) 
