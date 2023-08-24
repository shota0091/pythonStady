num = input("好きな数字を入れてね >")
intNum = int(num)
if intNum % 3 == 0 and intNum % 5 == 0:
  print("FuzzBuzz")
elif intNum % 3 == 0:
  print("Fuzz")
elif intNum % 5 == 0:
  print("Buzz")
else:
  print(intNum)