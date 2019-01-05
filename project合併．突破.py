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
	movie_usercomment = 'form#form_good1.form_good span'
	article6 = Soup2.select(movie_usercomment)


	introduction = str()#劇情介紹
	for art in article5:
		art = str(art)
		num = art.find('<span>')
		num2 = art.find('</span')
		introduction = art[num+6:num2]
		introduction.strip('</br>')
	
	usercomment = list()#影評
	filter = 1
	

	for art in article6:
		art = str(art)
		num = art.find('<span>')
		num2 = art.find('</span')
		onecomment = art[num+6:num2]
		if filter % 3 == 0:
			usercomment.append(onecomment)
		filter += 1

	print()
	print("劇情介紹：" , end = "")
	print(introduction)
	print("網友短評（僅限參考）：")
	
	for i in range(len(usercomment)):
		print('網友%d說: ' %(i+1))
		print('  ' + usercomment[i])
		
	return

conti = True
use2 = True
while conti:
	print('使用者您好，請選擇服務項目')	#服務開始介面
	print('以時間搜尋電影請按"1"，玩小遊戲請按"2"')
	choice = input('服務項目:')
	if choice == '1':
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

		greeting = input('是否要搜尋電影簡介和評論?(Y/N)')
		if greeting == 'N' or greeting == 'n':
			use2 = False
			conti = False
		elif greeting == 'Y' or greeting == 'y':	
			
			name = input('請輸入電影名稱:')
			function2(name)
			conti = False
		
		while conti == False:
			contd = input('是否繼續使用？(Y/N):')
			if contd == 'N' or contd == 'n':
				print('感謝您的支持，我們下次再會!')
				break
			elif contd == 'Y' or contd == 'y':
				
				conti = True
				break
			else:
				print('輸入錯誤，請重新輸入：')
				
				conti = False
				continue
	if choice == '2':
		import random
		game = True

		while game:
			a = input("嗨挑戰者！我們來玩1A2B吧!(Y/N)")
			if a == "Y" or a == "y" :
				playornot = True
				break
			elif a == "N" or a == "n" :
				playornot = False
				print("沒電影看還想耍任性?")
				print("不玩就不玩啊")
				conti = False
				game = False
			else:
				print("請重新輸入好ㄇ!")

		  
		times = 0  #計算第一次結束後不要玩的次數

		while playornot:
			print('注意！你只有10次機會！！')
			items = [1,2,3,4,5,6,7,8,9,0]
			random.shuffle(items)
			items = "".join('%s' %id for id in items)
			answer = items[0:4]
		  
			time = 0

			while time < 10:
				challenger = input("已嘗試次數：%d 請輸入數字 : " %time)
				time += 1
				A = 0
				B = 0
			
				if len(challenger)!= 4 or not challenger.isnumeric() or len({str(chr) for chr in challenger}) != 4 :
					time -=1
					print("不符合輸入格式，請重新輸入")
			
				else: 
					for i in range(4):
						if challenger.find(answer[i], i, i+1) != (-1) :
							A += 1
						if challenger.find(answer[i]) != (-1):
							B += 1

					B -= A
					print(str(A) + 'A' + str(B) + 'B')
					if A == 4:
						print("恭喜你猜中了！")
						break      

			if A != 4:
				print('ㄏㄏ你輸了ㄛ')

			playagain = str()
			while True:
				playagain = input("要再玩一次嗎？ Y/N")
				if playagain == 'Y' or playagain == 'y':
					break
				elif  playagain == 'N' or playagain == 'n':
					print("真的不玩了嗎?很好玩ㄟ")
					times += 1
					if times == 2:
						print("好啦不玩就不玩")
						print("沒電影看還不玩")
						playornot = False
						game = False
						conti = False
						break
				else:
					print("請再輸入一次！")
		while conti == False:
			contd = input('是否繼續使用？(Y/N):')
			if contd == 'N' or contd == 'n':
				print('感謝您的支持，我們下次再會!')
				break
			elif contd == 'Y' or contd == 'y':
				
				conti = True
				break
			else:
				print('輸入錯誤，請重新輸入：')
				
				conti = False
				continue