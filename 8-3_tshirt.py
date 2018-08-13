def get_formatted_name(first_name,last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi','hendrix')
print(musician)

def make_shirt(size,text):
    """Print size of shirt and message"""
    print('Making a ' + size + ' shirt displaying the text "' + text + '".')

make_shirt('large','fox')
make_shirt(text='fox',size='large')
