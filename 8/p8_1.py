#15816079　久田祐輝
for x in range(1, 10):
    print(repr(x).rjust(2), end = ' ')
    for y in range(2, 10):
        print(repr(x*y).rjust(2), end = ' ')
    print(' ')
