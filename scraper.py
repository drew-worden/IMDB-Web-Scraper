#IMPORTS
import requests
import pandas as pd
from bs4 import BeautifulSoup

#EMPTY DATAFRAME
queried_media = pd.DataFrame(columns = ["Title", "Year of Release", "IMDB Rating", "Number of Ratings", "Parental Rating", "Runtime", "Genre", "Full Release Date", "Country of Release", "Director", "MetaCritic Score", "Budget"])

#STRIP AND CLEANING FUNCTION
def strip():
    URL = input("IMDB LINK: ")
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    #TITLE
    title = soup.find("h1", "").get_text()
    title = title.split("\xa0")
    title = str(title[0])
    print(title)

    #YEAR OF RELEASE
    year_release = soup.find("h1", "").get_text()
    year_release = year_release.split("\xa0")
    year_release = year_release[1]
    year_release = str(year_release.replace("(", "").replace(")", ""))
    print(year_release)

    #IMDB RATING
    imdb_rating = float(soup.find(itemprop = "ratingValue").get_text())
    print(imdb_rating)
    #NUMBER OF RATINGS
    num_ratings = soup.find(itemprop = "ratingCount").get_text()
    num_ratings = int(num_ratings.replace(",", ""))
    print(num_ratings)

    #PARENTAL RATING
    dirty_parent_rating = soup.find("div", "subtext").get_text()
    dirty_parent_rating = dirty_parent_rating.split(" ")
    parent_rating_list = []

    for element in dirty_parent_rating:
        if element == "" or element == "\n":
            del element
        else:
            parent_rating_list.append(element)

    parent_rating = str(parent_rating_list[0].replace("\n", ""))
    print(parent_rating)

    #RUNTIME
    runtime = soup.find("time").get_text()
    runtime = runtime.split(" ")
    runtime_list = []
    for element in runtime:
        element = element.replace("\n", "")
        if element == "" or element == "\n":
            del element
        else:
            runtime_list.append(element)

    if len(runtime_list) == 2:
        runtime = str(runtime_list[0] + " " + runtime_list[1])
    else:
        runtime = str(runtime_list[0])
    print(runtime)

    #GENRE
    genre = soup.find("div", "subtext").get_text()
    genre = genre.split(" ")

    clean_genre = []
    for element in genre:
        element = element.replace("\n", "").replace("|", ""). replace(",", "")
        if element == '' or element == '' or element == '\n' or element == "|":
            del element
        else:
            clean_genre.append(element)
    genre = clean_genre

    list = []
    imdb_genres = ["Drama", "Adventure", "Comedy", "Romance", "Mystery", "Family", "Musical", "Animation", "Horror", "Action", "Thriller", "Crime", "Biography", "Sci-Fi", "History", "War", "Fantasy", "Western"]
    for element in genre:
        for item in imdb_genres:
            if item in element:
                list.append(item)

    genre = list
    print(genre)

    

strip()
