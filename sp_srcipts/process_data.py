# -*- coding: utf-8 -*-
import pandas as pd
from datetime import datetime

if __name__=="__main__":
    df = pd.read_csv("E:\\projects\\recys\\dataset\\0_999_user_info.csv")
    del df["Unnamed: 0"]
    df['time'] = pd.to_datetime(df['time'])
    user_days = df[df['user_id']==98047837][df['time'] >= datetime(2014,11,2)]\
    [df['time'] < datetime(2014,11,3)]
    user_count = user_days['user_id'].count()
    