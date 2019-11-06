#!/usr/bin/env python3
# coding=utf-8
# noinspection PyUnresolvedReferences
import __init__

import os
import sqlite3 as db

from util import *


def main():
    new_data = db.connect(os.path.join(os.path.dirname(__file__), './db/app_details.db'))\
        .cursor().execute('SELECT * FROM app_details').fetchall()
    conn = db.connect(os.path.join(os.path.dirname(__file__), './db/pre_app_category.db'))
    conn.execute('CREATE TABLE IF NOT EXISTS "tb_pre_app_category" ' +
                 '("package_name" TEXT,"category" TEXT,PRIMARY KEY ("package_name"))')
    count_insert = 0
    count_update = 0
    count_skip = 0
    for row in new_data:
        pkg = row[0]
        raw = row[1]
        category = map_tx_category(raw)
        saved = conn.cursor().execute(
            'SELECT * FROM tb_pre_app_category WHERE package_name = "%s"' % pkg).fetchone()
        if saved is None:
            logger.i(__name__, 'insert pkg: %s' % pkg)
            count_insert += 1
            save_to_db(conn, pkg, category)
        else:
            if category != saved[1]:
                logger.i(__name__, 'update pkg: %s' % pkg)
                count_update += 1
                save_to_db(conn, pkg, category)
            else:
                logger.i(__name__, 'no need to change: %s' % pkg)
                count_skip += 1
    conn.commit()
    logger.i(__name__, 'finished: insert %d, update %d, skip %d' % (count_insert, count_update, count_skip))
    pass


def save_to_db(conn, pkg, category):
    conn.execute('INSERT OR REPLACE INTO tb_pre_app_category ' +
                 '(package_name, category) VALUES("%s", "%s")' % (pkg, category))
    pass


def map_tx_category(category):
    if u'动作冒险' == category \
            or u'休闲益智' == category \
            or u'动作冒险' == category \
            or u'休闲益智' == category \
            or u'网络游戏' == category \
            or u'棋牌中心' == category \
            or u'飞行射击' == category \
            or u'经营策略' == category \
            or u'角色扮演' == category \
            or u'体育竞技' == category \
            or u'游戏' == category:
        return AppClassify.TYPE_GAMES
    elif u'' == category or u'default' == category:
        return AppClassify.TYPE_FAILED
    else:
        return {
            u'视频': AppClassify.TYPE_VIDEO,
            u'音乐': AppClassify.TYPE_MUSIC,
            u'购物': AppClassify.TYPE_SHOP,
            u'阅读': AppClassify.TYPE_BOOK,
            u'导航': AppClassify.TYPE_MAPS,
            u'社交': AppClassify.TYPE_SOCIAL,
            u'摄影': AppClassify.TYPE_CAMERA,
            u'新闻': AppClassify.TYPE_NEWS,
            u'工具': AppClassify.TYPE_LIFESERVICE,
            u'美化': AppClassify.TYPE_LIFESERVICE,
            u'教育': AppClassify.TYPE_EXAM,
            u'生活': AppClassify.TYPE_LIFESERVICE,
            u'安全': AppClassify.TYPE_BOOST,
            u'旅游': AppClassify.TYPE_TRAVEL,
            u'儿童': AppClassify.TYPE_LIFESERVICE,
            u'理财': AppClassify.TYPE_INVESTMENT,
            u'系统': AppClassify.TYPE_BOOST,
            u'健康': AppClassify.TYPE_LIFESERVICE,
            u'娱乐': AppClassify.TYPE_LIFESERVICE,
            u'办公': AppClassify.TYPE_LIFESERVICE,
            u'通讯': AppClassify.TYPE_MESSAGING,
            u'出行': AppClassify.TYPE_MAPS
        }.get(category, AppClassify.TYPE_UNKNOWN)


class AppClassify:
    def __init__(self):
        pass
    TYPE_FAILED = 'FAILED'
    TYPE_UNKNOWN = 'UNKNOWN'
    TYPE_MESSAGING = 'MESSAGING'
    TYPE_MAILBOX = 'MAILBOX'
    TYPE_VOIP = 'VOIP'
    TYPE_WEATHER = 'WEATHER'
    TYPE_CLOCK = 'CLOCK'
    TYPE_NEWS = 'NEWS'
    TYPE_LIFESERVICE = 'LIFESERVICE'
    TYPE_VPN = 'VPN'
    TYPE_MUSIC = 'MUSIC'
    TYPE_BUSSINESS = 'BUSSINESS'
    TYPE_CAMERA = 'CAMERA'
    TYPE_VIDEO = 'VIDEO'
    TYPE_LIVESTREAMING = 'LIVESTREAMING'
    TYPE_MAPS = 'MAPS'
    TYPE_VEHICLE = 'VEHICLE'
    TYPE_TRAVEL = 'TRAVEL'
    TYPE_ACCOUNTS = 'ACCOUNTS'
    TYPE_TAXI = 'TAXI'
    TYPE_SHOP = 'SHOP'
    TYPE_BOOK = 'BOOK'
    TYPE_RECRUIT = 'RECRUIT'
    TYPE_PEDOMETER = 'PEDOMETER'
    TYPE_PAY = 'PAY'
    TYPE_BANK = 'BANK'
    TYPE_INVESTMENT = 'INVESTMENT'
    TYPE_GAMES = 'GAMES'
    TYPE_INDIVIDUATION = 'INDIVIDUATION'
    TYPE_MARRAGE = 'MARRAGE'
    TYPE_LIFESEVICE = 'LIFESEVICE'
    TYPE_LAUNCHER = 'LAUNCHER'
    TYPE_EXAM = 'EXAM'
    TYPE_LANGUAGELEARN = 'LANGUAGELEARN'
    TYPE_DICTIONARY = 'DICTIONARY'
    TYPE_DICTIONARYK = 'DICTIONARYK'
    TYPE_INPUTMETHOD = 'INPUTMETHOD'
    TYPE_BABYCARE = 'BABYCARE'
    TYPE_BOOST = 'BOOST'
    TYPE_BROWSER = 'BROWSER'
    TYPE_FILEMANAGE = 'FILEMANAGE'
    TYPE_MESSAGEING = 'MESSAGEING'
    TYPE_SOCIAL = 'SOCIAL'


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt as _:
        logger.key_interrupt()
    finally:
        logger.i(__name__, 'FINISHED')
