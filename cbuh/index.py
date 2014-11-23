import os
import ConfigParser

import xapian

termgenerator = xapian.TermGenerator()
termgenerator.set_stemmer(xapian.Stem("en"))

def index(contacts, database):
    c = ConfigParser.ConfigParser()
    c.read(contacts)

    db = xapian.WritableDatabase(database, xapian.DB_CREATE_OR_OPEN)

    for section in c.sections():
        doc = xapian.Document()
        termgenerator.set_document(doc)

        termgenerator.index_text(section, 1, 'id')
        for prefix, content in c.items(section):
            termgenerator.index_text(content, 1, prefix)
            termgenerator.index_text(content)
            termgenerator.increase_termpos()

    doc.add_boolean_term(section)
    db.replace_document(section, doc)
