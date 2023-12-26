# import libraries
import pandas as pd

# import modules
import films

# stats functions
def numFilms(df):
  return len(df.drop_duplicates(subset=['Name', 'Year']))

def numDirectors(df):
  return df.explode('Director')['Director'].nunique()

def numCountries(df):
  return df['Country'].nunique()

def numLanguages(df):
  return df['Language'].nunique()

def numDiaryEntries(df):
  return len(df[df['Watched Date'].notna()])

def filmsByYear(df):
  return df.groupby(['Year'])

def filmsByDecade(df):
  group = df['Year'] // 10 * 10
  return df.groupby(group)

def myAverageRating(df):
  return df['Rating'].mean()

# output
df = films.getFilms()
print(df.columns)
print(df[['Name', 'Year', 'Rating']])

# print(numFilms(df))
# print(numDirectors(df))
# print(numCountries(df))
# print(numLanguages(df))
# print(numDiaryEntries(df))

# print(df['Year'].value_counts())
# grouped_df = filmsByYear(df)
# for group_name, group_data in grouped_df:
#     print(f"Group: {group_name}")
#     print(group_data)
#     print("\n")

grouped_df = filmsByDecade(df)
for group_name, group_data in grouped_df:
    print(f"Group: {group_name}")
    print(group_data[['Name', 'Year', 'Rating']])
    print(myAverageRating(group_data))
    print("\n")
