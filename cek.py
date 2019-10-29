from bs4 import BeautifulSoup
import urllib
from urllib.request import urlopen

url = "https://www.kitapyurdu.com/kitap/turkiye-ortadogu-ve-avrasyayi-neler-bekliyor-/101366.html"
#url'i okuyalum.


url_oku = urllib.request.urlopen(url)

#BeautifulSoup yollyalım.
soup = BeautifulSoup(url_oku, 'html.parser')

# tüm html dökümanı ekrana basalım
#print(soup.find_all('table.tr',limit=1))
#print(soup.find_all('script',attrs={'type':'text/javascript'}).next)
#'table',attrs={'class':'table table-hover table-bordered'}
#rows = soup.find_all()
desc = soup.find_all('span',attrs={'itemprop':'description'})[0].get_text()
pubdate = soup.find_all('td',attrs={'itemprop':'datePublished'})[0].get_text()
npage = soup.find_all('span',attrs={'itemprop':'numberOfPages'})[0].get_text()
price = soup.find_all('div',attrs={'class':'middle'})[0].get_text()
print("yayim tarihi"+" "+pubdate)
print("sayfa sayisi"+" "+npage)
print("price"+" "+price)
print("tanim"+" "+desc)
