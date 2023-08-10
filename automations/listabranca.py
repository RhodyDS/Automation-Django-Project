from pymongo import MongoClient
import pickle
import datetime

data = datetime.date.today()

client =  MongoClient()
db = client['Rengage']
dbfollowers = db['packfollowers']
dbcliente = db['clientes']
dbwork_diario = db['workday']


diccarq = open('dados/listbranca.pkl', 'rb')  # abrir dados de clientes
unff = pickle.load(diccarq)
diccarq.close()


for i in unff.keys():
    if dbcliente.find_one({'user':i}):
        dbcliente.update_one({'user':i}, {'$set':{'lista_branca': unff[i]}})
