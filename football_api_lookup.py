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

        try:
            response = requests.get(url, headers=headers, params=querystring)
        except Exception as e:
            print(f"Error fetching fixtures: {e}")
            return None

        return response.json()

    @staticmethod
    def search_fixtures(team_name, fixtures):
        matching_fixtures = []

        print('fixtures')
        print(fixtures)

        team_name = team_name.lower()
        for fixture in fixtures:
            home_team = fixture["teams"]["home"]["name"]
            away_team = fixture["teams"]["away"]["name"]

            if team_name in home_team.lower() or team_name in away_team.lower():
                fixture_date = fixture["fixture"]["date"]
                # fixture_time = fixture["fixture"]["time"]
                fixture_result = fixture["goals"]
                matching_fixtures.append({
                    "home_team": home_team,
                    "away_team": away_team,
                    "fixture_date": fixture_date,
                    "home_score": fixture_result["home"],
                    "away_score": fixture_result["away"],
                })

        print('matching_fixtures')
        print(matching_fixtures)
        return matching_fixtures
