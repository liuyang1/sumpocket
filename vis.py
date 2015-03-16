#! /usr/bin/env python2

def loadData(fn):
    with open(fn) as fp:
        lst = []
        for line in fp.readlines():
            t = line.split()
            lst.append(t)
        return lst


def loadTpl(fn):
    with open(fn) as fp:
        return fp.read()


def fmtTpl(tpl, data):
    d = {}
    d['username'] = 'pocket4t'
    date = [t[0] for t in data]
    sumdata = [int(t[1]) for t in data]
    adddata = [int(t[2]) for t in data]
    deldata = [-1 * int(t[3]) for t in data]
    d['date'] = str(date)
    d['adddata'] = str(adddata)
    d['deldata'] = str(deldata)
    r = tpl % d
    return r

if __name__ == "__main__":
    tpl = loadTpl('vis.html.tpl')
    data = loadData('update')
    r = fmtTpl(tpl, data)
    print(r)

