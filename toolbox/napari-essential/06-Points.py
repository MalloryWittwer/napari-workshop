"""
Add points with text
====================

Display a points layer on top of an image layer using the add_points and
add_image APIs
"""

data.

import numpy as np
import napari
import skimage.data as data

image = data.human_mitosis()

viewer = napari.Viewer()

viewer.add_image(image)

# viewer.add_image(np.zeros((400, 400)))

points = np.array([[100, 100], [200, 300], [333, 111]])

features = {
    'confidence': np.array([1, 0.5, 0]),
    'good_point': np.array([True, False, False]),
}

text = {
    'string': 'Confidence is {confidence:.2f}',
    'size': 20,
    'color': 'green',
    'translation': np.array([-30, 0]),
}

points_layer = viewer.add_points(
    points,
    features=features,
    text=text,
    size=20,
    edge_width=7,
    edge_width_is_relative=False,
    edge_color='confidence',
    edge_colormap='gray',
    face_color='good_point',
    face_color_cycle=['blue', 'green'],
)

points_layer.edge_color_mode = 'colormap'

if __name__ == '__main__':
    napari.run()
