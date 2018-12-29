import random



a = input("嗨挑戰者！我們來玩1A2B吧！ Y/N")
if a == "Y":
  True
elif a == "N":
  True #原則上要上一頁
else:
  print("請重新輸入好ㄇ!")

print('注意！你只有10次機會！！')
while True:

  items = [1,2,3,4,5,6,7,8,9,0]
  random.shuffle(items)
  items = "".join('%s' %id for id in items)
  answer = items[0:4]
  
  time = 0

  while time < 10:
    challenger = input("已嘗試次數：%d 請輸入數字" %time)
    time += 1
    A = 0
    B = 0

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
    if playagain == 'Y' or playagain == 'N':
      break
    else:
      print("請再輸入一次！")
  #這邊要寫if playagain ==怎樣就會怎樣
    

  