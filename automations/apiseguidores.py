import requests
from pymongo import MongoClient

client = MongoClient()
db = client['Rengage']

dbcliente = db['clientes']


url = "https://instagram28.p.rapidapi.com/following"

querystring = {"user_id":"52671945536","batch_size":"102"}

headers = {
	"X-RapidAPI-Key": "5221eb422bmsh72785dd1fcea78bp1bf268jsnf3f274245a2d",
	"X-RapidAPI-Host": "instagram28.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

seguidores = response.json()

dbcliente.insert_one({'daaddo': seguidores})

