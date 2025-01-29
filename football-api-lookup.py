import requests

url = "https://api-football-v1.p.rapidapi.com/v3/players"

querystring = {"team":"33","season":"2020"}

headers = {
	"x-rapidapi-key": "",
	"x-rapidapi-host": "api-football-v1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
