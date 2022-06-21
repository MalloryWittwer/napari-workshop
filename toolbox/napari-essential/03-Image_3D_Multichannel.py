"""
Loading a 3D multichannel image into the Napari viewer.
"""
import napari
from skimage import data

# Example 3D multichannel image (shape=(60, 2, 256, 256) ZCXY)
image = data.cells3d()

# Instanciate the viewer
viewer = napari.Viewer(title="Add a 3D+time multichannel image", ndisplay=3)

# Think about specifying the channel axis
viewer.add_image(image, channel_axis=1)

if __name__ == '__main__':
    napari.run()
