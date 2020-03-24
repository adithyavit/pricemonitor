import requests
from bs4 import BeautifulSoup

url = 'http://www.imdb.com/search/title?release_date=2017&sort=num_votes,desc&page=1'
response = requests.get(url)
html_soup = BeautifulSoup(response.text, 'html.parser')

movie_containers = html_soup.find_all('div', class_ = 'lister-item mode-advanced')

first_movie = movie_containers[0]

#print(first_movie)
print(first_movie.h3.a.text)

#print(first_movie.h3.span.text)

first_year = first_movie.h3.find('span', class_ = 'lister-item-year text-muted unbold')

print(first_year.text[1:-1])

first_imdb = float(first_movie.strong.text)

print(first_imdb)

first_mscore = first_movie.find('span', class_ = 'metascore favorable')
first_mscore = int(first_mscore.text)
print(first_mscore)

first_votes = first_movie.find('span', attrs = {'name':'nv'})
print(first_votes.text)

print(first_votes['data-value'])


Scraping IMDB data using BeautifulSoup
 - Scraped data of around 2000 movies from IMDb using beautiful soup.
 - extracted name, IMDB rating, number of votes, meta scores, year of release for each movie.
 - stored the data of all the movies in a data frame using pandas and generated reports of the data.
 - periodically updated the data by comparing it with previously generated reports.
 - projected the distributions of IMDB ratings and meta scores of movies using matplotlib. 