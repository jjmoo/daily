#!/usr/bin/env python3
# coding=utf-8
# noinspection PyUnresolvedReferences
import __init__

import myapp
import record
import requests

from util import *

timeout = 30
requests_header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/54.0.2840.87 Safari/537.36'}


def get_content(url):
    return requests.get(url, headers=requests_header, timeout=timeout).content.decode('utf-8')


def main():
    url_checked = []
    pkg_added = []
    url_queue = [myapp.get_seed_url()]
    count_url = 1
    while len(url_queue) is not 0:
        target_url = url_queue.pop(0)
        content = get_content(target_url)
        pkg, category, name, download, child = myapp.parse_target(target_url, content)
        if target_url not in url_checked:
            url_checked.append(target_url)
        for url in child:
            if url not in url_checked and url not in url_queue:
                url_queue.append(url)
                count_url += 1
        if pkg is not None and category is not None and len(pkg.strip()) > 0 and len(category.strip()) > 0:
            if pkg not in pkg_added:
                pkg_added.append(pkg)
            record.update(pkg, category, name, download)
            logger.d(__name__, 'update pkg: [' + name + '] ' + pkg + ' --> ' + category)
        logger.i(__name__, 'pkg_cnt: ' + str(len(pkg_added)) +
                 ', url_queue_size: ' + str(len(url_queue)) + '/' + str(count_url) +
                 ', current url: ' + target_url)
    pass


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt as _:
        logger.key_interrupt(__name__)
    finally:
        logger.i(__name__, 'FINISHED')
