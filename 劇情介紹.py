import requests
import webbrowser

keyword = input()
movie_keyword = {'keyword': keyword}
r = requests.get('https://movies.yahoo.com.tw/moviesearch_result.html' , params= movie_keyword)#先找搜尋頁面
print(r.url)
from bs4 import BeautifulSoup
Soup = BeautifulSoup(r.text,'html.parser')
movie_page = 'div.release_foto a' #查出搜尋頁面
article4 = Soup.select(movie_page)

page = str()
for art in article4:
  art = str(art)
  num3 = art.find('href="')
  num4 = art.find('">')
  page = art[num3+6:num4]

print(page)

p = requests.get(page)
Soup2 = BeautifulSoup(p.text, 'html.parser')
movie_introduction = 'div.gray_infobox_inner'
article5 = Soup2.select(movie_introduction)

introduction = str()
for art in article5:
  art = str(art)
  num = art.find('<span>')
  num2 = art.find('</span')
  introduction = art[num+6:num2]
  introduction.strip('</br>')
  
print(introduction)



