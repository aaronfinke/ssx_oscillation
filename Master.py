#!/usr/bin/python
import setup

class Master:

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

        
