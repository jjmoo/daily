#!/usr/bin/env python3
# coding=utf-8
# noinspection PyUnresolvedReferences
import __init__

import os
import sqlite3 as db

from util import *
import classify


def map_category(raw):
    if '::' in raw:
        parts = raw.split('::')
        return classify.map_gl_category(parts[0], parts[1])
    else:
        return classify.map_tx_category(raw)


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
        category = map_category(raw)
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


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt as _:
        logger.key_interrupt()
    finally:
        logger.i(__name__, 'FINISHED')
