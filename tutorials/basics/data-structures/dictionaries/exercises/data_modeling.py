# Sample playlist data model in python.
playlist =  {
    "title":"My playlist",
    "author":"Abhinav Mishra",
    "songs": [{
    "name":"Turn it off",
    "artists":["Culture Abuse"],
    "album":"Peach",
    "date":"2017-10-31",
    "length":"3:37"
    },
    {
    "name":"song_2",
    "artists":["test","test2"],
    "album":"Peach",
    "date":"2017-10-31",
    "length":"3:37"
    }]
}

for song in playlist['songs']:
    print(song["name"])