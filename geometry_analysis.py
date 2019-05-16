#This is my geometry code
import numpy
import sys
import os

xyz_file = os.path.join('data','benzene.xyz')
outfile = open(xyz_file, 'r')
data = outfile.readlines()
outfile.close()
waterdata = data[2:]
initialcoords = []
coords = []
symbols = []
for i in range(0,len(waterdata)):
        initialcoords.append(waterdata[i].split())
        symbols.append(initialcoords[i][0])
coords = numpy.array(initialcoords)[:,1:].astype(numpy.float)
def calculate_distance(atom1,atom2):
        """
        Calculate the distance between two atoms.

        Parameters
        ----------
        atom1: list
            A list of coordinates [x, y, z]
        atom2: list
            A list of coordinates [x, y, z]
        
        Returns
        -------
        bond_length: float
            The distance between atoms.
        Examples
        --------
        >>> calculate_distance([0,0,0], [0,0,1])
        1.0
        """
        x_distance = atom1[0]-atom2[0]
        y_distance = atom1[1]-atom2[1]
        z_distance = atom1[2]-atom2[2]
        distance = numpy.sqrt(x_distance**2+y_distance**2+z_distance**2)
        return distance

def bond_check(bond_distance,min=0,max=1.5):
        if bond_distance > min and bond_distance < max:
            is_a_bond = True
        else:
            is_a_bond = False
        return is_a_bond
for numA, atomA in enumerate(coords):
    for numB, atomB in enumerate(coords):
        distance_AB = calculate_distance(atomA, atomB)
        if bond_check(distance_AB,max=1.6):
            print(F'{symbols[numA]} to {symbols[numB]} : {distance_AB:.3f}')
