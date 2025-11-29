import pandas as pd
import requests
from constants import ESPN_SCOREBOARD_URL
from services.espn_api import get_current_season, get_current_week

class QBFinalizedDataset:
    def __init__(self, qb_cleaned_dataset):
        self.qb_cleaned_dataset = qb_cleaned_dataset
        self.current_week = get_current_week()
        

