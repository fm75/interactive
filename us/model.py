import pandas as pd
import datetime as dt
from typing import List

df = None

def county_file_name(state: str) ->str:
    return '/'.join(['data', 'counties', state.lower().replace(' ', '-')]) + '.csv'


def update_stats(state:str, date: dt.date) -> pd.DataFrame:
    global df
    df = pd.read_csv(county_file_name(state))
    return df.describe()[['pop2019']].style.format({"pop2019": "{:,.0f}",})

def update_counties(state: str, date: dt.date, column: str, ascending: bool) -> pd.DataFrame:
    global df
    df = pd.read_csv(county_file_name(state))
    return df.sort_values(by=column, 
        ascending=ascending)[['county', 'pop2019']].style.format({"pop2019": "{:,.0f}",})

def states() -> List[str]:
    return list(pd.read_csv('data/us-states-only.csv').state)
