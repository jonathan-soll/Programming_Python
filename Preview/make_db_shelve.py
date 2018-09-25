"""
Create 'people-shelve' database containing 'bob' and 'sue'
"""

from initdata import bob, sue
import shelve

db = shelve.open('people-shelve')
db['bob'] = bob
db['sue'] = sue
db.close()
