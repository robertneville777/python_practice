from collections import OrderedDict

glossary = OrderedDict()

glossary['dictionary'] = 'Record of key-value pairs.'
glossary['list'] = 'Basically an array containing elements of any type.'
glossary['tuple'] = 'Like a list but cannot be modified.'
glossary['Zen of Python'] = 'Python coding philosophy.'
glossary['PEP 8'] = 'Python formatting guidelines.'
glossary['Python term 6'] = 'Python definition 6.'
glossary['python term 7'] = 'Python definition 7.'
glossary['python term 8'] = 'Python definition 8.'
glossary['python term 9'] = 'Python definition 9.'
glossary['python term 10'] = 'Python definition 10.'

print("")

for word, definition in glossary.items():
    print(word.title() + ": " + definition + "\n")
