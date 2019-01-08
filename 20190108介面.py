import sys
import os
from tkinter import*
from tkinter import messagebox
from random import randint
from tkinter import ttk
from pprint import pprint
from tkinter import scrolledtext

#----------函數程式碼分隔線------------------------------------------------------------------------------------------
satis = dict()

#電影場次
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
	string = ""
	string += "\n"
	string += '['+name+']'
	counter = 0
	for a in range(len(影城movie)):
		timelist = " ".join(str(e) for e in 影城time[a])
		if len(timelist)!= 0:
			string += "\n"
			string += "@"+str(影城movie[a])
			string += "\n"
			string += "    "+"場次: "+timelist
			counter += 1
	if counter == 0:
		string += "\n"+"    "+"本時段無場次"
	string += "\n"		
	return  string

	

#劇情與評價
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
		introduction.strip(' </br>')
	
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
	
	影評文字 = "\n"+"劇情介紹："+"\n"
	影評文字 += introduction +"\n"+"\n"
	影評文字 += "網友短評（僅限參考）：" +"\n"
	影評文字 += "\n"
	for i in range(len(usercomment)):
		影評文字 += '網友%d說: ' %(i+1) +"\n"
		影評文字 += '  ' + usercomment[i]+"\n"
		影評文字 += "\n"
		
	return 影評文字

#滿意度	
def satisfaction():
	滿意度文字 = "滿意度 (滿分為五顆星)"
	滿意度文字 += "\n\n"
	scoreorder = sorted( [ [-satis[key],key] for key in satis ] )  #用前者VALUE排序
	for i in range(len(satis)):
		k = scoreorder[i][1]
		滿意度文字 += str(-scoreorder[i][0])+' stars   '+k+"\n"
	return 滿意度文字
	
#----------介面程式碼分隔線------------------------------------------------------------------------------------------


    


#第二視窗(選遊戲或電影)
def start():
	window.destroy()
	i = useroption.get()
	if i == 0:
	#進入電影分支
			#2.出現爬蟲結果(第三視窗)
		def showmovie():
			window2.quit()
			timeresult = starthour_combel.get().zfill(2)+"時"+starthmin_combel.get().zfill(2)+"分到"+endhour_combel.get().zfill(2)+"時"+endmin_combel.get().zfill(2)+"分間台大周邊電影院放映的電影有："			
			global starttimehour,starttimeminute,endtimehour,endtimeminute
			starttimehour = str(starthour_combel.get().zfill(2))
			starttimeminute = str(starthmin_combel.get().zfill(2))
			endtimehour = str(endhour_combel.get().zfill(2))
			endtimeminute = str(endmin_combel.get().zfill(2))
			
			window3 = Tk()
			window3.title("找電影中")
			label = Label(window3, text = "您的搜尋結果如下", width = 20, bg = "lightgreen")
			label.pack()
			
			out1 = fuction("東南亞秀泰影城",'https://movies.yahoo.com.tw/theater_result.html/id=53')
			out2 = fuction("百老匯數位影城",'https://movies.yahoo.com.tw/theater_result.html/id=52')
			out3 = fuction("梅花數位影院",'https://movies.yahoo.com.tw/theater_result.html/id=126')	
			movieschedule = out1+out2+out3		
			
			#開演時段
			scheduletext = scrolledtext.ScrolledText(window3,width = 50, height = 10, wrap = WORD) #text要用來放爬蟲結果
			scheduletext.pack(side = LEFT) 
			scheduletext.insert(INSERT,"時段："+movieschedule)
			

			#滿意度

			satitext = scrolledtext.ScrolledText(window3,width = 50, height = 10, wrap = WORD) #text要用來放爬蟲結果
			satitext.pack(side = LEFT) 
			satitext.insert(INSERT,"滿意度：")

			
			#繼續搜尋
			search_messagebox = messagebox.askokcancel("還想知道更多", "是否要搜尋電影簡介和評論?")
			#不要就出現對話框
			if search_messagebox == False:
				comfirm_messagebox = messagebox.askokcancel("對話視窗", "是否繼續使用？")
				#還是不要就離開
				if comfirm_messagebox == False:
					messagebox.showinfo("對話方塊","感謝您的支持，我們下次再會!")
					window3.destroy()
					window2.destroy()

				#改要重頭開始
				else:
					window = Tk()
					window.title("不上課要幹嘛")
					window.geometry("300x300")
					window.maxsize(500,500)

					label1 = Label(window,text = "使用者您好，請選擇服務項目", width = 30,height = 5, bg = "lightyellow").pack(side = TOP)
					label2 = Label(window,text = '以時間搜尋電影請按"1",玩小遊戲請按"2"').pack(side = TOP)

					service = {0:"1",1:"2"}
					useroption = IntVar()
					useroption.set(0)
					for i in range(len(service)):
						Radiobutton(window,text = service[i],variable = useroption,value = i).pack()

					Button(window2,text = "確定",command = start).pack()
					window.mainloop()

			else:#要就搜尋
				name = StringVar
				Label(window3,text = "請輸入電影名稱後按確認：", width = 20, bg = "lightblue").pack()
				Entry(window3,width = 25, textvariable = name).pack(side = TOP)
				Button(window3,text = "確認").pack(side = BOTTOM)#按鈕功能待設計
				commenttext = scrolledtext.ScrolledText(window3,width = 50, height = 10, wrap = WORD) #text要用來放爬蟲結果
				commenttext.pack(side = RIGHT) 
				commenttext.insert(INSERT,"影評：")




		#1.下拉選單選時段
		window2 = Tk()
		window2.title("請選擇電影開演時段：")


		hour = []
		for i in range(24):
			hour.append(i)

		minute = []
		for i in range(0,60,5):
			minute.append(i)
		#起始時間
		start_label1 = Label(window2, text = '起始時間:', width=10)
		start_label1.grid(row = 0,column = 0)
		
		starthour_combel = ttk.Combobox(window2, width=10, values = hour)
		starthour_combel.grid(row = 0, column = 1 )
		starthour_combel.current(12)

		start_label2 = Label(window2, text = '時', width = 5)
		start_label2.grid(row = 0,column = 2)


		starthmin_combel = ttk.Combobox(window2, width=10, values = minute)
		starthmin_combel.grid(row = 0, column = 3 )
		starthmin_combel.current(0)

		#結束時間
		end_label1 = Label(window2, text = '結束時間:', width=10)
		end_label1.grid(row = 3,column = 0)
		
		endhour_combel = ttk.Combobox(window2, width=10, values = hour)
		endhour_combel.grid(row = 3, column = 1 )
		endhour_combel.current(12)

		end_label2 = Label(window2, text = '時', width = 5)
		end_label2.grid(row = 3,column = 2)


		endmin_combel = ttk.Combobox(window2, width=10, values = minute)
		endmin_combel.grid(row = 3, column = 3 )
		endmin_combel.current(0)

		end_label3 = Label(window2, text = '分', width = 5)
		end_label3.grid(row = 3,column = 2)

		#確認按鈕則在文字框跑爬蟲結果
		confirmtime = Button(window2,text = "確定",command = showmovie)
		confirmtime.grid(row = 3,column = 4)

		window2.mainloop()






	
		
	else:
	#進入小遊戲分支
		def Callcmdplay1a2b():
			window4.destroy()
			os.system('C:\\Users\\mikem\\Desktop\\Final-Project-Team-10\\PBC-Final-Project-Team-10\\1a2b.py')
		#1.對話框
		ask_messagebox = messagebox.askokcancel("準備好了嗎？", "嗨挑戰者！我們來玩1A2B吧！")
		if ask_messagebox == True:
			play_messagebox = messagebox.askokcancel("準備好了嗎？","注意！你只有10次機會！！")
			if play_messagebox == True:
				#2.小遊戲開始
				window4 = Tk()
				window4.title("玩1A2B")
				window4.geometry("300x250")
				label1 = Label(window4,text = "使用者您好，請在命令提示字元中使用本服務", width = 40,height = 5, bg = "lightyellow")
				label1.pack(side = TOP)
				B=Button(window4,text="知道了",width = 10, height = 5, command= Callcmdplay1a2b, bg = "yellow")
				B.pack()
				window4.mainloop()
			else:
				notplay_messagebox = messagebox.showwarning("沒電影看還想耍任性?","不玩就不玩啊") 
				sys.exit(0)
		else:
			notplay_messagebox = messagebox.showwarning("沒電影看還想耍任性?","不玩就不玩啊") 
			sys.exit(0)
#第一視窗
window = Tk()
window.title("不上課要幹嘛")
window.geometry("300x300")
window.maxsize(500,500)

label1 = Label(window,text = "使用者您好，請選擇服務項目", width = 30,height = 5, bg = "lightyellow").pack(side = TOP)
label2 = Label(window,text = '以時間搜尋電影請按"1",玩小遊戲請按"2"').pack(side = TOP)

service = {0:"1",1:"2"}
useroption = IntVar()
useroption.set(0)
for i in range(len(service)):
	Radiobutton(window,text = service[i],variable = useroption,value = i).pack()

Button(window,text = "確定",command = start).pack()
window.mainloop()
