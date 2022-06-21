"""
Adding a Labels layer to the Napari viewer.

More info:
https://napari.org/howtos/layers/labels.html
"""
import napari
from skimage.morphology import label
from skimage import data

viewer = napari.Viewer(title="Labels image", ndisplay=3)

# Example image with labels
image = data.binary_blobs(length=128, volume_fraction=0.1, n_dim=3)
labeled_image = label(image)  # Connected components labeling

# Add the image
viewer.add_image(image, name='image')

# Add the labels
viewer.add_labels(labeled_image, name='labels')

if __name__ == '__main__':
    napari.run()
