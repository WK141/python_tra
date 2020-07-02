print("身長を入力してください(m)")  
height = float(input())
print("体重を入力してください(kg)")
weight = float(input())

bmi = weight / (height ** 2) 

if bmi < 18.5 :
    j = "やせ"
elif bmi < 25 :
    j = "標準"
elif bmi < 30 :
    j = "肥満"
else :
    j = "高度な肥満"

print("あなたは「" + str(j) + "」です。")