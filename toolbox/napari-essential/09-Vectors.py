"""
Adding a Vector layer to the napari viewer.

More info on Vector layers:
https://github.com/napari/napari/blob/main/examples/add_vectors_image.py

More info on optical flow:
https://scikit-image.org/docs/stable/auto_examples/registration/plot_opticalflow.html#sphx-glr-auto-examples-registration-plot-opticalflow-py
"""

import numpy as np
from skimage import data
from skimage.registration import optical_flow_ilk
import napari

image0, image1 = data.vortex()
nl, nc = image0.shape

viewer = napari.Viewer()

viewer.add_image(image0)
viewer.add_image(image1)

# Optical flow estimator
v, u = optical_flow_ilk(image0, image1, radius=15)

# Flow magnitude
norm = np.sqrt(u ** 2 + v ** 2)

viewer.add_image(norm, opacity=0.5, colormap='cyan', name='flow magnitude')

def create_vector_data(u, v, nvec=20):
    """
    A set of N vectors should be represented as an array of shape (N, 2, D) with
    the second axis representing the X and Y coordinates of the starting point
    of the vector, D its dimensionality.
    """
    step = max(nl//nvec, nc//nvec)
    y, x = np.mgrid[:nl:step, :nc:step]
    u_ = u[::step, ::step]
    v_ = v[::step, ::step]

    vector_data = []
    for a, b, c, d in zip(x.ravel(), y.ravel(), u_.ravel(), v_.ravel()):
        v = np.array([[b, a], [d, c]])
        vector_data.append(v)
    vector_data = np.array(vector_data)

    return vector_data

# Get vector data from the optical flow
vector_data = create_vector_data(u, v)

# Add a vectors layer
viewer.add_vectors(vector_data, name='vector field',
    edge_width=2, length=4, edge_color='magenta'
)

if __name__ == '__main__':
    napari.run()
