from bs4 import BeautifulSoup
import urllib.request
from htmlpage import url
urlToScrape = input('URL to open. Press Enter to Default')
if urlToScrape == "":
  urlToScrape = 'https://www.amazon.com/Best-Sellers/zgbs'
f = open('htmlpage.py', mode='w+')
fp = urllib.request.urlopen(str(urlToScrape))

mybytes = fp.read()
i = False
mystr = mybytes.decode("utf8")
fp.close()

html_doc=mystr
soup = BeautifulSoup(html_doc, 'html.parser')
readLink = str(url)

link = soup.find('a', attrs={'class' : 'a-link-normal'})
endlink = link['href']
fulllink = 'amazon.com'+endlink
# print(link['href'])
print(fulllink)
print(readLink)
if fulllink != readLink.lstrip():
  print('they are not the same')
else:
  print("they are the same")

f.write("url = '" + fulllink + "'")
f.close
fp = urllib.request.urlopen('https://'+str(fulllink))
mybytes = fp.read()
i = False
mystr = mybytes.decode("utf8")
fp.close()

html_doc=mystr
soup2 = BeautifulSoup(html_doc, 'html.parser')
title = soup2.find('span', attrs={'id' : 'productTitle'}).text
title = str(title)
# print(title.lstrip().rstrip())