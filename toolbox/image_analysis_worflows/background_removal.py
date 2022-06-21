from skimage.io import imread
from skimage.filters import gaussian
from skimage.restoration import rolling_ball
from skimage.morphology import disk
from skimage.filters import difference_of_gaussians
from skimage.morphology import white_tophat
import napari

# Example image
image = imread('napari-workshop/example_data/zfish_eye.tif')[:, :, 0]

viewer = napari.Viewer(title="Background subtraction")

viewer.add_image(image, name="original")

# Rolling ball method
background_rolling = rolling_ball(image, radius=25)
img_rolling = image - background_rolling

viewer.add_image(img_rolling, name="rolling ball")

# Gaussian method (background subtraction)
background_gaussian = gaussian(image, sigma=20, preserve_range=True)
img_gaussian = image - background_gaussian

viewer.add_image(img_gaussian, name="gaussian subtraction")

# Gaussian method (background division)
background_gaussian = gaussian(image, sigma=50, preserve_range=True)
img_gaussian_divide = image / background_gaussian

viewer.add_image(img_gaussian_divide, name="gaussian division")

# Difference of Gaussians
img_dog = difference_of_gaussians(image, 0, 15)

viewer.add_image(img_dog, name="difference of gaussians")

# Top-Hat filter
img_top_hat = white_tophat(image, disk(15))

viewer.add_image(img_top_hat, name="Top-Hat")

viewer.grid.enabled = True

if __name__ == '__main__':
    napari.run()
