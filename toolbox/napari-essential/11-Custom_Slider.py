"""
Selecting a binary threshold dynamically with a slider.

More info:
https://napari.org/guides/magicgui.html
"""
import napari
from napari.types import ImageData, LabelsData
from magicgui import magicgui
from skimage import img_as_float, data
from skimage.exposure import rescale_intensity


@magicgui(
    auto_call=True,
    threshold={"widget_type": "FloatSlider", "max": 1},
    layout='horizontal'
)
def binary_thresold(layer: ImageData, threshold: float=0.5) -> LabelsData:
    """Applies a binary threshold to the image."""
    if layer is not None:
        layer = rescale_intensity(layer, out_range=(0, 1))
        return (layer > threshold).astype('int')


viewer = napari.Viewer(title="Binary threshold selection with a slider")

image = img_as_float(data.coins()[50:-50, 50:-50])

viewer.add_image(image, name="coins")

viewer.window.add_dock_widget(binary_thresold, area='bottom')


if __name__ == '__main__':
    napari.run()
