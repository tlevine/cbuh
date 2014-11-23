queryparser = xapian.QueryParser()
queryparser.set_stemmer(xapian.Stem("en"))
queryparser.set_stemming_strategy(queryparser.STEM_SOME)
queryparser.add_prefix("title", "S")
queryparser.add_prefix("description", "XD")
queryparser.add_boolean_prefix('id')

def search(database, search)
    db = xapian.Database(database)
