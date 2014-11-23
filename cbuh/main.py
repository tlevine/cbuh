import argparse

from .index import index
#from .mutt import mutt
#from .search import search

def parser():
    epilog = '''
Search the contact list in ~/.cbuh. The search is an ordinary Xapian
query (http://xapian.org/docs/queryparser.html) with some prefixed terms.

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
    p.add_argument('search', metavar = '[search term]', nargs = '*',
        help = 'The search terms, if you\'re running a search')
    return p


def cli():
    p = parser()
    a = p.parse_args()

    if a.index:
        index()

    if a.mutt:
        mutt()

    if len(a.search) > 0:
        search(a.search)
