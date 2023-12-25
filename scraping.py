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

  header = soup.find('section', id='featured-film-header')
  subheader = header.find('p')
  # title = header.find('h1').text
  # year = subheader.find('small', class_='number').text
  director = subheader.find('span').text

  cast_section = soup.find('div', id='tab-cast').find_all('a', class_='tooltip')
  cast = [actor.text for actor in cast_section]

  details_section = soup.find('div', id='tab-details').find_all('a')
  country = details_section[-2].text
  language = details_section[-1].text

  genres_section = soup.find('div', id='tab-genres').find('div').find_all('a')
  genres = [genre.text for genre in genres_section]

  # return title, year, director, cast, country, language, genres
  return director, cast, country, language, genres
