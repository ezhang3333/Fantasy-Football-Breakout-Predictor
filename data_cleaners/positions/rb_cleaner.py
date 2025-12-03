from data_cleaners.nfl_rp_cleaner import NFLReadCleaner
import pandas as pd
import numpy as np
from constants import TEAM_NAME_TO_ABBR, rb_calculated_stats

class RBCleaner:
    def __init__(self, cleaned_data, rb_def_stats):
        self.cleaned_data = cleaned_data[cleaned_data["position"] == "RB"].copy()
        self.rb_def_stats = rb_def_stats.copy()
        self.calculated_stats = rb_calculated_stats

    def add_calculated_stats(self):
        df = self.cleaned_data.copy()
        
        # volume
        df["touches"] = df["rec_attempt"] + df["rush_attempt"]
        df["snap_share"] = df["offense_pct"]
        df["rush_share"] = df["rush_attempt"] / df["rush_attempt_team"]
        # do you want to keep this weighting
        df["weighted_opp_share"] = df["rush_attempt"] + 3 * df["rec_attempt"]
        
        # trends all require sorting by name and gsis id
        # "touches_3wk_avg"
        # "touches_trend_3v7"
        # "snap_share_3wk_avg"
        # "snap_share_trend_3v7"
        # "fp_ppr_3wk_avg"
        # "fp_ppr_trend_3v7"

        # rushing efficiency
        df["rush_ypc"] = df["rush_yards_gained"] / df["rush_attempt"]
        df["rush_td_rate"] = df[""]

        # ADD SOME SORT OF TOUCHDOWN FEATURE TRACKING IN RB_CALCULATED_STATS in constants.py