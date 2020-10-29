import requests
from bs4 import BeautifulSoup
import pandas as pd

#tv show info function
def tvShow(showName):
    showName = showName.replace(" ", "_")
    page = requests.get(f"https://en.wikipedia.org/wiki/{showName}_(TV_series)")
    soup = BeautifulSoup(page.content, 'html.parser')
    main = soup.find(id="content")
    infos = main.find_all('p')
    definition = infos[1].get_text()
    cast = main.find(class_='div-col columns column-width').get_text()
    show = '\t\t***definition *** \n' + definition + '\n' + '\t\t***Cast ***\n' + cast 
    showName = showName.replace("_", "+")
    ytUrl = f"https://www.youtube.com/results?search_query={showName}+trailer"
    ytTrailer = '\n\n\t\t***trailer***\n' + ytUrl
    watchFree = '\n\n\t\t***Watch For Free***\n' + f'https://www.cimaclub.cam/search/{showName}'
    return show +  ytTrailer + watchFree