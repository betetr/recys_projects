
# coding: utf-8

# In[ ]:


# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from datetime import datetime

if __name__=="__main__":
    # df = pd.read_csv("E:\\recys_projects\\dataset\\0_999_user_info.csv")
    df = pd.read_csv("/home/xuyayuan/recys_projects/dataset/0_999_user_info.csv")
    del df["Unnamed: 0"]
    df['time'] = pd.to_datetime(df['time'])
    user_days = df[df['user_id']==98047837][df['time'] >= datetime(2014,11,2)][df['time'] < datetime(2014,11,3)]
    user_count = user_days['user_id'].count()

    def get_user_counts(df,day):
        if day < 13:
            new_df = df[df['time'] >= datetime(2014,11,day+17)][df['time'] < datetime(2014,11,day+18)].groupby('user_id').count()
            return new_df
        if day == 13:
            new_df = df[df['time'] >= datetime(2014,11,day+17)][df['time'] < datetime(2014,12,1)].groupby('user_id').count()
            return new_df
        new_df = df[df['time'] >= datetime(2014,12,day-13)][df['time'] < datetime(2014,12,day-12)].groupby('user_id').count()
        return new_df

    new_df = get_user_counts(df,10)
    print(new_df.head())

    new_df.index[:6]

    p=new_df.ix[[134658],'item_id']
    print(np.array(p).tolist()[0])
    p = np.array(p).tolist()
    print(p)

