import requests


def get_rangers_players(football_api_key):
    url = "https://v3.football.api-sports.io/fixtures"

    # the free tier of the API is restricted to the season 2021 onwards
    querystring = {"team": "257", "season": "2021"}
    headers = {
        "x-rapidapi-key": football_api_key,
        "x-rapidapi-host": "v3.football.api-sports.io"
    }

    # response = requests.get(url, headers=headers, params=querystring)
    print(response.json())
    return response.json()
