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

fsVOIManager defines merged VOIs with a CSV file, VOI definition file. 
