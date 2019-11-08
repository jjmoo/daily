#!/usr/bin/env python3
# coding=utf-8
# noinspection PyUnresolvedReferences
import __init__

import os
import google
import myapp
import crawler
import record

from util import *

pkg_list = []
failed_list = []
died_list = []

with open(os.path.join(os.path.dirname(__file__), './input/pkg_list.txt'), 'r') as fr:
    for line in fr.readlines():
        pkg_list.append(line.split(':')[1].strip())

for pkg in pkg_list:
    target_url = myapp.app_detail_url_format % pkg
    content = crawler.get_content(target_url)
    _, category, name, download = myapp.parse_app_detail(target_url, content)
    if category is not None and len(category.strip()) > 0:
        record.update(pkg, category, name, download)
    else:
        failed_list.append(pkg)

logger.w(__name__, 'failed to get from tencent [%d]: %s' % (len(failed_list), failed_list))

for pkg in failed_list:
    target_url = google.app_detail_url_format % pkg
    content = crawler.get_content(target_url)
    pkg, category_top, category_sub, name, download = google.parse_app_detail(target_url, content)
    if category_sub is not None and len(category_sub.strip()) > 0:
        record.update(pkg, category_top + '::' + category_sub, name, download)
    else:
        died_list.append(pkg)

logger.w(__name__, 'failed to get from google [%d]: %s' % (len(died_list), died_list))

