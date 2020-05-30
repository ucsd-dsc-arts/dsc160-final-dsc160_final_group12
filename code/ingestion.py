""" Image Ingestion

ingestion.py allows users to upload an image of 
their choice

"""

# Importing scripts
import pandas as pd
import numpy as np
import panel as pn
pn.extension()

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
            global filepath
            filepath = 'data/temp/'+file_input.filename
            file_input.save(filepath)
        
        return file_input
    
    return pn.Row(check_input)
