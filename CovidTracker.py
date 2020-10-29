import requests
from bs4 import BeautifulSoup
import pandas as pd

# function that trackes covid-19 by contrey
def covidStat(contry):
    print("Hello to Discord Bot Covid-19 tracker !")
    page = requests.get(
        f"https://www.worldometers.info/coronavirus/country/{contry}/")
    soup = BeautifulSoup(page.content, 'html.parser')
    main = soup.find(class_="content-inner")
    infos = main.find_all(id="maincounter-wrap")
    discreptions = [info.find('h1') for info in infos]
    values = [info.find('span') for info in infos]
    final = pd.DataFrame({
        'Descreptions': discreptions,
        'Value': values,
    })
    return final
