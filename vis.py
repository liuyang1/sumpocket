#! /usr/bin/env python2
import sys


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


def fmtLineTpl(tplfn, data):
    tpl = loadTpl(tplfn)
    d = {}
    d['username'] = 'pocket4t'
    date = [t[0] for t in data]
    // sumdata = [int(t[1]) for t in data]
    adddata = [int(t[2]) for t in data]
    deldata = [-1 * int(t[3]) for t in data]
    d['date'] = str(date)
    d['adddata'] = str(adddata)
    d['deldata'] = str(deldata)
    r = tpl % d
    return r


def fmtKTpl(tplfn, data):
    tpl = loadTpl(tplfn)
    d = {}
    d['username'] = 'pocket4t'
    date = [t[0] for t in data]
    d['date'] = str(date)
    kdata = [(int(t[1]), int(t[2]), int(t[3])) for t in data]
    kdata = [[a0 + a2 - a1 , a0, a0 - a1, a0 + a2] for a0, a1, a2 in kdata]
    d['kdata'] = str(kdata)
    r = tpl % d
    return r



def LineTpl():
    data = loadData('update')
    r = fmtLineTpl('vis.html.tpl', data)
    print(r)


def KTpl():
    data = loadData('update')
    r = fmtKTpl('kvis.html.tpl', data)
    print(r)


def usage():
    print("python2 vis.py [line/k]")


if __name__ == "__main__":
    if sys.argv[1] == "line":
        LineTpl()
    elif sys.argv[1] == "k":
        KTpl()
    else:
        usage()
