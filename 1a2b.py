import random
import os
playornot = True


  
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
			times += 1
			if times == 1:
				playornot = False
				starttoback = True
				break
		else:
			print("請再輸入一次！")
def backtomainpage():
	os.system('C:\\Users\\mikem\\Desktop\\Final-Project-Team-10\\PBC-Final-Project-Team-10\\20190107介面.py')
while starttoback:
	backornot = input("是否回到主程式? Y/N")
	if backornot == 'Y' or backornot == 'y':
		backtomainpage()
		starttoback = False
		break
	elif  backornot == 'N' or backornot == 'n':
		print("BYE")
		starttoback = False
		break
	else:
		print("請再輸入一次！")

	


