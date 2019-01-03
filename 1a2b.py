import random
game = True

while game:
  a = input("嗨挑戰者！我們來玩1A2B吧！ Y/N")
  if a == "Y" or a == "y" :
    playornot = True
    break
  elif a == "N" or a == "n" :
    playornot = False
    print("沒電影看還想耍任性?")
    print("不玩就不玩啊")
    break
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
        break
    else:
      print("請再輸入一次！")

    


