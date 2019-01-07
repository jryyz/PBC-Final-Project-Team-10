import sys
import os
from tkinter import*
from tkinter import messagebox
from random import randint
from tkinter import ttk
from pprint import pprint



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
			timeresult = starthour_combel.get()+"時"+starthmin_combel.get()+"分到"+endhour_combel.get()+"時"+endmin_combel.get()+"分間台大周邊電影院放映的電影有："

			window3 = Tk()
			window3.title("找電影中")
			label = Label(window3, text = "您的搜尋結果如下", width = 20, bg = "lightgreen")
			label.pack()
			
			moviebar = Scrollbar(window3)
			movietext = Text(window3,width = 50, height = 10, wrap = WORD) #text要用來放爬蟲結果
			moviebar.pack(side = RIGHT, fill = Y) 
			movietext.pack(side = LEFT, fill = Y)
			moviebar["command"] = movietext.yview
			movietext["yscrollcommand"] = moviebar.set

			movietext.insert(INSERT,timeresult)
			

			
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
				Button(window3,text = "確認").pack(side = BOTTOM)#按鈕功能待設計
				Label(window3,text = "請輸入電影名稱後按確認：", width = 20, bg = "lightgreen").pack(side = BOTTOM)
				Entry(window3,width = 25, textvariable = name).pack(side = BOTTOM)




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
			os.system('C:\\Users\\ventose\\Documents\\PBC-Final-Project-Team-10\\1a2b.py')
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

		elif ask_messagebox == False or play_messagebo == False:
			notplay_messagebox = messagebox.showwarning("沒電影看還想耍任性?","不玩就不玩啊") 

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
