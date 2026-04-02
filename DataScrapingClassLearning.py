import requests as r
from bs4 import BeautifulSoup as bs
import pandas as pd
#
# response = r.get("https://www.scrapethissite.com/pages/simple/")
# pageSource = response.text
# with open("PageSource.txt","w") as f:
#     f.write(pageSource)

with open("PageSource.txt","r",encoding="utf-8") as f:
    sourceCode = f.read()
    s = bs(sourceCode,"html.parser")
    # s = s.prettify()
    countryData ={"Country Name": [], "Country Capital": [], "Country Population": [], "Country Area": []}
    countryNames = s.find_all("h3",{"class":"country-name"})
    countrycapitals = s.find_all("span", {"class": "country-capital"})
    countrypopulation = s.find_all("span", {"class": "country-population"})
    countryArea = s.find_all("span", {"class": "country-area"})
    for i in range(len(countryNames)):
        countryData["Country Name"].append(countryNames[i].text.strip())
        countryData["Country Capital"].append(countrycapitals[i].text.strip())
        countryData["Country Population"].append(countrypopulation[i].text.strip())
        countryData["Country Area"].append(countryArea[i].text.strip())
