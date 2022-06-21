"""
Demo: using a Shapes layer to dynamically adjust exposure of an image.
"""

import numpy as np
from skimage.exposure import rescale_intensity
from skimage import data, img_as_float
import napari

viewer = napari.Viewer(title='Local histogram equalization')

image = img_as_float(data.coins()[50:-50, 50:-50])
rx, ry = image.shape

viewer.add_image(image)
viewer.add_image(np.zeros((1, 1), dtype='float'), name='preview')

viewer.add_shapes(
    data=[[100, 100], [120, 120]],
    name='window',
    shape_type='rectangle',
    edge_width=1,
    edge_color='red',
    face_color='transparent',
    opacity=0.7,
)

viewer.layers['window'].mode = 'SELECT'

def adjust_histogram():
    bbox = np.squeeze(np.array(viewer.layers['window'].data))
    x_lims, y_lims = bbox.T
    min_x, max_x = int(np.min(x_lims)), int(np.max(x_lims))
    min_y, max_y = int(np.min(y_lims)), int(np.max(y_lims))

    cropped_image = image[min_x:max_x, min_y:max_y]

    min_value = np.quantile(cropped_image, 0.1)
    max_value = np.quantile(cropped_image, 0.9)

    rescaled_image = rescale_intensity(image, in_range=(min_value, max_value))

    viewer.layers['image'].data = rescaled_image

viewer.layers['window'].events.set_data.connect(adjust_histogram)

if __name__ == '__main__':
    adjust_histogram()
    napari.run()
