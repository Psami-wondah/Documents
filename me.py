
def do_twice(f, s):
    f(s)
    f(s)


def print_spam():
    print('spam')

def print_twice(bruce):
    print(bruce)
    print(bruce)


def do_four(r, d):
    do_twice(r, d)
    do_twice(r, d)

do_four(print_twice, 'spam')    








