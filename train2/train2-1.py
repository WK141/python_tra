def calc_time(distance , speed):
    result = distance / speed
    return result

# TODO: 例外処理を組み込む
print("速度を入力してください(/km)")
speed = int(input())
print("距離を入力してください(km)")
distance = int(input())

time = calc_time(speed,distance)

print(str(time) + "時間かかります")