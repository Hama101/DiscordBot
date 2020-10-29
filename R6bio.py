import requests
from bs4 import BeautifulSoup
import pandas as pd

# fucntions that find player stat
def findBio(opName):
    url = "https://rainbowsix.fandom.com/wiki/" + opName
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    realInfos = soup.find('aside')
    divInfos = realInfos.find_all('div')
   
    titles = []
    for title in divInfos:
        s = title.find('h3')
        if  s is not None :
            #print(s.get_text())
            titles.append(s.get_text())
    
    descriptions=[]
    for description in divInfos:
        s = description.find('div')
        if  s is not None :
            #print(s.get_text())
            descriptions.append(s.get_text())
            
    bioGraphyHolder = soup.find(class_="mw-parser-output")
    bioGraphy ='```  **Biography**  ```' +bioGraphyHolder.find_all('p')[3].get_text() + bioGraphyHolder.find_all('p')[4].get_text()
 
    

    bio = pd.DataFrame(
    {
        'titles': titles,
        'descriptions': descriptions,
    })
    
    return     (bio,bioGraphy)

#print(findBio('ash') )      