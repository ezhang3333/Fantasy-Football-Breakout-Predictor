import pandas as pd
import requests
from constants import ESPN_SCOREBOARD_URL, qb_calculated_stats
from services.espn_api import get_current_season, get_current_week

class QBFinalizedDataset:
    def __init__(self, qb_cleaned_dataset):
        self.qb_cleaned_dataset = qb_cleaned_dataset
        self.current_week = get_current_week()

    def extract_finalized_dataset(self):
        cleaned = self.qb_cleaned_dataset
        curr_week = self.current_week
        
        if self.current_week == 1:
            return cleaned[qb_calculated_stats]
        else:
            qb_cleaned_correct_weeks = cleaned[cleaned["week"].between(1, curr_week - 1)]
            return qb_cleaned_correct_weeks[qb_calculated_stats]
