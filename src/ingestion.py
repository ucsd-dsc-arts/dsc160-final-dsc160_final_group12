""" Image Ingestion

ingestion.py allows users to generate and upload an 
image of their choice

"""

# Importing scripts
import pandas as pd
import numpy as np
from skimage import io
from skimage.transform import resize
import panel as pn
pn.extension()

import holoviews as hv
from holoviews import opts
from holoviews import streams
hv.extension('bokeh')



def draw():
    """
    Allows users to draw and download an image
    of their choice
    
    :returns: Widget to draw
    """
    
    # Creating widget
    path = hv.Path([])
    freehand = streams.FreehandDraw(source=path, num_objects=100,
                                    styles={'line_color': ['black']})
    
    # Customizing
    path.opts(
    opts.Path(active_tools=['freehand_draw'], height=219, 
              line_width=20, width=519, xaxis=None, yaxis=None))
    
    return path

    

filepath = ''
def input_data():
    """
    Allows users to upload an image of their 
    choice
    
    :returns: panel widget to input file
    """
    
    file_input = pn.widgets.FileInput()
    
    @pn.depends(file_input.param.filename)
    def check_input(file):
        """
        Checks if input file has been passed in.
        If so, saves data into directory
        """
        
        if pd.isnull(file_input.filename):
            return file_input
        
        else:
            #Saving and converting image
            global filepath
            filepath = '../data/text_image.png'
            file_input.save(filepath)
            image = io.imread(filepath)
            resized_image = resize(image, (73, 173))
            io.imsave(fname=filepath, arr=resized_image)
        
        return file_input
    
    return pn.Row(check_input)
