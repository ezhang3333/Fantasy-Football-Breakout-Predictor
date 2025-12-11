import pandas as pd
from constants import TEAM_NAME_TO_ABBR, cbs_def_vs_rb_stats, cbs_def_vs_wr_stats

TEAM_NICK_TO_ABBR = {
    full_name.split()[-1]: abbr
    for full_name, abbr in TEAM_NAME_TO_ABBR.items()
}

class CBSDefCleaner:
    def __init__(self, def_vs_rb_stats, def_vs_wr_stats, def_vs_te_stats):
        self.def_vs_rb_stats = def_vs_rb_stats.copy()
        self.def_vs_wr_stats = def_vs_wr_stats.copy()
        self.def_vs_te_stats = def_vs_te_stats.copy()
        self.calculated_stats = {
            'cbs_def_vs_rb_stats' : cbs_def_vs_rb_stats,
            'cbs_def_vs_wr_stats' : cbs_def_vs_wr_stats 
        }

    def calculate_cbs_def_vs_rb_stats(self):
        rb_def_df = self.def_vs_rb_stats.copy()

        rb_def_df["def_rush_ypa_allowed"] = rb_def_df["Rush YPA"]
        rb_def_df["def_rb_carries_allowed"] = rb_def_df["Rush Att"]
        rb_def_df["def_rb_receptions_allowed"] = rb_def_df["Recpt"]
        rb_def_df["def_rb_touchdowns_allowed"] = (rb_def_df["Rush TD"] + rb_def_df["Rec TD"])
        rb_def_df["def_rb_fantasy_points_allowed"] = rb_def_df["FPTS"]

        rb_def_df["TeamNickname"] = (
            rb_def_df["Team"]
            .str.replace("RB vs ", "", regex=False)
            .str.strip()
        )
        rb_def_df["team"] = rb_def_df["TeamNickname"].map(TEAM_NICK_TO_ABBR)

        rb_def_df = rb_def_df.dropna(subset=["team"])

        result_df = rb_def_df[[
            "team",
            "def_rush_ypa_allowed",
            "def_rb_carries_allowed",
            "def_rb_receptions_allowed",
            "def_rb_touchdowns_allowed",
            "def_rb_fantasy_points_allowed",
        ]].reset_index(drop=True)

        return result_df

    def calculate_cbs_def_vs_wr_stats(self):
        wr_def_df = self.def_vs_wr_stats.copy()
        
        wr_def_df["def_wr_ftps"] = wr_def_df["FPTS"]
        wr_def_df["def_wr_targets"] = wr_def_df["Targt"]
        wr_def_df["def_wr_yards_per_target"] = wr_def_df["Rec Yds"].astype(float) / wr_def_df["Targt"].astype(float)
        wr_def_df["def_wr_yards_per_target"] = wr_def_df["def_wr_yards_per_target"].fillna(0)

        wr_def_df["TeamNickname"] = (
            wr_def_df["Team"]
            .str.replace("WR vs ", "", regex=False)
            .str.strip()
        )
        wr_def_df["team"] = wr_def_df["TeamNickname"].map(TEAM_NICK_TO_ABBR)

        wr_def_df = wr_def_df.dropna(subset=["team"])

        result_df = wr_def_df[[
            "team",
            "def_wr_ftps",
            "def_wr_targets",
            "def_wr_yards_per_target",
        ]].reset_index(drop=True)

        return result_df

    def calculate_cbs_def_vs_te_stats(self):
        te_def_df = self.def_vs_te_stats.copy()
        
        te_def_df["def_te_ftps"] = te_def_df["FPTS"]
        te_def_df["def_te_targets"] = te_def_df["Targt"]
        te_def_df["def_te_yards_per_target"] = te_def_df["Rec Yds"].astype(float) / te_def_df["Targt"].astype(float)
        te_def_df["def_te_yards_per_target"] = te_def_df["def_wr_yards_per_target"].fillna(0)

        te_def_df["TeamNickname"] = (
            te_def_df["Team"]
            .str.replace("WR vs ", "", regex=False)
            .str.strip()
        )
        te_def_df["team"] = te_def_df["TeamNickname"].map(TEAM_NICK_TO_ABBR)

        te_def_df = te_def_df.dropna(subset=["team"])

        result_df = te_def_df[[
            "team",
            "def_te_ftps",
            "def_te_targets",
            "def_te_yards_per_target",
        ]].reset_index(drop=True)

        return result_df