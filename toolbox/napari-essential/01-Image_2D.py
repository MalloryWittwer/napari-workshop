"""
Loading a 2D image into the napari Viewer.
"""
import napari
import skimage.data as data

# Example image
image = data.hubble_deep_field()

# Instantiate a Viewer object
viewer = napari.Viewer(title="Add a 2D image")

# Adding a name to the image is optional
viewer.add_image(image, name="Hubble Deep Field")

if __name__ == '__main__':
    napari.run()
