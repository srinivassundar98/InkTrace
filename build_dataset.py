import pandas as pd
import sqlite3
import json
json_file_path="news-category-dataset\\News_Category_Dataset_v3.json"
data = []
with open(json_file_path, 'r') as file:
    for line in file:
        json_object = json.loads(line)
        data.append(json_object)

df_newscat = pd.DataFrame(data)
df_newscat_cleaned=df_newscat[["date","authors","headline","short_description"]]

df_all=pd.read_csv('all-the-news-2-1.csv')
df_ny_times=pd.read_csv('nytimes_front_page.csv')

con=sqlite3.connect('all-the-news.db')
df_allnews1=pd.read_sql('SELECT * FROM LONGFORM',con=con)

df_all_cleaned=df_all[["date","title","author","article"]]
df_all_cleaned.dropna(inplace=True)
def add_midnight(time_str):
    if len(time_str) == 10:  # Just the date part (YYYY-MM-DD)
        return time_str + ' 00:00:00'
    else:
        return time_str

# Apply the function to the 'datetime' column
df_all_cleaned['date'] = df_all_cleaned['date'].apply(add_midnight)

# Convert the 'datetime' column to datetime format
df_all_cleaned['date'] = pd.to_datetime(df_all_cleaned['date'])

df_all_cleaned['date'] = df_all_cleaned['date'].dt.strftime('%Y-%m-%d')

df_ny_times=pd.read_csv('nytimes_front_page.csv')

df_ny_times_cleaned=df_ny_times[["date","author","title","content"]]
df_ny_times_cleaned.dropna(inplace=True)

df_allnews1_cleaned=df_allnews1[["date","author","title","content"]]
df_allnews1_cleaned.dropna(inplace=True)

df_all_cleaned.rename(columns={
    'date': 'DATE',
    'author': 'AUTHOR',
    'title':'TITLE',
    'article':'ARTICLE'
    }, inplace=True)

df_allnews1_cleaned.rename(columns={
    'date': 'DATE',
    'author': 'AUTHOR',
    'title':'TITLE',
    'article':'ARTICLE'
    }, inplace=True)

df_newscat_cleaned.rename(columns={
    'date': 'DATE',
    'authors': 'AUTHOR',
    'headline':'TITLE',
    'short_description':'ARTICLE'
    }, inplace=True)

df_ny_times_cleaned.rename(columns={
    'date': 'DATE',
    'author': 'AUTHOR',
    'title':'TITLE',
    'content':'ARTICLE'
    }, inplace=True)


dataframes = [
    df_all_cleaned,
    df_allnews1_cleaned,
    df_newscat_cleaned,
    df_ny_times_cleaned
]



# Concatenate all DataFrames
df_combined = pd.concat(dataframes, ignore_index=True)
df_combined = df_combined.drop_duplicates()
author_counts = df_combined['AUTHOR'].value_counts()
top_authors = author_counts.head(10)
top_authors_df = df_combined[df_combined['AUTHOR'].isin(top_authors.index)]

downsampled_df = top_authors_df.groupby('AUTHOR').head(5017)


downsampled_df.to_csv('cleaned_and_filtered.csv')