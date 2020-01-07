#IMPORTS
import requests
import pandas as pd
from bs4 import BeautifulSoup

#EMPTY DATAFRAME
queried_media = pd.DataFrame(columns = ["Title", "Year of Release", "IMDB Rating", "Number of Ratings", "Parental Rating", "Runtime", "Genre", "Full Release Date", "Country of Release", "Director", "MetaCritic Score", "Budget"])

#STRIP AND CLEANING FUNCTION
def strip():
    URL = input("Enter the URL of the IMDB page that you want to scrape: ")
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    #TITLE
    title = soup.find("h1", "").get_text()
    title = title.split("\xa0")
    title = title[0]
    print(title)

    #YEAR OF RELEASE
    year_release = soup.find("h1", "").get_text()
    year_release = year_release.split("\xa0")
    year_release = year_release[1]
    year_release = year_release.replace("(", "").replace(")", "")
    print(year_release)

strip()
