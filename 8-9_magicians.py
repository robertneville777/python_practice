def show_magicians(magician_list):
    """ Prints the name of each magician in the input list """
    for magician in magician_list:
        print(magician.title() + ' has some mind-boggling sleight of hand skills.')

beastly_magicians = ['bob','bill','daniel','conrad osborne','pastor neipp']

show_magicians(beastly_magicians)
