# """
# Demo: nuclei segmentation with Cellpose.

# More info:
# - ...
# """

# from skimage import data, img_as_float
# from cellpose import models  # Install: pip install cellpose
# import napari

# image = img_as_float(data.human_mitosis())

# viewer = napari.Viewer(title='Nuclei segmentation with CellPose')

# viewer.add_image(image)

# model = models.Cellpose(gpu=False, model_type='nuclei')

# masks, flows, styles, diams = model.eval(image, diameter=None, channels=[0, 0])

# viewer.add_labels(masks, name='segmentation')

# if __name__ == '__main__':
#     napari.run()
