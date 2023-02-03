import requests 
from bs4 import BeautifulSoup
import re

class Crawler:
    def __init__(self,maxPages,urls=[]):
        self.maxPages = maxPages
        self.urlsToVisit = urls
        self.visitedUrls = []
    
    def validUrl(self,url):
        r = requests.get(url)
        if r.status_code == 200:
            soup = BeautifulSoup(r.content, "html.parser")
            return soup
        else : 
            print(f"Erreur{r.status_code}.")
            return None

    def domainName(self,url):
        domain = re.search(r"w?[a-v|x-z][\w%\+-\.](org|fr|com|net)", url)
        domainSite = domain.group()
        return domainSite


    def getInternalUrls(self,url):
        html = self.validUrl(url)
        #print(html)
        domainSite = self.domainName(url)

        for links in html.find_all('a'):
            if 'href'  in links.attrs:
                if domainSite in links.attrs['href']:
                    if 'page' in links.attrs['href']:
                        if 'fr' in links.attrs['href']:
                            if 'villages' in links.attrs['href']:
                                print(links.attrs['href'])
                            elif 'sejour' in links.attrs['href']:
                                print(links.attrs['href'])
                            elif 'vacances' in links.attrs['href']:
                                print(links.attrs['href'])
                            elif 'clubs' in links.attrs['href']:
                                print(links.attrs['href'])
                            elif 'residence' in links.attrs['href']:
                                print(links.attrs['href'])
                            elif 'location' in links.attrs['href']:
                                print(links.attrs['href'])
                            elif 'hebregements' in links.attrs['href']:
                                print(links.attrs['href'])
                            elif 'location' in links.attrs['href']:
                                print(links.attrs['href'])
                            elif 'week' in links.attrs['href']:
                                print(links.attrs['href'])

Crawler(maxPages=2).getInternalUrls("https://www.azureva-vacances.com/fr/page/destination-vacances-azureva")