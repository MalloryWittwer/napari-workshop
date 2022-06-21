"""
Adding a Tracks layer to the Napari viewer.

More info:
https://napari.org/howtos/layers/tracks.html
"""

import napari
import numpy as np

def create_tracks_data(n_tracks=100):

    def lissajous(t):
        a = np.random.random(size=(3,)) * 80.0 - 40.0
        b = np.random.random(size=(3,)) * 0.05
        c = np.random.random(size=(3,)) * 0.1
        return (a[i] * np.cos(b[i] * t + c[i]) for i in range(3))

    tracks = []
    for track_id in range(n_tracks):
        track = np.zeros((200, 10), dtype=np.float32)
        timestamps = np.arange(track.shape[0])
        x, y, z = lissajous(timestamps)
        track[:, 0] = track_id
        track[:, 1] = timestamps
        track[:, 2] = 50.0 + z
        track[:, 3] = 50.0 + y
        track[:, 4] = 50.0 + x
        tracks.append(track)

    tracks = np.concatenate(tracks, axis=0)
    tracks = tracks[:, :5]  # just the coordinate data

    return tracks

# Get some data:
tracks = create_tracks_data()

# Instantiate the viewre
viewer = napari.Viewer(ndisplay=3)

# Add the tracks layer
viewer.add_tracks(tracks)

if __name__ == '__main__':
    napari.run()
