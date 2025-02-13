import requests


class FootballApi:
    API_HOST = "v3.football.api-sports.io"

    def __init__(self, api_key):
        self.api_key = api_key


    def get_fixtures(self, team_id, season):
        url = f"https://{self.API_HOST}/fixtures"
        querystring = {"team": team_id, "season": season}
        headers = {
            "x-rapidapi-key": self.api_key,
            "x-rapidapi-host": self.API_HOST
        }

        response = requests.get(url, headers=headers, params=querystring)
        return response.json()


    @staticmethod
    def search_fixtures(team_name, fixtures):
        matching_fixtures = []

        team_name = team_name.lower()
        for fixture in fixtures:
            home_team = fixture["teams"]["home"]["name"]
            away_team = fixture["teams"]["away"]["name"]

            if team_name in home_team.lower() or team_name in away_team.lower():
                fixture_date = fixture["fixture"]["date"]
                # fixture_time = fixture["fixture"]["time"]
                fixture_result = fixture["goals"]
                fixture_summary = f"{home_team} vs {away_team} on {fixture_date}. Result: {fixture_result}"
                matching_fixtures.append(fixture_summary)

        return matching_fixtures
