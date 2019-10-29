from bs4 import BeautifulSoup
import urllib
import urllib.error
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

url = "https://www.kitapyurdu.com/kitap/bozkirda-yeseren-sevda-turkuleriaytmatov-ve-eserleri-uzerine/101367.html"
url_oku = urllib.request.urlopen(url)
soup = BeautifulSoup(url_oku, 'html.parser')
name = soup.find('div' ,attrs={'class':'padding'}).find('h1').text
yorum = soup.find('div',attrs={'class':'image-container'}).find('a')
yorum2= soup.find('a',attrs={'class':'colorbox'})
#print(yorum2)
print(yorum['href'])
print(name)
