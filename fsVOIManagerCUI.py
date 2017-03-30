#!/usr/bin/env python
# coding: utf-8

__author__ = 'keisu-ma'

import sys
import pandas as pd

from fsVOIManager import mergeFSVOI

def argumentError():
    print("Invalid argument!")
    print("Usage: %s input_NIfTI_VOI_file VOI_set_file output_NIfTI_VOI_file" % (sys.argv[0]))
    sys.exit(0)

if __name__ == "__main__":
    # Load argument
    try:
        inFile = sys.argv[1]
        voiSetFile = sys.argv[2]
        outFile = sys.argv[3]
    except ValueError:
        argumentError()
    except IndexError:
        argumentError()

    # Load VOI set
    voidef = pd.read_csv(voiSetFile)

    # Apply VOI set
    mergeFSVOI(inFile, outFile, voidef)

