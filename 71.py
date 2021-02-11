import math
def mysqur(a):
    x=a/2
    while True:

        y = (x + a/x) / 2
        if y == x:
            break
        x = y
    return x

def test_square_root():
    b=1.0
    print('a','   ', 'mysqrt(a)  ', '              ','math.sqrt(a)              ', 'diff     ')
    print('-','   ', '---------  ', '              ','------------              ', '----     ')
    while b<=9:
        print(b,' ', mysqur(b),' '*(25 -len(str(mysqur(b)))), math.sqrt(b),' '*(25 -len(str(math.sqrt(b)))), (mysqur(b)-math.sqrt(b)))
        b=b+1

test_square_root()