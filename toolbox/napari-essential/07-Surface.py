"""
Adding a (3D mesh) Surface layer to the Napari viewer.

More info:
https://napari.org/howtos/layers/surface.html
"""
import napari
from vispy.io import read_mesh, load_data_file

# Currently, you can load .obj and .obj.gz formats
vert, faces, _, _ = read_mesh(load_data_file('orig/triceratops.obj.gz'))

# Correct mesh orientation, scale it up, and fix facet normals
vert *= -100
faces = faces[:, ::-1]

viewer = napari.Viewer(ndisplay=3)

# Add the surface mesh
surface = viewer.add_surface(data=(vert, faces), name="Triceratops")

if __name__ == '__main__':
    napari.run()
