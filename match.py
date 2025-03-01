import requests
import sqlite3

player_id = '1119281509'

class MatchInfo():
    def __init__(self, match_id, hero_id, radiant_win, duration):
        self.match_id = match_id
        self.hero_id = hero_id
        self.radiant_win = radiant_win
        self.duration = duration

    def __str__(self):
        return self.to_message()
    
    def to_message(self) -> str:
        return (f"Match ID: {self.match_id}\n"
                f"Hero ID: {self.hero_id}\n"
                f"Radiant Win: {'Yes' if self.radiant_win else 'No'}\n"
                f"Duration: {self.duration} seconds\n")

# Function to get recent matches using the OpenDota API for a given player
def get_recent_matches(player_id) -> list[MatchInfo] | None:
    url = f'https://api.opendota.com/api/players/{player_id}/recentMatches'
    response = requests.get(url)
    
    if response.status_code == 200:
        return [MatchInfo(match['match_id'], match['hero_id'], match['radiant_win'], match['duration']) for match in response.json()]
    else:
        return None

# Function to fetch the first recent match
def get_last_match(player_id):
    matches = get_recent_matches(player_id)
    if matches and len(matches) > 0:
        match = matches[0]  # Get the first match
        return match
    else:
        return None

match = get_last_match(player_id)
