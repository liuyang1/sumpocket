#! /usr/bin/env python2

import sys
import urllib
try:
    import urllib2
except ImportError:
    print("use python2 instead")
    sys.exit()
import json
import logging
import logging.config
import conf
from datetime import date

with open('logging.json') as fp:
    logcfg = json.load(fp)
    logging.config.dictConfig(logcfg)

log = logging.getLogger('sumpocket')
hist = "histfile"
upfn = "update"


def post(url, dct):
    dct["state"] = "unread"
    dct["detailType"] = "simple"
    data = urllib.urlencode(dct)
    log.debug(data)
    try:
        req = urllib2.urlopen(url, data)
    except urllib2.HTTPError:
        log.fatal('bad request')
        sys.exit()
    rsp = req.read()
    return rsp


def parse(txt):
    d = json.loads(txt)
    ks = d["list"].keys()
    return ks


def loadHist(fn):
    with open(fn) as fp:
        txt = fp.read()
        return json.loads(txt)
    log.warn("not exist histfile")
    return []


def saveHist(fn, data):
    with open(fn, "w") as fp:
        fp.write(json.dumps(data, sort_keys=True, indent=4))


def saveUpdate(fn, c):
    with open(fn, "a") as fp:
        t = date.strftime(date.today(), "%Y-%m-%d")
        s = t + " %d %d %d\n" % (c[0], c[1], c[2])
        fp.write(s)


def cmpId(old, new):
    a = [i for i in new if i not in old]
    d = [i for i in old if i not in new]
    return len(new), len(a), len(d)

if __name__ == "__main__":
    arg = sys.argv
    if len(arg) >= 2:
        test = arg[1] == "test"
    else:
        test = False
    if test:
        log.info("test mode")
    log.info("post")
    rsp = post('https://getpocket.com/v3/get', conf.conf)
    new = parse(rsp)
    old = loadHist(hist)
    c = cmpId(old, new)
    log.info(str(c))
    if not test:
        saveUpdate(upfn, c)
        saveHist(hist, new)
        log.info("save")
    else:
        log.info("not save under test mode")
