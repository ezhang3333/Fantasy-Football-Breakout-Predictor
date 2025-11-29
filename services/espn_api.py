import requests
from constants import ESPN_SCOREBOARD_URL


def _fetch_scoreboard_json():
    response = requests.get(
        ESPN_SCOREBOARD_URL,
        timeout=10,
    )
    response.raise_for_status()
    return response.json()


def get_current_week():
    data = _fetch_scoreboard_json()

    week_info = data.get("week", {})
    current_week = week_info.get("number")

    if current_week is None:
        raise ValueError(f"Could not find current week in response: {week_info}")

    return current_week


def get_current_season():
    data = _fetch_scoreboard_json()

    season_info = data.get("season", {})
    season_year = season_info.get("year")

    if season_year is None:
        raise ValueError(f"Could not find season year in response: {season_info}")

    return season_year
