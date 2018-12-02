
import xlrd #libreria para leer archivos excel
import simplejson as json
import couchdb

couch = couchdb.Server ('http://Admin:admin@localhost:5984')

db= couch['inmuebles']

libro = xlrd.open_workbook('sold.xlsx')#abrimos el libro de excel
hoja = libro.sheet_by_index(0)#estabecemos la hoja del libro en este caso 0

for i in range(0, hoja.nrows):#numero de filas
        data = {}
        fila = hoja.row_values(i)#iteracciones de filas
        data['sold'] = {
        'latitude':fila[0],
        'longitude':fila[1],
        'streetAddress':fila[2],
        'suburb':fila[3],
        'postcode':fila[4],
        'region':fila[5],
        'bedrooms':fila[6],
        'bathrooms':fila[7],
        'parkingSpaces':fila[8],
        'propertyType':fila[9],
        'price':fila[10],
        'listingId':fila[11],
        'title':fila[12],
        'dateSold':fila[13],
        'modifiedDate':fila[14]
        }
        #Lo almacenamos en couchdb 
        db.save(data)
        
  




    

    




