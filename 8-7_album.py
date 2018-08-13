def make_album(artist_str,album_str,num_tracks=0):
    music = {'artist':artist_str, 'album':album_str}
    if num_tracks:
        music['number of tracks'] = num_tracks
    return music

artist1 = make_album('underoath','define the great line')
artist2 = make_album('as i lay dying','an ocean between us')
artist3 = make_album('oceana','the tide')
artist4 = make_album('of machines','as if everything was held in place',11)
print(artist1)
print(artist2)
print(artist3)
print(artist4)
