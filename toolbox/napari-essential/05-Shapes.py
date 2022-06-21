"""
TODO: use regionpropse to draw bounding boxes around labels and text their area
"""
import numpy as np
from skimage import data
import napari

# data.

viewer = napari.view_image(data.camera(), name='photographer')

polygons = [
    np.array([[225, 146], [283, 146], [283, 211], [225, 211]]),
    np.array([[67, 182], [167, 182], [167, 268], [67, 268]]),
    np.array([[111, 336], [220, 336], [220, 240], [111, 240]]),
]

features = {
    'likelihood': [21.23423, 51.2315, 100],
    'class': ['hand', 'face', 'camera'],
}
edge_color_cycle = ['blue', 'magenta', 'green']

text = {
    'string': '{class}: {likelihood:0.1f}%',
    'anchor': 'upper_left',
    'translation': [-5, 0],
    'size': 8,
    'color': 'green',
}

shapes_layer = viewer.add_shapes(
    polygons,
    features=features,
    shape_type='polygon',
    edge_width=3,
    edge_color='class',
    edge_color_cycle=edge_color_cycle,
    face_color='transparent',
    text=text,
    name='shapes',
)

if __name__ == '__main__':
    napari.run()
