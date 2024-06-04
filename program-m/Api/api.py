from flask import Blueprint
import requests
import json

blueprint_api = Blueprint('blueprint_api', __name__,
    template_folder= 'templates',
    static_folder= 'static')

url = "https://imdb-top-100-movies.p.rapidapi.com/"
headers = {
	"X-RapidAPI-Key": "1f93b26d2bmsh150922e83cf0129p11c46djsn1f78557faf20",
	"X-RapidAPI-Host": "imdb-top-100-movies.p.rapidapi.com"
}
#nacte vsechny filmy do metody jako retezec
def GetFilmy():   
    response = requests.get(url, headers=headers)
    
    return json.loads(response.text)

#nacte jeden film podle id do metody jako retezec
def GetDetailFilm(id):   
    response = requests.get(url + str(id), headers=headers)
    
    return json.loads(response.text)
