# database of albums or tracks

albums = {
    'address' : "mongodb://localhost:27017/",
    'database' : 'dhh',
    'collection' : 'albums'
}


# database of artists

artists = {
    'address' : 'mongodb://localhost:27017/',
    'database' : 'dhh',
    'collection' : 'artists_list'
}

# artists{
#     {artist1},
#     {artist2},
#     ....
# }
# 
# artist{
#     artist : 'artist name',
#     spotify_id : 'spotifyid',
#     total : total no of tracks # including features
# }

