debt = 250000                       #借入額
repay = 30000                       #毎月支払額
month = 0                               

while 0 < debt :
    debt = debt + (debt * 0.14 / 12)    #借入+(借入 - 金利 ÷ 12ヶ月)
    month = month + 1        
    if repay < debt :           
        debt = debt - repay 
        print(str(month) + "ヶ月目：返済額 = " + str(repay) + "円,残り" + str(debt) + "円" )
    else :
        repay = debt
        print(str(month) + "ヶ月目：返済額 = " + str(debt) + "円,返済完了" )
        debt = 0