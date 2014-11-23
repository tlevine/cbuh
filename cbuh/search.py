import itertools
import json

import xapian

def queryparser(prefixes):
    '''
    Takes a list of prefixes
    '''
    q = xapian.QueryParser()
    q.set_stemmer(xapian.Stem('en'))
    q.set_stemming_strategy(q.STEM_SOME)
    for prefix in prefixes:
        q.add_prefix(prefix, prefix)
    return q

def search(database, prefixes, search):
    db = xapian.Database(database)

    with open(prefixes, 'r') as fp:
        p = json.load(fp)
    q = queryparser(p)

    query = q.parse_query(search)
    enquire = xapian.Enquire(db)
    enquire.set_query(query)

    persons = set()
    for offset in itertools.count(0, 1):
        matches = enquire.get_mset(offset, 100)
        if matches.size() > 0:
            for match in matches:
                person = match.document.get_data()
                if person not in persons:
                    persons.add(person)
                    yield person
        else:
            break
