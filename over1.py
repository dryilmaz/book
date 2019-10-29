from bs4 import BeautifulSoup
import urllib
import urllib.error
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

file = open("deneme2.txt","r")
for line in file:
     #Let's split the line into an array called "fields" using the ";" as a separator:
     fields = line.split(";")

     #and let's extract the data:
     songTitle = fields[0]

     #Print the song
     print(songTitle)
     url = songTitle



     try:
         url_oku = urllib.request.urlopen(songTitle)
     except(HTTPError) as e:
         print(e)
     except URLError:
         print("server down")
     else:
         soup = BeautifulSoup(url_oku, 'html.parser')
         try:
             npage = soup.find_all('span',attrs={'itemprop':'numberOfPages'})[0].get_text()
         except(IndexError):
             npage = "sayfa sayisi belirtilmemis"
         print("sayfa sayisi " + npage)








   #It is good practice to close the file at the end to free up resources
file.close()
