import os
import sys
import argparse

from .index import index
from .search import search
#from .mutt import mutt

def parser():
    DIR = os.path.expanduser('~/.cbuh')
    epilog = '''
Search the contact list in ~/.cbuh/contacts. The search is an ordinary Xapian
query (http://xapian.org/docs/queryparser.html) with whatever prefixed terms
you like. I suggest these.

* id
* name
* email
* phone
* place

If you apply these prefixes, you search within that field only;
for example, "name:Francisco" searches for people with names like
"Francisco". Searching for simply "Francisco", on the other hand,
will also match everyone who lives in San Francisco.
'''
    p = argparse.ArgumentParser(description = 'Query the contact list.',
        epilog = epilog, formatter_class = argparse.RawDescriptionHelpFormatter)
    p.add_argument('-m', '--mutt', action = 'store_true', default = False,
        help = 'Export the contact list as a mutt alias file.')
    p.add_argument('-i', '--index', action = 'store_true', default = False,
        help = 'Index the contact list.')
    p.add_argument('-c', '--contacts', metavar = 'path', action = 'store',
        default = os.path.join(DIR, 'contacts'), help = 'The contacts file')
    p.add_argument('-d', '--database', metavar = 'path', action = 'store',
        default = os.path.join(DIR, 'db'), help = 'The database directory')
    p.add_argument('-p', '--prefixes', metavar = 'path', action = 'store',
        default = os.path.join(DIR, 'prefixes'), help = 'The prefixes file')
    p.add_argument('search', metavar = '[search term]', nargs = '*',
        help = 'The search terms, if you\'re running a search')
    return p


def cli():
    p = parser()
    a = p.parse_args()

    if a.index:
        index(a.contacts, a.database, a.prefixes)

    if a.mutt:
        mutt(a.contacts)

    if len(a.search) > 0:
        for person in search(a.database, a.prefixes, ' AND '.join(a.search)):
            sys.stdout.write(person + '\n')

    if len(a.search) == 0 and (not a.mutt) and (not a.index):
        p.print_help()
        sys.exit(2)
