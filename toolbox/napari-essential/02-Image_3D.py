"""
Loading a 3D image into the Napari viewer.
"""
import napari
from skimage import data

# Example data
image = data.binary_blobs(length=128, volume_fraction=0.1, n_dim=3)

# Adding ndisplay=3 will launch the viewer in 3D mode directly.
viewer = napari.Viewer(title="Add a 3D image", ndisplay=3)

viewer.add_image(image)

if __name__ == '__main__':
    napari.run()
