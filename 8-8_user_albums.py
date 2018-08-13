def make_album(artist_str,album_str,num_tracks=0):                              
    music = {'artist':artist_str, 'album':album_str}                            
    if num_tracks:                                                              
        music['number of tracks'] = num_tracks                                  
    return music

user_album = {}

while True:
    print("Enter 'q' anytime to exit.")
    art_in = input('Please enter artist name: ')
    if art_in == 'q':
        break
    alb_in = input('Please enter album name: ')
    if alb_in == 'q':
        break
    num_tr = input('Please enter number of tracks: ')
    if num_tr == 'q':
        break

    user_album = make_album(art_in,alb_in,num_tr)

    print(user_album)
