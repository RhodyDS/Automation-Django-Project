import requests
import json 
from pymongo import MongoClient

client = MongoClient()
db = client['Rengage']

dbcliente = db['clientes']

url = "https://instagram28.p.rapidapi.com/user_info"

querystring = {"user_name":"rhodyds"}

headers = {
	"X-RapidAPI-Key": "5221eb422bmsh72785dd1fcea78bp1bf268jsnf3f274245a2d",
	"X-RapidAPI-Host": "instagram28.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

dados = response.json()


dbcliente.insert_one({'dados': dados})

