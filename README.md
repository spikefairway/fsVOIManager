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

### GUI-based definition

You can start the tool for GUI-based definition with the following command:

```
$ python fsVOIManager.py
```

This is a main window for the GUI tool.

![GUI main](https://github.com/spikefairway/fsVOIManager/blob/master/docimgs/gui_main.png)

Main window has three columns. A list on the left column has VOI defined in FreeSurfer (see $FREESURFER_HOME/FreeSurferColorLUT.txt on your computer).
A list on the top of right column indicates VOI you define. You can add or merge FreeSurfer VOI to user-defined VOI by buttons on the center column.


