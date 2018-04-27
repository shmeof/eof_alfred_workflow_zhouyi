#!/usr/bin/python
# encoding: utf-8

import sys
from workflow import Workflow3

def main(wf):
    args = wf.args

    import urllib2
    from bs4 import BeautifulSoup

    reload(sys)
    sys.setdefaultencoding('utf-8')

    url = 'https://so.gushiwen.org/guwen/bookv_218.aspx'
    content = urllib2.urlopen(url).read()
    soup = BeautifulSoup(content)
    contsonSoup = soup.find("div", class_="contson")

    for item in contsonSoup.strings:
        wf.add_item(title=item, subtitle=item)
    wf.send_feedback()

if __name__ == '__main__':
    # Create a global `Workflow3` object
    wf = Workflow3()
    # Call your entry function via `Workflow3.run()` to enable its
    # helper functions, like exception catching, ARGV normalization,
    # magic arguments etc.
    sys.exit(wf.run(main))