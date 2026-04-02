import requests as r
from bs4 import BeautifulSoup as bs
#
# response = r.get("https://www.scrapethissite.com/pages/simple/")
# pageSource = response.text
# with open("PageSource.txt","w") as f:
#     f.write(pageSource)

with open("PageSource.txt","r") as f:
    sourceCode = f.read()
    s = bs(sourceCode,"html.parser")
    # s = s.prettify()
    countryNames = s.find_all("h3",{"class":"country-name"})
    for eachCountry in countryNames:
        print(eachCountry.text.strip())