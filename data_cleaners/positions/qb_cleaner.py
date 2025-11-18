from data_cleaners.nfl_rp_cleaner import NFLReadCleaner
import pandas as pd

class QBCleaner:
    def _init__(self, cleaned_data):
        self.cleaned_data = cleaned_data
    
        self.calculated_stats = {
            
        }

# add trendy stats like past 5 weeks usage and target share or like past 3 weeks, decide the number of weeks later        
