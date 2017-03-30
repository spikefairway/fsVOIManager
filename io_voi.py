#!/usr/bin/env python
# coding: utf-8

__author__ = 'keisu-ma'

import os
import re
import nibabel as nib
import numpy as np
import pandas as pd

import utils as utils

"""
IO module for VOI definition file.

VOI definition file is a csv file which has look-up table between FreeSurfer and user-defined VOIs.

Table format is the followings:

    |FS VOI No.|FS VOI name|user VOI name|user VOI No.|
"""

def loadFSLUT():
    """
    Load FreeSurfer look-up table.
    """
    fs_home = os.environ["FREESURFER_HOME"]
    fs_lut_file = os.path.join(fs_home,
                               "FreeSurferColorLUT.txt")
    fs_lut = pd.read_csv(fs_lut_file, comment="#",
                         delim_whitespace=True,
                         names=["FS VOI No.", "FS VOI name",
                                "R", "G", "B", "A"])

    return fs_lut

def save_userLUT(voidef, out_lut_file):
    """
    Save look-up table for user-defined VOI.

    Format for outputted table:
        |user VOI No.|user VOI name|

    """
    df = voidef[["user VOI No.", "user VOI name"]]
    df2 = df.drop_duplicates(["user VOI name"])

    df2.to_csv(out_lut_file, index=False, sep=" ", header=False)

    return None
