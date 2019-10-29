from bs4 import BeautifulSoup
import urllib
from urllib.request import urlopen
#Accessing a text file - www.101computing.net/mp3-playlist/

file = open("links.txt","r")

#Repeat for each song in the text file
for line in file:



  #Let's split the line into an array called "fields" using the ";" as a separator:
  fields = line.split(";")

  #and let's extract the data:
  songTitle = fields[0]

  #Print the song
  print(songTitle)

  url = songTitle
  url_oku = urllib.request.urlopen(songTitle)
  soup = BeautifulSoup(url_oku, 'html.parser')
  desc = soup.find_all('span',attrs={'itemprop':'description'})[0].get_text()
  pubdate = soup.find_all('td',attrs={'itemprop':'datePublished'})[0].get_text()
  npage = soup.find_all('span',attrs={'itemprop':'numberOfPages'})[0].get_text()
  price = soup.find_all('div',attrs={'class':'middle'})[0].get_text()
  name = soup.find('div' ,attrs={'class':'padding'}).find('h1').text
  print("yayim tarihi"+" "+pubdate)
  print("sayfa sayisi"+" "+npage)
  print("price"+" "+price)
  print("tanim"+" "+desc)
  print("isim"+name)


#It is good practice to close the file at the end to free up resources
file.close()
