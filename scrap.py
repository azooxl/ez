import requests 
from bs4 import BeautifulSoup

def getAllPages():
    urls = []
    pageNumber = 1


    for i in range(243):
        i = f"https://www.citya.com/annonces/location/appartement{pageNumber}"
        pageNumber += 1
        urls.append(i)


    return(urls)


def parseJ(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    appart = soup.find_all('div', class_="infos")

    for jsp in appart:
        try:
            type = jsp.find('strong').text.strip()
        except AttributeError as e:
            type = ""
        try:
            ville = jsp.find('p', class_="ville").text.strip()
        except AttributeError as e:
            ville = ""
        try:
            prix = jsp.find('p', class_="prix").text.strip()
        except AttributeError as e:
            prix = ""
        
        with open('fichier.csv', "a", encoding="UTF8" )as f:
            f.write(f"Nombre de pièces et surface habitable :  {type}\n")
            f.write(f"Lieu :  {ville}\n")
            f.write(f"Prix :  {prix}\n\n")


def parseAll():
    links = getAllPages()
    for link in links:
        parseJ(url=link)

parseAll()