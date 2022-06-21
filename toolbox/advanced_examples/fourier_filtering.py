"""
Demo: using a Napari Shapes layer to control Fourier filtering interactively.
"""

import numpy as np
import skimage.data
import napari
from scipy.fft import fft2, fftshift, ifft2, ifftshift
from skimage import img_as_float
from skimage.color import rgb2gray


viewer = napari.Viewer(title='Playing with Fourier')

image = img_as_float(rgb2gray(skimage.data.astronaut()))
rx, ry = image.shape

from skimage.exposure import rescale_intensity
from skimage.transform import resize

artefacts = np.mean(skimage.io.imread('/home/mallory/Desktop/artificial.png'), -1)
artefacts = rescale_intensity(artefacts, out_range=(0, 1))
artefacts = resize(artefacts, output_shape=image.shape)
image = rescale_intensity(artefacts + image, out_range=(0, 1))

viewer.add_image(image, name='image', visible=False)

fourier_img = fftshift(fft2(image))

viewer.add_image(np.log(fourier_img.real), name='fft', visible=False)

viewer.add_image(np.zeros((1, 1), dtype='float'), name='restored', blending='additive')

viewer.add_shapes(
    data=[[rx // 2, ry // 2], [30, 30]],
    name='ellipse',
    shape_type='ellipse',
    edge_width=1,
    edge_color='red',
    face_color='#ff000033',
    opacity=0.7,
    blending='additive'
)

def update_fourier():
    labs = viewer.layers['ellipse'].to_labels(image.shape)
    fourier_img_cropped = fourier_img.copy()
    fourier_img_cropped[labs != 0] = 0
    # fourier_img_cropped[labs == 0] = 0
    restored = ifft2(ifftshift(fourier_img_cropped))
    restored = rescale_intensity(restored.real, out_range=(0, 1))
    # print('exposure: ', restored.max(), restored.min())
    viewer.layers['restored'].data = restored

viewer.layers['ellipse'].events.set_data.connect(update_fourier)

viewer.layers['ellipse'].mode = 'SELECT'

if __name__ == '__main__':
    update_fourier()
    napari.run()
