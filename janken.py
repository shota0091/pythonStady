import random

def junkenPon(num):
  print("ジャンケン！")
  junken = ["グー","チョキ","パー"]
  myHund = num
  yourHund = random.randrange(3)
  if myHund == 0 and yourHund == 1 or myHund == 1 and yourHund == 2 or myHund == 2 and yourHund == 0:
    print("あなた："+junken[myHund]+" 相手："+ junken[yourHund]+"であなたの勝ち")
  elif myHund == 2 and yourHund == 1 or myHund ==1  and yourHund == 0 or myHund == 0 and yourHund == 2:
    print("あなた："+junken[myHund]+" 相手："+ junken[yourHund]+"であなたの負け")
  else:
    print("あなた："+junken[myHund]+" 相手："+ junken[yourHund]+"であいこ")
  


while True:
  num = input("ジャンケンするよ 1.開始 2.やめる")
  if int(num) == 1:
    jnk = input("ジャンケン！ 1:グー 2:チョキ 3:パー")
    junkenPon(int(jnk))
  elif int(num) == 2:
    break
  else:
    print("1~3で入力してね")