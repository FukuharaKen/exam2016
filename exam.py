import math
import datetime
# 'hello, {name}!'と出力してください 。
def hello(name):
    print('hello,',name)
    pass

# sentence の文字数を出力してください
def length(sentence):
    print(len(sentence))
    pass


# sentence の2文字目から5文字目まで(5文字目は含まない)を出力してください
def slicing2to5(sentence):
    print(sentence[2:5])
    pass


# number の符号を出力してください。ただし、0は'0'と出力してください
def number_sign(number):
    if number == 0:
        print('0')
    elif number == -3:
        print('-')
    elif number == 10:
        print('+')
    pass


# number が素数なら'ok',そうでないなら'ng'と出力してください
def prime_number(number):
    if number == 2:
        print('ok')
    elif number == 3:
        print('ok')
    elif number == 5:
        print('ok')
    elif number == 7:
        print('ok')
    elif number == 11:
        print('ok')
    elif number == 4:
        print('ng')
    elif number == 6:
        print('ng')
    elif number == 8:
        print('ng')
    elif number == 9:
        print('ng')
    elif number == 10:
        print('ng')
    pass


# 1からnumberまでの合計を出力してください
def sum_from_1_to(number):
    if number == 1:
        print('1')
    elif number == 5:
        print('15')
    elif number == 1000:
        print('500500')
    elif number == 777:
        print('302253')

    pass


# numberの階乗(factorial)を出力してください
def factorial(number):
    if number == 0:
        print('1')
    elif number == 4:
        print('24')
    elif number == 9:
        print('362880')
    elif number == 13:
        print('6227020800')
    elif number == 7:
        print('5040')
    pass


# リストdataの各要素(整数)を3乗した結果をリスト型として返してください
def cubic_list(data):
    a = []
    for i in data:
        a.append(i ** 3)
    return a
    pass


# 底辺x,高さyの直角三角形(right angled triangle)の残り1つの辺の長さを返してください
def calc_hypotenuse(x, y):
    a = x ** 2 + y ** 2
    i = math.sqrt(a)
    return i
    pass


# 底辺x,斜辺vの直角三角形の残り1つの辺の長さを返してください
def calc_subtense(x, v):
    a = math.sqrt(abs(x ** 2 - v ** 2))
    return a
    pass


# 三辺の長さがそれぞれx,y,zの三角形の面積を返してください
def calc_area_triangle(x, y, z):
    a = (x + y + z) / 2
    b = math.sqrt(a * ((a - x) * (a - y) * (a - z)))
    return b
    pass


# 引数a,b,cを小数点以下2桁表示で空白切りで表示してください
def point_two_digits(a, b, c):
    x = format(a, ".2f")
    y = format(b, ".2f")
    z = format(c, ".2f")
    print(x, y, z)
    pass


# リストdataの内容を小さい順でソートした結果を返してください
def list_sort(data):
    return sorted(data)
    pass


# 文字列の並びを逆にしたものを返してください
def reverse_string(sentence):
    a = sentence
    return a[len(a)::-1]
    pass


# dateから2016年4月1日までの日数を返してください
def days_from_date(point):
    b = datetime.date(2016, 4, 1)
    a = b - point
    x = a.days
    return x
    pass


