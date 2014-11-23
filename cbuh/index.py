import os

import xapian

def index():
    pass

'''
db = xapian.WritableDatabase(dbpath, xapian.DB_CREATE_OR_OPEN)
def reify(db, record):
    record = _convert(record)

    reified_document = xapian.Document()
    termgenerator.set_document(reified_document)

    for field, term in terms.items():
        termgenerator.index_text(record.get(field, u''), 1, term['code'])

    for field in general:
        termgenerator.index_text(record.get(field, u''))
        termgenerator.increase_termpos()

    for field, term in values.items():
        if field in record:
            reified_document.add_value(term['slot'], record[field])

    reified_document.set_data(json.dumps(record))

    identifier = u'Q' + record['id']
    reified_document.add_boolean_term(identifier)
    db.replace_document(identifier, reified_document)
'''
