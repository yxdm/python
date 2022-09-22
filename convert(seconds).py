#接收一个表示纪元秒数的正整数seconds，也就是从1970年1月1日8时0分0秒到目前为止经过的秒数
#要求返回纪元秒数seconds对应的日期时间字符串。
#例如：main（1601901810）返回‘2020-10-05_20：43：30’日期和时间之间有一个下画线
from time import strftime,localtime

def convert(seconds):
    return strftime('%Y-%M-%d_%H:%m:%S',localtime(seconds))

print(convert(1601901810))
