# -*- coding:utf8 -*-

if __name__ == "__main__":
    l = []
    ls = []
    for i in range(31):
        d = 'day_' + str(i+1)
        l.append(d)
    # print('\n,'.join(l))
    for f in l:
        fs = f  + ' int'
        ls.append(fs)
    print('\n,'.join(ls))
    #