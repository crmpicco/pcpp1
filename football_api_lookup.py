import requests


class FootballApi:
    BASE_URL = "https://v3.football.api-sports.io"

    def __init__(self, api_key):
        self.api_key = api_key

    def get_fixtures(self, team_id, season):
        url = f"{self.BASE_URL}/fixtures"
        querystring = {"team": team_id, "season": season}
        headers = {
            "x-rapidapi-key": self.api_key,
            "x-rapidapi-host": "v3.football.api-sports.io"
        }

        response = requests.get(url, headers=headers, params=querystring)
        return response.json()
