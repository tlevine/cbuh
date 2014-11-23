import ConfigParser

def sort(contacts):
    old = ConfigParser.ConfigParser()
    old.read(contacts)

    sections = list(sorted(old.sections()))
    data = [old.items(section) for section in sections]

    new = ConfigParser.ConfigParser()
    for section, data in zip(sections, data):
        new.add_section(section)
        for key, value in data:
            new.set(section, key, value)
    
    with open(contacts, 'w') as fp:
        new.write(fp)
