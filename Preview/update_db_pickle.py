"""
Load the pickled database
Update the 'pay' for 'sue'
Update the 'name' for 'tom'
Pickle the database
"""

import pickle

dbfile = open('people-pickle', 'rb')
db = pickle.load(dbfile)
dbfile.close()

db['sue']['pay'] *= 1.10
db['tom']['name'] = 'Tom Tom'

dbfile = open('people-pickle', 'wb')
pickle.dump(db, dbfile)
dbfile.close()
