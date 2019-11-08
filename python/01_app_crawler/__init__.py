import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

db_dir = os.path.join(os.path.dirname(__file__), './db')
if not os.path.exists(db_dir):
    os.mkdir(db_dir)
