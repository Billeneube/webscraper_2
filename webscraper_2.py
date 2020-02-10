from bs4 import BeautifulSoup
<<<<<<< HEAD
import urllib.request
f = open('htmlpage.txt', mode='w+')
fp = urllib.request.urlopen("https://www.amazon.com/Best-Sellers/zgbs")
mybytes = fp.read()
i = False
mystr = mybytes.decode("utf8")
fp.close()

html_doc=mystr
soup = BeautifulSoup(html_doc, 'html.parser')
content=soup.prettify()
f.write(content)





score = soup.find('div',attrs={'class': 'zg_rankInfo'})
link = soup.find('a', attrs={'class' : 'a-link-normal'})
endlink = link['href']
fulllink = 'amazon.com'+endlink
print(link['href'])
print(fulllink)

f.write(soup.prettify())
f.close
=======
>>>>>>> 4a414c06a1e681a666f598510e2f0b14022b5bb1
