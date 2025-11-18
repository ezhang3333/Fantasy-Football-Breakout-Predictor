from data_cleaners.nfl_rp_cleaner import NFLReadCleaner
import pandas as pd

class QBCleaner:
    def _init__(self, cleaned_data):
        self.cleaned_data = cleaned_data
    
        self.calculated_stats = {
            
        }

# add trendy stats like past 5 weeks usage and target share or like past 3 weeks, decide the number of weeks later        
"""
 THESE ARE INDENTIFIERS: 'team', 'position', 'full_name', 'gsis_id', 'week'
NEED TO ENCODE THESE: 'home_team', 'away_team'
'height', 'weight', 'years_exp', 'draft_number', 'total', 'spread_line', 'roof', 'surface', 'temp', 'wind',
'avg_time_to_throw', 'avg_intended_air_yards', 'aggressiveness', 'avg_air_yards_to_sticks',
'completion_percentage_above_expectation', 'max_air_distance', 'pass_attempt', 'pass_air_yards', 'pass_yards_gained
'pass_touchdown', 'rush_touchdown', 'pass_interception', 'pass_touchdown_diff', ''
"""