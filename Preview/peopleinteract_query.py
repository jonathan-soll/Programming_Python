# interactive queries

import shelve

fieldnames  = ('name', 'age', 'job', 'pay')
maxfield    = max(len(f) for f in fieldnames) # length of longest word

db = shelve.open('class-shelve') # store the shelve 'db'

while True:
    key = input('\nKey? => ')
    if not key: break # if nothing is given (empty line) break the loop
    try:
        record = db[key]
    except:
        print('No such key %s!' % key)
    else:
        for field in fieldnames:
            "Print the value of 'field' for the 'record' object"
            print(field.ljust(maxfield), '=>', getattr(record, field))
