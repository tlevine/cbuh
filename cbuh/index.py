import os
import json
import ConfigParser

import xapian

# This might be interesting eventually
# http://xapian.org/docs/omega/termprefixes.html

termgenerator = xapian.TermGenerator()
termgenerator.set_stemmer(xapian.Stem("en"))

def index(contacts, database, prefixes):
    c = ConfigParser.ConfigParser()
    c.read(contacts)

    db = xapian.WritableDatabase(database, xapian.DB_CREATE_OR_OPEN)

    p = set()
    for person in c.sections():
        doc = xapian.Document()
        termgenerator.set_document(doc)

        termgenerator.index_text(person, 1, u'id')
        for prefix, content in c.items(person):
            termgenerator.index_text(content, 1, u'X' + prefix)
            termgenerator.index_text(content)
            termgenerator.increase_termpos()
            p.add(prefix)

        doc.add_boolean_term(u'Q' + person)
        doc.set_data(person)
        db.replace_document(u'Q' + person, doc)

    with open(prefixes, 'wb') as fp:
        json.dump(list(p), fp)

