import os
import sqlite3 as db

update_db_format = 'INSERT OR REPLACE INTO app_details (pkg, category, name, download) VALUES("%s", "%s", "%s", "%s")'

conn = db.connect(os.path.join(os.path.dirname(__file__), './db/app_details.db'))
conn.execute('CREATE TABLE IF NOT EXISTS `app_details` ('
             '`pkg` TEXT NOT NULL, `category` TEXT NOT NULL, `name` TEXT, `download` TEXT,  PRIMARY KEY(`pkg`))')
conn.commit()


def update(pkg, category, name, download):
    if name is None:
        name = 'NULL'
    if download is None:
        download = 'NULL'
    conn.execute(update_db_format % (pkg, category, name, download))
    conn.commit()
    pass
