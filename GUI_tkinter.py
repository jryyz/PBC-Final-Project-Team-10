from tkinter import*
from tkinter import messagebox
window = Tk()
window.title("不上課要幹嘛")
window.geometry("500x500")
window.maxsize(700,700)

label1 = Label(window,text = "要看電影還是玩遊戲?", width = 30,height = 10, bg = "lightyellow")

def checkdaytime():
	def showmsg():#做爬蟲結果視窗
		window3 = Tk()
		window3.title("我想看電影")
		i = option.get()
		label3 = Label(window3,text = "時間是"+ time[i])#失效待查
		sbar = Scrollbar(window3)
		text = Text(window3,width = 50, height = 10, wrap = WORD) #text要用來放爬蟲結果
		#做卷軸
		sbar.pack(side = RIGHT, fill = Y) 
		text.pack(side = LEFT, fill = Y)
		sbar["command"] = text.yview
		text["yscrollcommand"] = sbar.set

	#要加時間文字方塊
	window2 = Tk()
	window2.title("選電影時段")
	label2 = Label(window2,text = "請選時間:").pack()
	time = {0:"8:00~9:00",1:"9:00~10:00"}
	option = IntVar()
	option.set(0)
	for i in range(len(time)):
		Radiobutton(window2,text = time[i],variable = option,value = i).pack()
	Button(window2,text = "確定",command = showmsg).pack()

def play1a2b():
	# def compare:#引入程式


	ask_messagebox = messagebox.askokcancel("準備好了嗎？", "嗨挑戰者！我們來玩1A2B吧！")
	if ask_messagebox == True:
		play_messagebox = messagebox.askokcancel("準備好了嗎？","注意！你只有10次機會！！")
		if play_messagebox == True:
			window4 = Tk()
			window4.title("玩1A2B").geometry("300x300")
			num_label = Label(window4,width = 20,text = "我猜是：(請輸入四個數字)").pack(side = top)#輸入
			guess_entry = Entry(window4,width = 10, textvariable = num1).pack(side = LEFT)
			submit_button = Button(width4,width = 10,text = "確定",command = compare).pack(side = LEFT)#交答案
			result_label = Label(window4,width = 10, text = result).pack(side = LEFT)#回傳結果

	elif ask_messagebox == False or play_messagebo == False:
		notplay_messagebox = messagebox.showwarning("沒電影看還想耍任性?","不玩就不玩啊") 





movie_button = Button(window,text = "要看電影!", width = 15, height = 10,bg = "lightblue",command = checkdaytime)
game_button = Button(window,text = "要玩遊戲!", width = 15, height = 10, bg = "lightgreen",command = play1a2b)

label1.pack()
movie_button.pack(side = RIGHT, ipadx = 20, padx = 30)
game_button.pack(side = LEFT, ipadx = 20, padx = 30)


window.mainloop()