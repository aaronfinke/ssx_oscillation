#!/usr/bin/python
import setup

class Master(object):

    def __init__(self, argslist, masterfile):
        self.masterfile = masterfile
        self.beamcenter = argslist.beamcenter
        self.oscillation = argslist.oscillation
        self.distance = argslist.distance
        self.wavelength = argslist.wavelength
        self.framesperdegree = argslist.framesperdegree
        self.totalframes = argslist.totalframes
        self.output = argslist.output
        self.spacegroup = argslist.spacegroup
        self.unitcell = argslist.unitcell

        setupMasterDirectory(self.output,self.masterfile)

        self.numberoffiles = getNumberOfFilesToProcess(self.masterfile)
        self.numberofdatawells = getNumberOfDataWells(self.masterfile, self.oscillation,self.framesperdegree)


    def __str__(self):
        return "{a} and {b}".format(a=numberoffiles,b=numberofdatawells)
