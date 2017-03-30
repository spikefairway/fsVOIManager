#!/usr/bin/env python
# coding: utf-8

"""
Utilities.
"""

import numpy as np
import nibabel as nib
import re
import wx
import os

def loadImage(f):
    """ Load NIfTI image.
    """
    img = nib.load(f)
    mat = img.get_data()
    aff = img.get_affine()

    return mat, aff, img

def array2NIfTI(imgMat, imgAffine, outFile, **kwargs):
    img = nib.Nifti1Image(imgMat, imgAffine, **kwargs)
    img.to_filename(outFile)

    return img

def array2NIfTIAsDType(imgMat, imgAffine, outFile, dtype=np.int16, **kwargs):
    hdr = nib.Nifti1Header()
    hdr.set_data_dtype(dtype)
    img = array2NIfTI(imgMat, imgAffine, outFile, header=hdr, **kwargs)

    return img

def ShowOpenDialog(frame, curdir, wildcard="*.*",
                   mes="Select a file to open."):
    """
    Module for show the open dialog.
    """
    dlg = wx.FileDialog(frame, mes, curdir, "",
                        wildcard, wx.FD_OPEN)
    res = dlg.ShowModal()
    if res == wx.ID_OK:
        fname = dlg.GetFilename()
        dirname = dlg.GetDirectory()
        curdir = dirname
        open_fname = os.path.join(dirname, fname)
    elif res == wx.ID_CANCEL:
        return None
    else:
        pass
    dlg.Destroy()

    return open_fname

def ShowOpenDialogMul(frame, curdir, wildcard="*.*",
                      mes="Select files to open."):
    """
    Module for show the open dialog for multiple files.
    """
    dlg = wx.FileDialog(frame, mes, curdir, "",
                        wildcard, wx.FD_OPEN|wx.FD_MULTIPLE)
    res = dlg.ShowModal()
    if res == wx.ID_OK:
        flist = dlg.GetPaths()
        dirname = dlg.GetDirectory()
        curdir = dirname
    elif res == wx.ID_CANCEL:
        return None
    else:
        pass
    dlg.Destroy()

    return flist

def ShowSaveDialog(frame, curdir, wildcard="*.*",
                   mes="Select a file to save"):
    """
    Module to show the save dialog.
    """
    sav_dlg = wx.FileDialog(frame, mes, curdir, "",
                            wildcard=wildcard,
                            style=wx.FD_SAVE|wx.FD_OVERWRITE_PROMPT)
    res = sav_dlg.ShowModal()
    if res == wx.ID_OK:
        fname = sav_dlg.GetFilename()
        dirname = sav_dlg.GetDirectory()
        curdir = dirname
        save_fname = os.path.join(dirname, fname)
    elif res == wx.ID_CANCEL:
        return None
    else:
        pass
    sav_dlg.Destroy()

    return save_fname

def addPrefix(fPath, prefix):
    """
    Add prefix to file.
    """
    fDir, fBase = os.path.split(fPath)
    ret = os.path.join(fDir,
                       "".join([prefix, fBase]))

    return ret

def addPostfix(fPath, postfix):
    """
    Add postfix to file.
    """
    fDir, fBase = os.path.split(fPath)
    fBase2, fExt = os.path.splitext(fBase)

    ret = os.path.join(fDir,
                       "".join([fBase2, postfix, fExt]))

    return ret
