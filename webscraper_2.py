from bs4 import BeautifulSoup
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


x=f.read()
if x == soup.prettify():
  print("the same")
else:
  print("not the same")



score = soup.find('div',attrs={'class': 'zg_rankInfo'})
print(score)
f.write(soup.prettify())
f.close
