satis = dict()

starttimehour=input()
starttimeminute=input()
starttime=starttimehour+':'+starttimeminute
endtimehour=input()
endtimeminute=input()
endtime=endtimehour+':'+endtimeminute

def fuction(name,url):
	import requests
	requests.get(url)
	res = requests.get(url)
	res.text

	from bs4 import BeautifulSoup
	Soup = BeautifulSoup(res.text,'html.parser')

	tag_name = 'div.theaterlist_name a'
	movie_time = 'ul.theater_time  '
	star = 'div.leveltext.starwithnum span.count'
	articles = Soup.select(tag_name)
	article2 = Soup.select(movie_time)
	article3 = Soup.select(star)

#電影名稱	
	影城movie = []

	for art in articles:
		art = str(art)
		num1 = art.find('>')
		art = art[num1+1:-4]
		影城movie.append(art)
		
#電影場次
	影城timecode = []
	影城time = []
	find_time1=0

	for art in article2:
		art = str(art)
		num2 = art.find('">')
		art = art[num2+2:-5]	
		影城timecode.append(art)
	
	for i in 影城timecode:
		n=0
		ava_time=[]
		for j in i:
			n+=1
			if j == 't':
				find_time1=i.find('t">',n-1)
				selecttime = i[find_time1+3:find_time1+8]
				if selecttime>=starttime and selecttime<=endtime:
					ava_time.append(selecttime)
		影城time.append(ava_time)
    
                
#滿意度
	
	score=[]
	for art in article3:
		art = str(art)
		num3 = art.find('">')
		num4 = art.find('</')
		art = art[num3+2:num4]
		art= float(art)
		score.append(art)
	for i in range (len(影城movie)):
		satis[影城movie[i]]=score[i]
		
#輸出格式
	print('['+name+']')
	counter = 0
	for a in range(len(影城movie)):
		timelist = " ".join(str(e) for e in 影城time[a])
		if len(timelist)!= 0:
			print()
			print("@"+str(影城movie[a]))
			print("    "+"場次: "+timelist)
			counter += 1
	if counter == 0:
		print("    "+"本時段無場次")
			
	print()
fuction("東南亞秀泰影城",'https://movies.yahoo.com.tw/theater_result.html/id=53')
fuction("百老匯數位影城",'https://movies.yahoo.com.tw/theater_result.html/id=52')
fuction("梅花數位影院",'https://movies.yahoo.com.tw/theater_result.html/id=126')	

print("滿意度 (滿分為五顆星)")
print()
scoreorder = sorted( [ [-satis[key],key] for key in satis ] )  #用前者VALUE排序
for i in range(len(satis)):
	k = scoreorder[i][1]
	print(str(-scoreorder[i][0])+' stars   '+k)
