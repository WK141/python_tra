from PIL import Image
import math

im =Image.open('compare.png')

def calc_size(im):
    height = im.size[0]
    wide = im.size[1]
    max_common_number = math.gcd(height,wide)
    height_divisor = int(height / max_common_number)
    wide_divisor = int(wide / max_common_number) 
    print("高さは" + str(height) + "、画像の幅は" + str(wide) + "、アスペクト比は"  + str(height_divisor) + ":" +str(wide_divisor))
    
calc_size(im)