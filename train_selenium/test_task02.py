#ひとつ上の階層をpathに追加
import os
import sys
path = os.path.join(os.path.dirname(__file__), '../')
sys.path.append(path)
from train2 import train2_2

#train2_2の条件分岐をすべて通るようなテストパターンを用意
#関数は分けなくても良い
def test_is_leap_yearDiv400():
    year = 2000
    actual = train2_2.is_leap_year(year)
    assert actual == True

def test_is_leap_yearNotDiv100():
    year = 1900
    actual = train2_2.is_leap_year(year)
    assert actual == False

def test_is_leap_yearDiv4():
    year = 2020
    actual = train2_2.is_leap_year(year) 
    assert actual == True

def test_is_leap_yearElse():
    year = 1999
    actual = train2_2.is_leap_year(year)
    assert actual == False