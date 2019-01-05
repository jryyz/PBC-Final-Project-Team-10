satis = dict()

def fuction(name,url,starttimehour,starttimeminute,endtimehour,endtimeminute):
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
	starttime=starttimehour+':'+starttimeminute
	endtime=endtimehour+':'+endtimeminute
	
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

	


def function2(keyword):
	import requests
	import webbrowser

	
	movie_keyword = {'keyword': keyword}
	r = requests.get('https://movies.yahoo.com.tw/moviesearch_result.html' , params= movie_keyword)#先找搜尋頁面
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
	return

conti = True
while conti:
	
	print('查詢時間請按"1",查詢電影劇情介紹請按"2"')	#服務開始介面
	opening = input('請選擇服務項目:')
	if opening == '1':
		starthour=input('起始小時:')
		startminute=input('起始分鐘:')
	
		endhour=input('結束小時:')
		endminute=input('結束分鐘:')
	
		fuction("東南亞秀泰影城",'https://movies.yahoo.com.tw/theater_result.html/id=53',starthour,startminute,endhour,endminute)
		fuction("百老匯數位影城",'https://movies.yahoo.com.tw/theater_result.html/id=52',starthour,startminute,endhour,endminute)
		fuction("梅花數位影院",'https://movies.yahoo.com.tw/theater_result.html/id=126',starthour,startminute,endhour,endminute)	

		print("滿意度 (滿分為五顆星)")
		print()
		scoreorder = sorted( [ [-satis[key],key] for key in satis ] )  #用前者VALUE排序
		for i in range(len(satis)):
			k = scoreorder[i][1]
			if str(-scoreorder[i][0]) == '0.0':
				print('尚無評價    '+k)
			else:
				print(str(-scoreorder[i][0])+' stars   '+k)
		conti = False
	elif opening == '2':
		name = input('請輸入電影名稱:')
		function2(name)
		conti = False
	elif opening != '1' or opening != '2':
	 
		 print('輸入錯誤，請重試')
		 conti = True
	print()
	
	while conti == False:
		contd = input('是否繼續使用？(Y/N):')
		if contd == 'N' or contd == 'n':
			break
		elif contd == 'Y' or contd == 'y':
			
			conti = True
			break
		else:
			print('輸入錯誤，請重新輸入：')
			
			conti = False
			continue 
	