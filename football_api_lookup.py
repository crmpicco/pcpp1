import requests
from typing import List, Dict, Any


class FootballApi:
    API_HOST: str = "v3.football.api-sports.io"

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    def get_fixtures(self, team_id: int, season: int) -> dict:
        url = f"https://{self.API_HOST}/fixtures"
        querystring = {"team": team_id, "season": season}
        headers = {
            "x-rapidapi-key": self.api_key,
            "x-rapidapi-host": self.API_HOST
        }

        try:
            response = requests.get(url, headers=headers, params=querystring)
        except Exception as e:
            print(f"Error fetching fixtures: {e}")
            return {}

        return response.json()

    @staticmethod
    def search_fixtures(team_name: str, fixtures: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        matching_fixtures = []

        team_name = team_name.lower()
        for fixture in fixtures:
            home_team = fixture["teams"]["home"]["name"]
            away_team = fixture["teams"]["away"]["name"]

            if team_name in home_team.lower() or team_name in away_team.lower():
                fixture_date = fixture["fixture"]["date"]
                fixture_result = fixture["goals"]
                matching_fixtures.append({
                    "home_team": home_team,
                    "away_team": away_team,
                    "fixture_date": fixture_date,
                    "home_score": fixture_result["home"],
                    "away_score": fixture_result["away"],
                    "home_logo": fixture["teams"]["home"]["logo"],
                    "away_logo": fixture["teams"]["away"]["logo"]
                })

        return matching_fixtures
