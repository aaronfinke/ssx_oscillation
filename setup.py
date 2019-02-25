#!/usr/bin/python

import h5py, os, sys
from contextlib import contextmanager
from pathlib import Path


def is_valid_h5_file(path):
    """
    Checks to ensure that the file path is a valid hdf5 file
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
    f = get_h5_file(path)
    return len(f['/entry/data'])

def getNumberOfFilesToProcess(path,num=None):
    if num == None:
        return getNumberOfFiles_fast(path)
    else:
        return num

def getNumberOfDataWells(masterfile,oscillation,framesperdegree):
    """returns the number of data wells in the master file."""
    filenum = getNumberOfFiles_fast(masterfile)
    frames = framesperdegree / oscillation
    return int(filenum / frames)


def getMasterPrefix(arg):
    """"Returns the name of the master file without the "_master.h5"
    suffix.
    """
    if arg.endswith('_master.h5'):
        stripped = arg.replace('_master.h5','')
        head, tail = os.path.split(stripped)
        return tail
    else:
        return

def setupMasterDirectory(input, dir):
    "Creates a master directory."
    master = getMasterPrefix(input)
    masterdir = os.path.join(dir,master)
    try:
        os.mkdir(masterdir)
    except FileExistsError:
        pass

def getMasterDirectory(input,dir):
    master = getMasterPrefix(input)
    return os.path.join(dir,master)

def setupMasterDirectories(argslist):
    """Sets up the master directories into which data sets
    will be processed. Input is parsed arguments.
    """
    for master in argslist.input:
        masterdir = setupMasterDirectory(master,argslist.output)

def getMasterDirectoryPaths(argslist):
    """Returns paths of master directories. Input is parsed arguments.
    """
    masterlist = []
    for masterfile in argslist.input:
        master = getMasterPrefix(masterfile)
        masterdir = os.path.join(argslist.output, master)
        masterlist.append(masterdir)
    return masterlist

def setup(argslist):
    setupMasterDirectories(argslist)
