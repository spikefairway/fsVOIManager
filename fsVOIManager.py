#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import wx
import numpy as np
import nibabel as nib
import pandas as pd
import six

from fsVOIManagerGUI import fsVOIManagerMain
import utils as utils
import io_voi as io_voi

"""
VOI definition file is a csv file which has look-up table between FreeSurfer and user-defined VOIs.

Table format is the followings:

    |FS VOI No.|FS VOI name|user VOI name|user VOI No.|
"""

def gen_merged_mask(fs_voi_mat, voi_no_list):
    """
    Return mask for merged VOI.
    """
    out = np.zeros_like(fs_voi_mat, dtype=np.bool)
    for vno in voi_no_list:
        out += fs_voi_mat == vno

    return out

def mergeFSVOI(in_file, out_file, voidef):
    """
    Merge Freesurfer VOI on NIfTI image.
    :param in_file: Input NIfTI file. (e.g., aparc+aseg.nii)
    :param out_file: Output NIfTI file. 
    :param voidef: VOI definition table.
    :return:
    """
    # Load image
    in_mat, in_aff = utils.loadImage(in_file)[:2]

    # Load VOI definition
    u_voidef = voidef[["user VOI No.", "user VOI name"]].drop_duplicates(["user VOI name"])

    # Merge VOIs
    out_mat = np.zeros_like(in_mat)
    for u_voi_no, u_voi in zip(u_voidef["user VOI No."], u_voidef["user VOI name"]):
        fs_voi_list = voidef.loc[voidef["user VOI name"] == u_voi, "FS VOI No."].values
        mask = gen_merged_mask(in_mat, fs_voi_list)
        out_mat[mask] = u_voi_no

    # Save VOI map
    utils.array2NIfTI(out_mat, in_aff, out_file)

    # Save LUT for user-defined VOI
    out_lut_file = utils.addPrefix(out_file, "lut_")
    io_voi.save_userLUT(voidef, out_lut_file)

    return out_mat

class fsVOIManager(fsVOIManagerMain):
    """
    GUI to manage VOI set from freesurfer.
    """

    def __init__(self, parent):
        super(fsVOIManager, self).__init__(parent)

        # Load FS VOI definition
        self.fs_lut = io_voi.loadFSLUT()

        # Initialize FS VOI list
        self.initializeFSVOIList()

    def initializeFSVOIList(self):
        # Set list
        defVOIList = self.fs_lut["FS VOI name"].values.tolist()
        self.defVOIListBox.SetItems(defVOIList)

        # Initialize
        self.voiset_table = pd.DataFrame({"FS VOI name" : [],
            "user VOI name" : []})
        self.voiset_list = []
        self.currentNIfTIFile = None
        self.updateFSVOIList(defVOIList)

    def loadExtractedVOIFileButtonOnButtonClick( self, event ):
        """
        Callback for load extracted VOI button.
        :param event
        :return:
        """
        # Load file
        iFile = utils.ShowOpenDialog(self, os.curdir, wildcard="*.nii")

        if iFile is not None:
            # Load image
            voi_mat = utils.loadImage(iFile)[0]

            # Value distribution
            fs_voi_nos = np.sort(np.unique(voi_mat))

            # Construct VOI list
            df = self.fs_lut.loc[self.fs_lut["FS VOI No."].isin(fs_voi_nos), :]
            voi_list = df["FS VOI name"].values.tolist()

            # Omit currently selected VOIs
            [voi_list.pop(voi_list.index(v))
                    for v in self.voiset_table["FS VOI name"].values]

            # Update VOI list
            self.currentNIfTIFile = iFile
            self.updateFSVOIList(voi_list)

    def loadDefaultButtonOnButtonClick( self, event ):
        """
        Callback for load default
        :param event:
        :return:
        """
        # Initialize
        self.initializeFSVOIList()

    def addButtonOnButtonClick( self, event ):
        """
        Callback for add button.
        Override.
        :param event:
        :return:
        """
        # Get selections
        selectedVOI = self.getSelectedVOIs()
        if selectedVOI is None:
            dlg = wx.MessageDialog(self, "Please select at least one VOI in 'Extracted VOI list'!", "Warning", style=wx.OK|wx.ICON_WARNING)
            dlg.ShowModal()
            dlg.Destroy()
        else:
            # Append VOI definition
            df = pd.DataFrame({"FS VOI name" : selectedVOI,
                               "user VOI name" : selectedVOI})
            self.voiset_table = self.voiset_table.append(df, ignore_index=True)
            self.voiset_list.extend(selectedVOI)

            # Pop out FS VOIs
            self.popFSVOI(selectedVOI)

            # Update
            self.updateListBoxes()

            # Deselection
            [self.defVOIListBox.Deselect(idx) for idx in self.defVOIListBox.GetSelections()]


    def mergeButtonOnButtonClick( self, event ):
        """
        Callback for merge button.
        Override.
        :param event:
        :return:
        """
        # Get selections
        selectedVOI = self.getSelectedVOIs()
        if selectedVOI is None:
            dlg = wx.MessageDialog(self, "Please select at least one VOI in 'Extracted VOI list'!", "Warning", style=wx.OK|wx.ICON_WARNING)
            dlg.ShowModal()
            dlg.Destroy()
        else:
            # Name
            inpVal = self.nameVOI()

            if inpVal is not None:        # Not canceled
                # Append
                df = pd.DataFrame({"FS VOI name" : selectedVOI,
                                   "user VOI name" : [inpVal] * len(selectedVOI)})
                self.voiset_table = self.voiset_table.append(df, ignore_index=True)
                self.voiset_list.append(inpVal)

                # Pop out FS VOIs
                self.popFSVOI(selectedVOI)

                # Update
                self.updateListBoxes()

            # Deselection
            [self.defVOIListBox.Deselect(idx) for idx in self.defVOIListBox.GetSelections()]


    def merge2VOIButtonOnButtonClick( self, event ):
        """
        Callback for merge to VOI button
        :param event:
        :return:
        """
        # Get selection
        iSelected = self.list4VOISet.GetSelection()
        selectedVOIFromExt = self.getSelectedVOIs()

        if selectedVOIFromExt is None:
            dlg = wx.MessageDialog(self, "Please select at least one VOI in 'Extracted VOI list'!", "Warning", style=wx.OK|wx.ICON_WARNING)
            dlg.ShowModal()
            dlg.Destroy()
        elif iSelected < 0:   # No selection
            dlg = wx.MessageDialog(self, "Please select one VOI from VOI set!", "Warning", style=wx.OK|wx.ICON_WARNING)
            dlg.ShowModal()
            dlg.Destroy()
        else:
            selectedVOI = self.voiset_list[iSelected]

            # Append
            df = pd.DataFrame({"FS VOI name" : selectedVOIFromExt,
                               "user VOI name" : [selectedVOI] * len(selectedVOIFromExt)})
            self.voiset_table = self.voiset_table.append(df, ignore_index=True)

            # Pop out FS VOIs
            self.popFSVOI(selectedVOIFromExt)

            # Maintain selection
            self.selectVOIInVOISet()



    def openVOISetButtonOnButtonClick( self, event ):
        """
        Callback for open button.
        :param event:
        :return:
        """
        # Open file
        iFile = utils.ShowOpenDialog(self, os.curdir,
                                     wildcard="*.csv",
                                     mes="Select a VOI set file.")

        if iFile is not None:
            # Load VOI set
            voiset_table = pd.read_csv(iFile).sort_values(["user VOI No.", "FS VOI No."], ascending=True)
            self.voiset_table = voiset_table[["FS VOI name", "user VOI name"]]
            user_vois = voiset_table["user VOI name"].values
            user_voi_nos = voiset_table["user VOI No."].values
            _, indices = np.unique(user_voi_nos, return_index=True)
            self.voiset_list = user_vois[indices].tolist()

            # Pop out FS VOIs
            self.popFSVOI(voiset_table["FS VOI name"].unique().tolist())

            # Update
            self.updateListBoxes()


    def genVOISet(self):
        """
        Generate VOI set with current settings.
        """
        tab = self.voiset_table.copy()

        fs_lut = pd.Series(data=self.fs_lut["FS VOI No."].values,
                           index=self.fs_lut["FS VOI name"])
        tab.loc[:, "FS VOI No."] = tab["FS VOI name"].map(fs_lut)

        nvoi = len(self.voiset_list)
        user_lut = pd.Series(data=list(range(1, nvoi + 1, 1)),
                             index=self.voiset_list)
        tab.loc[:, "user VOI No."] = tab["user VOI name"].map(user_lut)
        tab = tab[["FS VOI No.", "FS VOI name",
                   "user VOI name", "user VOI No."]]

        return tab


    def saveVOISetButtonOnButtonClick( self, event ):
        """
        Callback for save button.
        :param event:
        :return:
        """
        # Load file to save
        oFile = utils.ShowSaveDialog(self, os.curdir, wildcard="*.csv")

        # Save
        if oFile is not None:
            tab = self.genVOISet()
            tab.to_csv(oFile, index=False)

            # Save LUT file
            lut_file = utils.addPrefix(oFile, "lut_")
            io_voi.save_userLUT(tab, lut_file)

            """
            dlg = wx.MessageDialog(self, "VOIs were successfully saved to {0:s}.".format(oFile), "Message", style=wx.OK|wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()
            """

    def renameVOIButtonOnButtonClick( self, event ):
        """
        Callback to rename VOI.
        :param event:
        :return:
        """
        # Get selected
        iSelected = self.list4VOISet.GetSelection()
        selVOI = self.voiset_list[iSelected]

        # Enter name
        inpVal = self.nameVOI(selVOI)

        # Rename
        if inpVal is not None:
            # Rename on table
            lut = pd.Series(data=self.voiset_list,
                            index=self.voiset_list)
            lut[selVOI] = inpVal
            self.voiset_table.loc[:, "user VOI name"] = self.voiset_table["user VOI name"].map(lut)

            # Rename on list
            self.voiset_list[self.voiset_list.index(selVOI)] = inpVal

            # Update
            self.updateListBoxes()

    def removeVOIButtonOnButtonClick( self, event ):
        """
        Callback to remove VOI.
        :param event:
        :return:
        """
        # Get selected
        iSelected = self.list4VOISet.GetSelection()
        selVOI = self.voiset_list[iSelected]

        # Take back selected VOIs as FS VOIs
        df = self.voiset_table
        fs_vois_cur = self.currentFSVOIList
        fs_vois_back = df.loc[df["user VOI name"] == selVOI, "FS VOI name"].values.tolist()
        fs_vois_cur.extend(fs_vois_back)
        df2 = self.fs_lut.loc[self.fs_lut["FS VOI name"].isin(fs_vois_cur), :].sort_values("FS VOI No.", ascending=True)
        self.updateFSVOIList(df2["FS VOI name"].values.tolist())

        # Remove
        self.voiset_table = df.loc[df["user VOI name"] != selVOI, :]
        self.voiset_list.pop(iSelected)

        # Update
        self.updateListBoxes()


    def upVOIButtonOnButtonClick( self, event ):
        """
        Callback for up button
        :param event:
        :return:
        """
        # Get selected
        iSelected = self.list4VOISet.GetSelection()

        # Swap
        self.swapVOIList(iSelected, iSelected - 1)


    def downVOIButtonOnButtonClick( self, event ):
        """
        Callback for down button
        :param event:
        :return:
        """
        # Get selected
        iSelected = self.list4VOISet.GetSelection()

        # Swap
        self.swapVOIList(iSelected, iSelected + 1)


    def applyVOISetButtonOnButtonClick( self, event ):
        """
        Callback for apply VOI set button.
        :param event:
        :return:
        """
        if self.currentNIfTIFile is None:   # No loaded image file
            mes = "Please load extracted VOI file before applying VOI set!"
            dlg = wx.MessageDialog(self, mes, "Warning", style=wx.OK|wx.ICON_WARNING)
            dlg.ShowModal()
            dlg.Destroy()
        elif len(self.voiset_list) == 0: # No VOI set
            mes = "Please add at least one VOI to 'VOI set' list!"
            dlg = wx.MessageDialog(self, mes, "Warning", style=wx.OK|wx.ICON_WARNING)
            dlg.ShowModal()
            dlg.Destroy()
        else:
            # File to save
            oFile = utils.ShowSaveDialog(self, os.curdir, wildcard="*.nii")

            # Generate table
            tab = self.genVOISet()

            mergeFSVOI(self.currentNIfTIFile, oFile, tab)

            # Dialog
            mes = "Merged VOI file '%s' was generated." % (oFile)
            dlg = wx.MessageDialog(self, mes, "Succeeded", style=wx.OK|wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()

    def list4VOISetOnListBox( self, event ):
        """
        Callback when item in 'list4VOISet' is selected
        Override.
        :param event:
        :return:
        """
        self.selectVOIInVOISet()


    def getSelectedVOIs(self):
        """
        Get selected VOIs.
        :return:
        """
        # Get selections
        iSelect = self.defVOIListBox.GetSelections()
        if len(iSelect) != 0:
            selectedVOI = [self.currentFSVOIList[i] for i in iSelect]

            return selectedVOI
        else:
            return None


    def updateFSVOIList(self, voilist):
        """
        Update FS VOI list.
        :return:
        """
        self.currentFSVOIList = voilist
        self.defVOIListBox.SetItems(voilist)


    def updateListBoxes(self):
        """
        Update list for VOI set.
        :return:
        """
        # Set list
        self.list4VOISet.SetItems(self.voiset_list)

        # Clear contents for selected VOI
        self.m_listBox4.Clear()


    def nameVOI(self, defVal=""):
        # Name for merged VOI
        flag = True
        while flag:
            # Dialog to name
            dialog = wx.TextEntryDialog(self, "Name for merged VOI", value=defVal)
            dialog.ShowModal()

            # Get input
            inpVal = dialog.GetValue()
            dialog.Destroy()

            # Duplication check
            if (inpVal in self.voiset_list) and (inpVal != defVal):
                # Warning
                dupMes = "'%s' already exists in VOI set!\nPlease enter another name." % (inpVal)
                mesDialog = wx.MessageDialog(self, dupMes, "Warning", style=wx.OK|wx.ICON_WARNING)
                mesDialog.ShowModal()
                mesDialog.Destroy()
            else:
                flag = False

        if inpVal == defVal:        # Canceled
            return None
        else:
            return inpVal

    def swapVOIList(self, i1, i2):
        # Swap VOI list
        voiList = self.voiset_list
        voiList[i1], voiList[i2] = voiList[i2], voiList[i1]
        self.voiset_list = voiList

        # Update
        self.updateListBoxes()

        # Set selection
        self.list4VOISet.SetSelection(i2)
        self.selectVOIInVOISet()


    def selectVOIInVOISet(self):
        """
        Select VOI
        :return:
        """
        # Get selected
        iSelected = self.list4VOISet.GetSelection()
        if iSelected >= 0:
            selVOI = self.voiset_list[iSelected]

            # Get contents
            selContent = self.voiset_table.loc[self.voiset_table["user VOI name"] == selVOI, "FS VOI name"].values.tolist()

            # Set
            self.m_listBox4.SetItems(selContent)

    def popFSVOI(self, voi_list):
        """
        Pop out selected VOIs from FS VOI list.
        """
        fs_voi_list = self.defVOIListBox.GetItems()
        [fs_voi_list.pop(fs_voi_list.index(v))
                for v in voi_list]
        self.updateFSVOIList(fs_voi_list)



if __name__ == "__main__":
    app = wx.App()

    frame = fsVOIManager(None)
    frame.Show()

    app.MainLoop()

