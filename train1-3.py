print("身長を入力してください(m)")  
height = float(input())
print("体重を入力してください(kg)")
weight = float(input())

bmi = weight / (height ** 2) 

if bmi < 18.5 :
    judge = "やせ"
elif bmi < 25 :
    judge = "標準"
elif bmi < 30 :
    judge = "肥満"
else :
    judge = "高度な肥満"

print("あなたは「" + str(judge) + "」です。")