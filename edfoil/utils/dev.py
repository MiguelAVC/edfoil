'''
Development utilities for the EdFoil project.
'''

import sys
import os

def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller.
    
    :param relative_path: Relative path to the resource.
    :type relative_path: str
    
    :returns: Absolute path to the resource.
    :rtype: str
    """
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)