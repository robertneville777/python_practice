def make_great(old_magician_list,new_magician_list):
    """ Appends the str -- the great -- to the input string """
    while old_magician_list:
        cur_magician = old_magician_list.pop() + ' the Great'
        new_magician_list.append(cur_magician) 
        #print(magician)
    #return magician_list

def show_magicians(magician_list):                                              
    """ Prints the name of each magician in the input list """                  
    for magician in magician_list:                                              
        print(magician.title() + 
        ' has some mind-boggling sleight of hand skills.')

new_mag_list = []
old_mag_list = ['billy','happy','deeds']
make_great(old_mag_list,new_mag_list)
show_magicians(new_mag_list)

original_mag_list = ['hudini','dude from batman','wolverine actor']
modified_mag_list = []

make_great(original_mag_list[:],modified_mag_list)
show_magicians(original_mag_list)
show_magicians(modified_mag_list)
