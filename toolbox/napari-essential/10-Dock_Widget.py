"""
Using magicgui to create a custom dock widget.

More info:
https://napari.org/guides/magicgui.html
"""
import napari
from magicgui import magicgui
from napari.utils.notifications import show_info

viewer = napari.Viewer()

@magicgui(call_button="Say hello")
def say_hello():
    show_info('Hello!')  # Shows a pop-up notification in the viewer

# Attach the dock widget to the viewer
viewer.window.add_dock_widget(say_hello, area='right', name='Hello')

if __name__ == '__main__':
    napari.run()
