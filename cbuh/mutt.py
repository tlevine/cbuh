import ConfigParser

def mutt(contacts):
    '''
    Convert each contact to a mutt alias, using the first email address
    field and (optionally) the first name field.
    '''
    c = ConfigParser.ConfigParser()
    c.read(contacts)
    for person in c.sections():
        name = None
        email = None
        for key, value in reversed(c.items(person)):
            if key == 'email':
                email = value
            elif key == 'name':
                name = value
        if email != None and name != None:
            yield 'alias %s %s <%s>' % (person, name, email)
        elif email != None and name == None:
            yield 'alias %s <%s>' % (person, email)
