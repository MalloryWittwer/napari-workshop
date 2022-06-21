"""
Demo: segmentation based on thresholding and connected components labeling.
"""
import numpy as np
from skimage import data
from skimage.filters import threshold_otsu
from skimage.segmentation import clear_border
from skimage.measure import label, regionprops
from skimage.morphology import remove_small_objects
from scipy.ndimage.morphology import binary_fill_holes
import napari

# Example image
image = data.coins()[50:-50, 50:-50]

# Napari viewer
viewer = napari.Viewer(title="Watershed segmentation")

viewer.add_image(image, name='image', rgb=False)

# Global threshold
thresh = threshold_otsu(image)
binary_image = image > thresh

# Morphological operations
binary_image = binary_fill_holes(binary_image)
binary_image = clear_border(binary_image)
binary_image = remove_small_objects(binary_image, min_size=20)

# Connected components labeling
label_image = label(binary_image)

viewer.add_labels(label_image, name='segmentation')

# Add bounding boxes
rectangles = []
for region in regionprops(label_image):
    min_x, min_y, max_x, max_y = region.bbox
    rectangles.append([[min_x, min_y], [max_x, max_y]])

# Compute areas
label_areas = np.bincount(label_image.ravel())[1:]

viewer.add_shapes(
    data=rectangles,
    features={'area': label_areas},
    name='bounding boxes',
    shape_type='rectangle',
    edge_width=1,
    edge_color='white',
    face_color='transparent',
    opacity=0.7,
    text = {
        'string': 'Area: {area} px',
        'size': 12,
        'color': 'white',
        'translation': np.array([-30, 0]),
    }
)

if __name__ == '__main__':
    napari.run()
