import requests
from bs4 import BeautifulSoup
import pandas as pd

# fucntions that find player stat
def findStat(playerName):
    url = "https://r6.tracker.network/profile/pc/" + playerName
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    mainInfos = soup.find(class_='trn-card__content trn-card--light pt8 pb8')
    rank = [mainInfos.find_all(class_='')[4].find('div').get_text()]
    mmr = [mainInfos.find(class_='trn-text--dimmed').get_text()]
    order = [mainInfos.find(class_='trn-text--primary').get_text()]
    Kdholder = soup.find(class_='trn-card__content pt8 pb8')
    kd = [Kdholder.find_all(class_="")[1].get_text()]
    s = [f'Rank : {rank}',
         f'MMR : {mmr}',
         f'Region Order : {order}',
         f'Over all KD : {kd}']
    return s
