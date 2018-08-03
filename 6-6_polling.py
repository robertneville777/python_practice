friends = ['jen','edward','ryan','john']

favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }

for person in friends:
    if person in set(favorite_languages.keys()):
        print("Thanks for taking the poll, " + person.title() +  ".")
    else:
        print(person.title() + ", please take our poll.")
