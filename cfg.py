import math

##

inputtraj = "dump.trj"

### Output data files

outputScd  = "Scd.dat"
outputmScd = "mScd.dat"
output2Sxx = "2Sxx.dat"
outputSzz  = "Szz.dat"

### Start and end atoms
### Remember atoms n-1 and n+1 will be pulled in

bilayernormal = [0, 0, -1]
start = 2
end = 7

 
### Data Formats

ROWDATA  = 7 ## This is the number of lumps of data we take from LAMMPS data file
ROWBOND  = 4 ## Bond data from the LAMMPS data file
ROWANGLE = 5 ## Angle data from the LAMMPS data file
