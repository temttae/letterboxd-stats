# import libraries
from bs4 import BeautifulSoup
import requests
import lxml

def makeSoup(url):
  page = requests.get(url)
  soup = BeautifulSoup(page.text, 'lxml')
  return soup

# scrape film information
def getFilmInfo(url):
  soup = makeSoup(url)

  crew_section = soup.find('div', id='tab-crew')
  director_section = crew_section.find('div').find_all('a')
  director = [director.text for director in director_section]

  cast_section = soup.find('div', id='tab-cast').find_all('a', class_='tooltip')
  cast = [actor.text for actor in cast_section]

  details_section = soup.find('div', id='tab-details').find_all('a')
  country = details_section[-2].text # FIX THIS (cannot use this index)
  language = details_section[-1].text # FIX THIS (there are multiple languages)

  genre_section = soup.find('div', id='tab-genres').find('div').find_all('a')
  genre = [genre.text for genre in genre_section]

  return director, cast, country, language, genre
  # return director, cast, country, language, genre, rating
