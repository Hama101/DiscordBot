import requests
from bs4 import BeautifulSoup
import pandas as pd


def gameFinder(gameName):
    gameName = gameName.replace(' ', '_')
    page = requests.get(f"https://en.wikipedia.org/wiki/{gameName}")
    soup = BeautifulSoup(page.content, 'html.parser')
    main = soup.find(id='bodyContent')
    infos = main.find_all('p')
    definition = infos[1].get_text() + infos[2].get_text()
    game = '\t\t***Definition***\n' + definition + '\n'
    gameName = gameName.replace("_", "+")
    ytTrailler = '\n\n\t\t***Trailer && Gameplay ***\n' + f"https://www.youtube.com/results?search_query={gameName}+trailer"
    downlodForFree = '\n\n\t\t***Download For Free***\n' + f'https://fitgirlrepacks.co/search/{gameName}'
    return game + ytTrailler + downlodForFree


