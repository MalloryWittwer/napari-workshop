"""
Demo: using the Hough transform to detect circular shapes in an image.

More info:
https://scikit-image.org/docs/stable/auto_examples/edges/plot_circular_elliptical_hough_transform.html
"""
import numpy as np
from skimage.transform import hough_circle, hough_circle_peaks
from skimage.feature import canny
from skimage.util import img_as_ubyte
import skimage.data
import napari

# Example image
image = img_as_ubyte(skimage.data.coins()[50:-50, 50:-50])

# Napari viewer
viewer = napari.Viewer(title='Circles detection')

viewer.add_image(image, name='image')

# Canny edge detection
edges = canny(image, sigma=3, low_threshold=10, high_threshold=50)

# Hough circles detection
hough_radii = np.arange(20, 35, 2)
hough_res = hough_circle(edges, hough_radii)

# Select the most prominent circles
accums, cx, cy, radii = hough_circle_peaks(hough_res, hough_radii, total_num_peaks=4)

# Add circles to a Shapes layer
full_data = []
for center_x, center_y, radius in zip(cx, cy, radii):
    full_data.append([[center_y, center_x], [radius, radius]])

viewer.add_shapes(
    data=full_data,
    name='detected circles',
    features=None,
    properties=None,
    shape_type='ellipse',
    edge_width=1,
    edge_color='red',
    face_color='#ff000000',
)

# Convert shapes to labels => set up the viewer
label_image = viewer.layers['detected circles'].to_labels(image.shape)
label_areas = np.bincount(label_image.ravel())[1:]

size_range = np.max(label_areas) - np.min(label_areas)
cols = (label_areas - np.min(label_areas)) / size_range

viewer.layers['detected circles'].features = {'area': label_areas, 'col': cols}
viewer.layers['detected circles'].text = {
    'string': 'Area: {area} px',
    'size': 12,
    'color': 'white',
    'translation': np.array([-30, 0]),
}

viewer.layers['detected circles'].edge_color = 'col'
viewer.layers['detected circles'].face_color = 'col'
viewer.layers['detected circles'].opacity = 0.3

if __name__ == '__main__':
    napari.run()
