#!/usr/bin/python

import h5py
import os
import sys
from pathlib import Path

def is_valid_h5_file(path):
  """ 
  Checks to ensure that the file path(s) is/are hdf5 files
  """
  try:
    file = h5py.File(path, 'r')
  except IOError:
    raise argparse.ArgumentTypeError("File is not valid h5 format")
  return path

def get_h5_file(path):
  try:
    file = h5py.File(path, 'r')
  except Exception:
    raise IOError("Not a valid h5 file")
  return file

def getNumberOfFiles(path):
    """Return number of data files linked to a master file. Much
    slower than listing the number of files in a master file but 
    also checks for correct type."""
    f = get_h5_file(path)
    group = f['/entry/data']
    num = 0
    for value in group:
        if isinstance(group.get(value, getlink=True), h5py.ExternalLink):
            num += 1
    return num

def getNumberOfFiles_fast(path):
  """return number of data files by simply
  finding the length of the H5 group. No checks."""
  f = get_h5_file(file) 
  return len(f['/entry/data'])

def getNumberOfFilesToProcess(path,num=None):
  if num == None:
    return getNumberOfFiles_fast(path)
  else:
    return num

def setupMasterList(arglist):
  masterlist = []
  for masterpath in arglist:
    masterlist.append(Path(masterpath.strip('_master.h5')))
  return masterlist

def setupMasterDirectories(arglist):
  for masterpath in arglist:
    masterpath.mkdir(exist_ok=True)

