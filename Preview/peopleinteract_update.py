# interactive queries and updates

import shelve
from person import Person

fieldnames  = ('name', 'age', 'job', 'pay')

db = shelve.open('class-shelve') # store the shelve 'db'

while True:
    key = input('\nKey? => ')
    if not key: break # if nothing is given (empty line) break the loop
    if key in db:
        record = db[key] # set 'record' to existing record
    else:
        record = Person(name = '?', age = '?')

    for field in fieldnames:
        currval = getattr(record, field)
        newtext = input('\t[%s]=%s\n\t\tnew?=>' % (field, currval))
        if newtext:
            setattr(record, field, eval(newtext))
    db[key] = record

db.close()
