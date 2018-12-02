import csv
import json
import couchdb

couch = couchdb.Server ('http://Admin:admin@localhost:5984')

db= couch['cantantes']

filcsvFile = "songdata.csv" 
json_file = "output_file_name.json"

#Read CSV File 
with open(json_file, "w") as json_file:
   with open (filcsvFile) as cvsfil:
      csvReader = csv.DictReader (cvsfil)
      for rowcsv in csvReader:
          data = {}
          date = rowcsv ["artist"] # columna principal o id del csv
          data['cantantes'] = rowcsv
          db.save(data)

          print (data)
      


