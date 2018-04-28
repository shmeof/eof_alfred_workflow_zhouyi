#!/usr/bin/python
# encoding: utf-8

import sys
from workflow import Workflow3
import urllib2
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf-8')

def get_64(gua_key):
    url = 'https://www.gushiwen.org/guwen/zhouyi.aspx'
    content = urllib2.urlopen(url).read()
    soup = BeautifulSoup(content)
    gualist = soup.find("ul")
    alist = gualist.find_all("a")
    gua64 = dict();
    for a in alist:
        ahref = a.get("href")
        gname = a.get_text()
        gua64[gname] = ahref
    return gua64[gua_key]

def main(wf):
    args = wf.args
    if len(args) <= 0:
        wf.send_feedback()
        return

    try:
        # 六十四卦
        gua_url = get_64(args[0])
        content = urllib2.urlopen(gua_url).read()
        soup = BeautifulSoup(content)
        contsonSoup = soup.find("div", class_="contson")
        # aflred show
        for item in contsonSoup.strings:
            wf.add_item(title=item, subtitle=item, icon="")
        wf.send_feedback()
    except:
        tet = 0
    finally:
        tet = 1

if __name__ == '__main__':
    wf = Workflow3()
    sys.exit(wf.run(main))
