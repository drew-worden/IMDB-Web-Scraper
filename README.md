# IMDB WEB SCRAPER

- ## DESCRIPTION
  This python script utilizes the python packages "requests" and "BeautifulSoup" to extract elements from an IMDB web page and cleans them for further analysis. It starts with the "requests" package that gets passed a URL which accesses the page. The package "BeautifulSoup" is then used to extract certain HTML elements via classes or other CSS descriptors. After the relevant tags and their contents have been extracted for loops and conditional statements are used, along with some list manipulations, to clean the data into the format that would be useful for further analysis. Once the data has been grabbed and cleaned the "pandas" package is ustilized to package the data into a pandas DataFrame, which is the standard for data science related applications. Once this is done the DataFrame can then be exported into a csv.

- ## HOW TO USE
  Clone using Git or download the repository to a folder on your local computer. Inside you will find two files, scraper.py and README.md. The scraper.py file is the python script that does the scraping and the README.md file contains the contents that you are currently reading. Run the scraper.py file however you like, I prefer using Git Bash.

  Once you run the file you will be greeted by a text-based UI that will have three options.

  MAKE A QUERY - 1  
  VIEW DATAFRAME - 2  
  FINISH AND EXPORT DATAFRAME - 3  
  
  - MAKE A QUERY  
    Selecting this option by typing "1" and hitting enter will provide you with a option to input a IMDB link for a movie or TV show link. Once you have found a page that you would like to scrape, copy the URL, paste it into the program, and hit enter. The program will show what was scraped and add it to a DataFrame.
 
 - VIEW DATAFRAME  
   Selecting this option by typing "2" and hitting enter will print the current DATAFRAME, with all previous queries visible. This is here so that the user can keep track of what they have added.
   
 - FINISH AND EXPORT DATAFRAME  
   Selecting this option by typing "3" and hitting enter will close the program and export your DataFrame with all of its queries to a CSV file located in the same directory the scraper.py file is stored.
   
- ## NOTES  
  If you want to create another DataFrame using the scraper script, make sure you remove the previously exported CSV file from the directory, otherwise you will be confronted with an error.
  
  This project is not perfect and there are a few bugs and errors that still need ironing out. The purpose of this project is to showcase by ability to use different data science techniques in Python to obtain clean and workable data.
  
- ## CONTACT    
  If you have any questions or suggestions on how this project could be improved feel free to contact me at drew.p.worden@gmail.com.
  
