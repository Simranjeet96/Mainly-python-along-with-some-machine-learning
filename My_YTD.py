import requests
from bs4 import BeautifulSoup
print("enter the url of playlist...")
url="https://www.youtube.com/playlist?list=PLmXKhU9FNesSFvj6gASuWmQd23Ul5omtD"
# url=input()
response=requests.get(url).text
soup=BeautifulSoup(response,'lxml')
# for i in soup.find_all('a',class_="pl-video-title-link"):
#         print(i["href"])
#         print()


# class="pl-video-title-link yt-uix-tile-link yt-uix-sessionlink  spf-link "        
print(soup.prettify())