#! /usr/bin/env python2

import sys
import urllib
import urllib2
import json
import datetime
import logging
from conf import *
from datetime import date

# logger = logging.getLogger('sumpocket')
# logger.setlevel(logging.INFO)
def post(url, dct):
    dct["state"] = "unread"
    dct["detailType"] = "simple"
    data = urllib.urlencode(dct)
    req = urllib2.urlopen(url, data)
    rsp = req.read()
    return rsp


def parse(txt):
    d = json.loads(txt)
    ks = d["list"].keys()
    return ks


hist = "histfile"
upfn = "update"
def loadHist(fn):
    with open(fn) as fp:
        txt = fp.read()
        return json.loads(txt)


def saveHist(fn, data):
    with open(fn, "w") as fp:
        fp.write(json.dumps(data, sort_keys=True, indent=4))


def saveUpdate(fn, c):
    with open(fn, "a") as fp:
        t = date.strftime(date.today(), "%Y-%m-%d")
        s = t + " %d %d %d\n" % (c[0], c[1], c[2])
        fp.write(s)


def cmp(old, new):
    a = [i for i in new if i not in old]
    d = [i for i in old if i not in new]
    return len(new), len(a), len(d)

if __name__ == "__main__":
    print("post")
    rsp = post('https://getpocket.com/v3/get', conf)
    new = parse(rsp)
    old = loadHist(hist)
    c = cmp(old, new)
    print(c)
    saveUpdate(upfn, c)
    saveHist(hist, new)
    print("save")
