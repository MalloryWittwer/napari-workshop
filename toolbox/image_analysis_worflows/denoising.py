"""
Demo: comparison of denoising methods for image restoration.

More info:
https://scikit-image.org/docs/stable/api/skimage.restoration.html
"""

from skimage.restoration import (
    denoise_tv_chambolle,
    denoise_bilateral,
    denoise_wavelet,
    denoise_nl_means,
)
from skimage.filters import median, gaussian
from skimage import data, img_as_float
from skimage.util import random_noise
import napari

# Load example data and add random noise to it
# original = img_as_float(data.chelsea()[100:250, 50:300])
original = img_as_float(data.coins())
sigma = 0.155
noisy = random_noise(original, var=sigma**2)

viewer = napari.Viewer(title="Denoising an image")

# Median filter
viewer.add_image(median(noisy), name="Median filter")

# Gaussian filter
viewer.add_image(gaussian(noisy, sigma=1), name="Gaussian filter")

# Total variation denoising
viewer.add_image(denoise_tv_chambolle(noisy, weight=0.1), name='Total variation')

# Bilateral filter
viewer.add_image(denoise_bilateral(noisy, sigma_spatial=1), name='Bilateral filter')

# Wavelet denoising
viewer.add_image(denoise_wavelet(noisy, rescale_sigma=True), name='Wavelet')

# Non-local means
viewer.add_image(denoise_nl_means(noisy), name='Non-local means')

# Original image
viewer.add_image(original, name="Original")

# Noisy image
viewer.add_image(noisy, name="Noisy image")

viewer.grid.enabled = True

if __name__ == '__main__':
    napari.run()
