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

        setup.setupMasterDirectory(self.masterfile, self.output)

        self.masterdirectory = getMasterdirectory(self.masterfile, self.output)

        self.numberoffiles = setup.getNumberOfFilesToProcess(self.masterfile)
        self.numberofdatawells = setup.getNumberOfDataWells(self.masterfile, self.oscillation,self.framesperdegree)




    def __str__(self):
        return "{a} and {b}".format(a=numberoffiles,b=numberofdatawells)

    def printDataWells(self):
        numOfFiles=setup.getNumberOfFilesToProcess(self.masterfile)
        filesperwell = int(self.framesperdegree*self.oscillation)
        for filenum in range(1,numOfFiles,filesperwell):
            print("{a} - {b}".format(a=filenum,b=filenum + filesperwell - 1))
