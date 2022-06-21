"""
Demo: using a global vs a local threshold on an image.

More info:
https://scikit-image.org/docs/stable/auto_examples/applications/plot_thresholding.html
"""

from skimage import data
from skimage.filters import threshold_otsu, threshold_local
import napari

# Load example data
image = data.page()

# Otsu's global threshold
global_thresh = threshold_otsu(image)
binary_global = image > global_thresh

# Local threshold
block_size = 35
local_thresh = threshold_local(image, block_size, offset=10)
binary_local = image > local_thresh

# Visualization in Napari
viewer = napari.Viewer(title="Image thresholding")

viewer.add_image(image, name="Original")
viewer.add_image(binary_global, name="Global thresholding")
viewer.add_image(binary_local, name="Local thresholding")

viewer.grid.enabled = True


### Optional - slider to interactively set the block size of the local threshold.

# from magicgui import magicgui
# from napari.types import ImageData, LabelsData

# @magicgui(
#     auto_call=True,
#     block_size={"widget_type": "IntSlider", "max": 50},
#     layout='horizontal'
# )
# def local_threshold(layer: ImageData, block_size: int=15) -> LabelsData:
#     """Apply a local threshold. Note: the block size must be odd."""
#     if layer is not None:
#         return layer > threshold_local(image, block_size*2 + 1, offset=10)


# viewer.window.add_dock_widget(local_threshold, area='bottom')


if __name__ == '__main__':
    napari.run()
