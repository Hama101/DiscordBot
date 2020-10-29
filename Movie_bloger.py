import requests
from bs4 import BeautifulSoup
import pandas as pd

#function for movie Blog
def movieInfos(movieName):
    movieName = movieName.replace(" ", "_")
    page = requests.get(f"https://en.wikipedia.org/wiki/{movieName}_(film)")
    soup = BeautifulSoup(page.content, 'html.parser')
    main = soup.find(id="mw-content-text")
    infos = main.find_all('p')
    definition = infos[1].get_text()
    cast = main.find('ul').get_text()
    movie = '\t\t***definition***\n' + definition + '\n' + '\t\t***Cast***\n' + cast
    movieName = movieName.replace("_", "+")
    ytUrl = f"https://www.youtube.com/results?search_query={movieName}+trailer"
    ytTrailer = '\n\n\t\t***trailer***\n' + ytUrl
    watchFree = '\n\n\t\t***Watch For Free***\n' + f'https://www.cimaclub.cam/search/{movieName}'
    return movie + ytTrailer + watchFree