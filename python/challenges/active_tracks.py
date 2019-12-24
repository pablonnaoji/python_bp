"""
Given a list of track data, return the IDs of active tracks.
The list may contain duplicate tracks.

    [
        {
            'id': 1,
            'name': 'In Arms',
            'active': True,
        },
        {
            'id': 2,
            'name': 'Deep Dip',
            'active': False,
        },
        {
            'id': 3,
            'name': 'Panic Room',
            'active': True,
        },
        {
            'id': 1,
            'name': 'In Arms',
            'active': True,
        },
    ]  # should return [1, 3]

"""

def active_tracks(tracks):
    active = set()
    for track in tracks:
        if track['active'] == True:
            active.add(track['id'])
        else:
            pass
    return active
    