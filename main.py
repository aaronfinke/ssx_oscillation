import os, sys, h5py
from argparse import ArgumentParser
from make_xds_template import *
import setup
from Master import Master


def main():
    """
    Main routine for serialCAP
    """
    parser = ArgumentParser(description="write to a file")

    parser.add_argument("-i","--input", type=setup.is_valid_h5_file, required=True, nargs='+',
    help="path(s) of HDF5 master file(s)")

    parser.add_argument("-b","--beamcenter", nargs=2, required=True,
    help="beam center in X and Y (two arguments)")

    parser.add_argument("-r","--oscillation", type=float, default=1,
    help="oscillation angle per well, default = 1")

    parser.add_argument("-d","--distance", type=float, default=100,
    help="detector distance in mm")

    parser.add_argument("-w","--wavelength", type=float, default=1.216,
    help="Wavelength in Angstrom, default is 1.216")

    parser.add_argument("-f","--framesperdegree", type=int, default=5,
    help="Number of frames per degree, default is 5")

    parser.add_argument("-t","--totalframes", type=int, default=0,
    help="Total number of frames to be processed, default all")

    parser.add_argument("--output", default=os.getcwd(),
    help="Use this option to change output directory, default pwd")

    parser.add_argument("-sg","--spacegroup", type=int, default=0,
    help="Space group")

    parser.add_argument("-u","--unitcell", type=str, default="50 50 50 90 90 90",
    help="unit cell")

    argslist = parser.parse_args()
    for masterfile in argslist.input:
        master1= Master(argslist,masterfile)
        master1.printDataWells()

if __name__ == '__main__':
    main()
