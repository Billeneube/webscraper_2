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
x=f.read()
if x == soup.prettify():
  print("the same")
else:
  print("not the same")
# while i == False:
#   if x == soup.prettify():
#     i =True
#   else: 
#     print("not the same")







f.write(soup.prettify())
f.close
