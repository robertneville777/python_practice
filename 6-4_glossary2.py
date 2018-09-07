glossary = {
    'dictionary':'Record of key-value pairs.',
    'list':'Basically an array containing elements of any type.',
    'tuple':'Like a list but cannot be modified.',
    'Zen of Python':'Python coding philosophy.',
    'PEP 8':'Python formatting guidelines.',
    'Python term 6':'Python definition 6.',
    'python term 7':'Python definition 7.',
    'python term 8':'Python definition 8.',
    'python term 9':'Python definition 9.',
    'python term 10':'Python definition 10.',
}

print("")

for word, definition in glossary.items():
    print(word.title() + ": " + definition + "\n")
