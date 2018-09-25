"""
Dump the 'db' database into a file called 'people-pickle'
"""

from initdata import db
import pickle

dbfile = open('people-pickle', 'wb')
pickle.dump(db, dbfile)
dbfile.close()
