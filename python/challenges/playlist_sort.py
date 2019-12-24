"""
Implement a solution to re-arrange a list of N tracks on a playlist.
The position field of each track must reflect the order. If a position
is given out of range the list should be returned in the current order.

The list data will be in the format displayed in the examples below.

Ex. Move the track data in index 0 to index 2 and update the positions.

initial:

[
    {
        'playlist_id': 1,
        'track_id': 3212,
        'position': 1,
    },
    {
        'playlist_id': 1,
        'track_id': 3213,
        'position': 2,
    },
    {
        'playlist_id': 1,
        'track_id': 3214,
        'position': 3,
    },
    {
        'playlist_id': 1,
        'track_id': 3216,
        'position': 4,
    },
    {
        'playlist_id': 1,
        'track_id': 3217,
        'position': 5,
    },
]

result:

[
    {
        'playlist_id': 1,
        'track_id': 3213,
        'position': 1,
    },
    {
        'playlist_id': 1,
        'track_id': 3214,
        'position': 2,
    },
    {
        'playlist_id': 1,
        'track_id': 3212,
        'position': 3,
    },
    {
        'playlist_id': 1,
        'track_id': 3216,
        'position': 4,
    },
    {
        'playlist_id': 1,
        'track_id': 3217,
        'position': 5,
    },
]

"""

def playlist_sort(playlist_tracks, track_id, position):
    if (position > len(playlist_tracks)):
        return playlist_tracks
    else:
        position_of_index_b4 = 0
        for d in playlist_tracks:
            if d['track_id'] == track_id:
                break
            else:
                position_of_index_b4 +=1
        track = playlist_tracks.pop(position_of_index_b4)
        playlist_tracks.insert(position,track)
        index = 1
        for d in playlist_tracks:
            d['position'] = index
            index+=1
        return playlist_tracks