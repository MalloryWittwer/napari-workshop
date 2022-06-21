"""
Demo: using the SLIC algorithm and hierarchical merging of pixels to segment an image.

More info:
https://scikit-image.org/docs/dev/api/skimage.segmentation.html
"""

from skimage import data, segmentation, color
from skimage.future import graph
import numpy as np
import napari


def weight_mean_color(graph, src, dst, n):
    diff = graph.nodes[dst]['mean color'] - graph.nodes[n]['mean color']
    diff = np.linalg.norm(diff)
    return {'weight': diff}


def merge_mean_color(graph, src, dst):
    graph.nodes[dst]['total color'] += graph.nodes[src]['total color']
    graph.nodes[dst]['pixel count'] += graph.nodes[src]['pixel count']
    graph.nodes[dst]['mean color'] = (graph.nodes[dst]['total color'] /
                                      graph.nodes[dst]['pixel count'])

# Example image
image = data.coffee()

# Napari viewer
viewer = napari.Viewer(title="SLIC superpixels and hierarchical merging")

viewer.add_image(image, name='image', rgb=True)

# SLIC algorithm
slic_labels = segmentation.slic(image, compactness=30, n_segments=400, start_label=1)

# For visualization: colorize SLIC regions based on RGB mean
slic_image = color.label2rgb(slic_labels, image, kind='avg', bg_label=0)
slic_image = segmentation.mark_boundaries(slic_image, slic_labels, (0, 0, 0))

viewer.add_image(slic_image, name='SLIC superpixels')

# Region adjacency graph
g = graph.rag_mean_color(image, slic_labels)

merged_labels = graph.merge_hierarchical(slic_labels, g, thresh=35,
                                rag_copy=False,
                                in_place_merge=True,
                                merge_func=merge_mean_color,
                                weight_func=weight_mean_color)

merged_image = color.label2rgb(merged_labels, image, kind='avg', bg_label=0)
merged_image = segmentation.mark_boundaries(merged_image, merged_labels, (0, 0, 0))

viewer.add_image(merged_image, name='Hierarchical Merging', rgb=True)

viewer.grid.enabled = True

if __name__ == '__main__':
    napari.run()
