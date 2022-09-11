"""
data explorer v0.1
"""

import pandas as pd

def check_winner(goal_diff):
    if(goal_diff>0):
        return "H"
    elif(goal_diff<0):
        return "A"
    else:
        return "D"

class Explorer:
    data_pd = None

    def __init__(self):
        self.data_pd = pd.read_csv("database/example-data.csv", sep="\t")
        self.data_pd['GoalDiff'] = self.data_pd.GoalsH - self.data_pd.GoalsA
        self.data_pd['Winner'] = self.data_pd['GoalDiff'].apply(check_winner)

    def get_unique_teams(self):
        nr_team_a = self.data_pd['TeamA'].nunique()
        nr_team_h = self.data_pd['TeamH'].nunique()
        if not nr_team_a == nr_team_h:
            raise RuntimeError("Number of teams not equal: " + str(nr_team_a)
                               + " " + str(nr_team_h))
        return nr_team_a
    

