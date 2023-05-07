{
    'id': 'Spotify ID of the track',
    'name': 'Name of the track',
    'artists': [
        {
            'id': 'Spotify ID of the artist',
            'name': 'Name of the artist'
        },
        # Additional artists can be included here
    ],
    'album': {
        'id': 'Spotify ID of the album',
        'name': 'Name of the album',
        'images': [
            {
                'url': 'URL of the album cover image',
                'width': 'Width of the album cover image in pixels',
                'height': 'Height of the album cover image in pixels'
            },
            # Additional images can be included here
        ]
    },
    'preview_url': 'URL of a 30-second preview of the track',
    'duration_ms': 'Duration of the track in milliseconds',
    'popularity': 'Popularity of the track on Spotify (0-100)',
    'uri': 'Spotify URI of the track'
}

tracks = [
    {
        'id': '6rqhFgbbKwnb9MLmUQDhG6',
        'name': 'Somebody That I Used To Know',
        'artists': [
            {
                'id': '7DgJa5wu4oGMSkM9t0ils7',
                'name': 'Gotye'
            },
            {
                'id': '3nFkdlSjzX9mRTtwJOzDYB',
                'name': 'Kimbra'
            }
        ],
        'album': {
            'id': '3qPBlKmKlvNMXxUUqeDgS1',
            'name': 'Making Mirrors',
            'images': [
                {
                    'url': 'https://i.scdn.co/image/ab67616d0000b273b02e8da6e9ca9b1de6f28426',
                    'width': 640,
                    'height': 640
                }
            ]
        },
        'preview_url': 'https://p.scdn.co/mp3-preview/325e20e00b37de1c36d7b9379cfa3aa7bae47ce8?cid=774b29d4f13844c495f206cafdad9c86',
        'duration_ms': 244973,
        'popularity': 82,
        'uri': 'spotify:track:6rqhFgbbKwnb9MLmUQDhG6'
    },
    # Additional tracks can be included here
]

# Save the tracks to a file
import json
with open('tracks.json', 'w') as f:
    json.dump(tracks, f)
