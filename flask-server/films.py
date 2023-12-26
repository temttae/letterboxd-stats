# import libraries
import numpy as np
import pandas as pd

# import modules
import scraping as bs

# create watched films dataframe
def getWatchedFilms():
  diary_df = pd.read_csv('data/diary.csv')
  watched_df = pd.read_csv('data/watched.csv')
  ratings_df = pd.read_csv('data/ratings.csv')

  df = pd.merge(watched_df, ratings_df, on='Letterboxd URI', how='left', suffixes=('', '_y'))
  df.drop(['Date_y', 'Name_y', 'Year_y'], axis=1, inplace=True)

  df = pd.merge(df, diary_df, on=['Name', 'Year', 'Date'], how='outer', suffixes=('', '_z'))
  df.drop(['Letterboxd URI_z', 'Rating_z'], axis=1, inplace=True)

  df = df.head(50) # for small-batch testing
  return df

# df = getWatchedFilms()
# print(df[['Name', 'Year', 'Rating', 'Letterboxd URI']])

# fill dataframe with film info
def getFilmInfo(df):
  df['Director'] = None
  df['Cast'] = None
  df['Genre'] = None

  for index, row in df.iterrows():
    try:
      director, cast, country, language, genre = bs.getFilmInfo(row['Letterboxd URI'])
      # director, cast, country, language, genre, rating = bs.getFilmInfo(row['Letterboxd URI'])
      df.at[index, 'Director'] = tuple(director)
      df.at[index, 'Cast'] = tuple(cast)
      df.at[index, 'Country'] = country
      df.at[index, 'Language'] = language
      df.at[index, 'Genre'] = tuple(genre)
      # df.at[index, 'Average Rating'] = rating
    except Exception as err:
      print(err, row)
  
  return df

# return complete dataframe
def getFilms():
  df = getWatchedFilms()
  return getFilmInfo(df)

# df = getFilms()
# print(df)