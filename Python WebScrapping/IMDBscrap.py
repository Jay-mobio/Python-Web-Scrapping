import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlalchemy

url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"

response = requests.get(url)

soupe = BeautifulSoup(response.content, "html.parser")

names = []
IMDBRating = []
position = []
release_year = []

movies_dict = {
    "Title": names,
    "Rating": IMDBRating,
    "Rank": position,
    "Year": release_year
}

movies = soupe.find('tbody',{'class':'lister-list'}).find_all('tr')

for movie in movies:
    name = movie.find('td',class_ = 'titleColumn').a.text
    names.append(name)
    rating = movie.find('td', class_ = 'ratingColumn imdbRating').strong.string
    IMDBRating.append(rating)
    rank = movie.find('td',class_ = 'titleColumn').get_text(strip=True).split('.')[0]
    position.append(rank)
    year = movie.find('td',class_ = 'titleColumn').span.text.strip('()')
    release_year.append(year)

movies_df = pd.DataFrame(movies_dict)
engine = sqlalchemy.create_engine("postgresql://postgres:1713@localhost/webscrapping")
movies_df.to_sql(name = "movies",if_exists='replace', con=engine)
print(movies_df)