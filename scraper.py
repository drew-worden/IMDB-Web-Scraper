#IMPORTS
import requests
import pandas as pd
from bs4 import BeautifulSoup

#EMPTY DATAFRAME
queried_media = pd.DataFrame(columns = ["Title", "Year of Release", "IMDB Rating", "Number of Ratings", "Parental Rating", "Runtime", "Genre", "Full Release Date", "Country of Release", "Director", "MetaCritic Score", "Budget"])

#STRIP AND CLEANING FUNCTION
def strip():
    URL = "https://www.imdb.com/title/tt0111161/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=e31d89dd-322d-4646-8962-327b42fe94b1&pf_rd_r=2C21P8DMC00ETTVXAW8K&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_1"
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

    parent_rating = parent_rating_list[0].replace("\n", "")
    print(parent_rating)

strip()
