# ------------------------------------------------- #
# Title: Assignment 07 Pickling
# Description: A simple example of pickling from
# https://www.geeksforgeeks.org/understanding-python-pickling-example/
# ChangeLog: (Who, When, What)
# PChuoy,<8.23.2023>,Copied Script and modified
# ------------------------------------------------- #

import pickle


def storeData():
    # initializing data to be stored in db
    Omkar = {'key': 'Omkar', 'name': 'Omkar Pathak',
             'age': 21, 'pay': 40000}
    Jagdish = {'key': 'Jagdish', 'name': 'Jagdish Pathak',
               'age': 50, 'pay': 50000}

    # database
    db = {}
    db['Omkar'] = Omkar
    db['Jagdish'] = Jagdish

    # Its important to use binary mode
    dbfile = open('examplePickle.dat', 'ab')

    # source, destination
    pickle.dump(db, dbfile)
    dbfile.close()


def loadData():
    # for reading also binary mode is important
    dbfile = open('examplePickle.dat', 'rb')
    db = pickle.load(dbfile)
    for keys in db:
        print(keys, '=>', db[keys])
    dbfile.close()


if __name__ == '__main__':
    storeData()
    loadData()