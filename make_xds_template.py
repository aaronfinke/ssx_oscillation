#!/usr/bin/python

def writeToFile(filename):
  try:
    filename.write(make_XDS_template(
      "1 2 3 90 90 90", "/dev/null", 34, 45, 56, 0.2, 1.2156))
  except FileNotFoundError:
    print("File Not Found")


def make_XDS_template(unitcell, dataframes, orgx, orgy, detdist, oscillation, wavelength):
  return """SPACE_GROUP_NUMBER=0
UNIT_CELL_CONSTANTS= {unitcell}
 
NAME_TEMPLATE_OF_DATA_FRAMES= {dataframes}
JOB= XYCORR INIT COLSPOT IDXREF DEFPIX INTEGRATE CORRECT

ORGX= {orgx}  ORGY= {orgy}    
DETECTOR_DISTANCE= {detdist}   

OSCILLATION_RANGE={oscillation}  
X-RAY_WAVELENGTH={wavelength} 

DATA_RANGE= 
BACKGROUND_RANGE= 
SPOT_RANGE= 

DETECTOR=EIGER
MINIMUM_VALID_PIXEL_VALUE=0
OVERLOAD= 1048500   
SENSOR_THICKNESS=0.32 
QX=0.075  QY=0.075 
NX= 1030  NY= 1065  
UNTRUSTED_RECTANGLE=    0 1031    514  552 

LIB=/nfs/chess/sw/macchess/dectris-neggia-centos6.so

TRUSTED_REGION=0.0 1.41

DIRECTION_OF_DETECTOR_X-AXIS= 1.0 0.0 0.0
DIRECTION_OF_DETECTOR_Y-AXIS= 0.0 1.0 0.0 

MAXIMUM_NUMBER_OF_JOBS=4
MAXIMUM_NUMBER_OF_PROCESSORS=8  

ROTATION_AXIS= 0.0 -1.0 0.0
INCIDENT_BEAM_DIRECTION=0.0 0.0 1.0
FRACTION_OF_POLARIZATION=0.99 
POLARIZATION_PLANE_NORMAL= 0.0 1.0 0.0

REFINE(IDXREF)=BEAM AXIS ORIENTATION CELL  ! POSITION
REFINE(INTEGRATE)= ! ORIENTATION POSITION BEAM CELL AXIS
REFINE(CORRECT)=POSITION BEAM ORIENTATION CELL AXIS

VALUE_RANGE_FOR_TRUSTED_DETECTOR_PIXELS= 6000 30000
! INCLUDE_RESOLUTION_RANGE=50 1.8

MINIMUM_I/SIGMA=50.0
CORRECTIONS= !

SEPMIN=4.0       
CLUSTER_RADIUS=2""".format(unitcell=unitcell, dataframes=dataframes, 
  orgx=orgx, orgy=orgy, oscillation=oscillation, detdist=detdist, wavelength=wavelength)
