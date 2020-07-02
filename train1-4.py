debt = 250000                       #借入額
repay = 30000                       #毎月支払額
n = 1                               #返済にかかる月数

while 0 < debt :
    if repay < debt:                #借入+(借入 - 金利 ÷ 12ヶ月)
            debt = (debt + (debt * 0.14 /12)) - repay
            print(str(n) + "ヶ月目：返済額 = " + str(repay) + "円,残り" + str(debt) + "円" )
            n = n + 1
    else :
        debt = debt + (debt * 0.14 /12)
        print(str(n) + "ヶ月目：返済額 = " + str(debt) + "円,返済完了" )
        break