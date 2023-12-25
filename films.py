# import libraries
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
  df = df.head(5) # for small-batch testing

  return df

# fill dataframe with film info
def getFilmInfo(df):
  for index, row in df.iterrows():
    director, cast, country, language, genres = bs.getFilmInfo(row['Letterboxd URI'])
    # df.loc[df['Slug'] == slug, ['Director', 'Cast', 'Country', 'Language', 'Genres']] = [title, year, director, cast, country, language, genres]
    df.loc[index, ['Director', 'Country', 'Language']] = [director, country, language]
  
  return df

df = getWatchedFilms()
df = getFilmInfo(df)
print(df)

# stats functions
def numFilms(df):
  films = len(df)

def numDirectors(df):
  directors = df['Director'].nunique()

def numCountries(df):
  countries = df['Country'].nunique()

def numLanguages(df):
  languages = df['Language'].nunique()
