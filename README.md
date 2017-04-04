# fsVOIManager

**fsVOIManager** is a tool to merge volume of interests (VOIs) extracted with [FreeSurfer](https://surfer.nmr.mgh.harvard.edu/) (e.g., aparc+aseg). FreeSurfer can perform cortical and subcortical segmentations to dozens or a few hundred of brain regions. However, in some cases, hundreds of VOIs can be too much to investigate local brain functions. This tool can be useful to merge FreeSurfer VOIs to VOIs whatever you hope.

## Version

Current development status for fsVOIManager is beta.

## Requirements

- OS: Linux or Mac OS X
    - It should work well in Windows system, but, it has not been tested yet.
- FreeSurfer (5.3.0 or later)
- [Python](https://www.python.org/) (2.7 or 3.5)
- [Numpy](http://www.numpy.org/)
- [Pandas](http://pandas.pydata.org/)
- [nipy](http://nipy.org/nipy/)
- [nibabel](http://nipy.org/nibabel/)
- [wxPython Phoenix](https://wxpython.org/Phoenix/docs/html/)

## Usage

fsVOIManager requires parcellation maps extracted from FreeSurfer to merge. Only [NIfTI-1 format](https://nifti.nimh.nih.gov/nifti-1) is supported as parcellation map file. Please note that you need to convert the maps to NIfTI-1 format because format for FreeSurfer outputs is [MGH/MGZ format](https://surfer.nmr.mgh.harvard.edu/fswiki/FsTutorial/MghFormat). 

### VOI definition file

fsVOIManager defines merged VOIs with a CSV file, VOI definition file. An example for VOI definition file is the followings:

```
FS VOI No.,FS VOI name,user VOI name,user VOI No.
2,Left-Cerebral-White-Matter,SWM,1
4,Left-Lateral-Ventricle,CSF,2
5,Left-Inf-Lat-Vent,CSF,2
```

1st line defines what each column means. Each column indicates informations for VOI as follows:

- FS VOI No. : VOI No. defined in FreeSurfer. (See $FREESURFER\_HOME/FreeSurferColorLUT.txt)
- FS VOI name : Label name defined in FreeSurfer.
- user VOI name : VOI name defined by user.
- user VOI No. : VOI No. defined with fsVOIManager. These No. are assigned automatically with fsVOIManager.

2nd line in this example indicates 'Left-Cerebral-White-Matter' in the FreeSurfer parcellation map (e.g., aparc+aseg) is regarded as 'SWM' (it means subcortical white matter) in new user-defined VOI set.
3rd and 4th lines indicate 'Left-Lateral-Ventricle' and 'Left-Inf-Lat-Vent' are merged into 'CSF' (it means cerebrospinal fluid).

You can create VOI definition file from scratch. However, a GUI tool, fsVOIManager, can help you to create the definition.

### GUI-based VOI definition

You can start the tool for GUI-based definition with the following command:

```
$ python fsVOIManager.py
```

This is a main window for the GUI tool.

![GUI main](https://github.com/spikefairway/fsVOIManager/blob/master/docimgs/gui_main.png)

Main window has three columns. A list on the left column has VOI defined in FreeSurfer (see $FREESURFER_HOME/FreeSurferColorLUT.txt on your computer).
A list on the top of right column indicates VOI you define. You can add or merge FreeSurfer VOI to user-defined VOI by buttons on the center column.

'Add >>>' button simply add VOI as user-defined VOI. 'Merge as new >>>' button merges multiple FreeSurfer VOIs to an user-defined VOI. For example, if you hope to merge 'Left-Caudate' and 'Left-Putamen' to 'Left-Striatum', select 'Left-Caudate' and 'Left-Putamen' with Ctrl+Click (command+Click on Mac) or Shift+Click, and then push 'Merge as new >>>' button.

![example to merge](https://github.com/spikefairway/fsVOIManager/blob/master/docimgs/example_merge.png)

You can name a new merged VOI with pop-up window.

![Name merged VOI](https://github.com/spikefairway/fsVOIManager/blob/master/docimgs/name_mergedVOI.png)

Then, the merged VOI should be added to the list on the right columns. You can see FreeSurfer VOIs included in the new merged VOI in the bottom list on the right column.

![VOI merged](https://github.com/spikefairway/fsVOIManager/blob/master/docimgs/gen_mergedVOI.png)

'Merge to VOI >>>' button adds selected FreeSurfer VOIs to existing user-defined VOI. For example, if you hope to add 'Left-Accumbens-area' to 'Left-Striautm' you defined previously, select 'Left-Accumbens-area' on the left and 'Left-Striatum' on the right, and then push 'Merge to VOI >>>'. 

![Merge to VOI](https://github.com/spikefairway/fsVOIManager/blob/master/docimgs/merge_to_VOI.png)
![Merge to VOI 2](https://github.com/spikefairway/fsVOIManager/blob/master/docimgs/merge_to_VOI3.png)

You can manupilate VOIs you defined with buttons on the right side. The followings are explanations for the buttons:

![Open](https://github.com/spikefairway/fsVOIManager/blob/master/docimgs/open.png)
Open a CSV file which defines VOIs.

![Save](https://github.com/spikefairway/fsVOIManager/blob/master/docimgs/save.png)
Save current user-defined VOIs to CSV file.



HINTS: By default, all defined FreeSurfer VOIs are included in the list on the left. There are too many defined VOIs. For easier definition, you can load parcellation map outputted from FreeSurfer (e.g., aparc+aseg) with 'Load extracted VOI (.nii)' button. Then, you can see only VOIs existing in the loaded parcellation map. If you hope to go back default list, push 'Load default VOI list' on the bottom.




