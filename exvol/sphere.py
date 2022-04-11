import math
import numpy as np

#-------------------------------------------------------------------------------

class Sphere:

    def __init__(self, coords, radius, label = None):
        self.coords = np.array(coords, float)
        self.x, self.y, self.z = self.coords[0], self.coords[1], self.coords[2]
        self.r = radius
        self.label = label

    #---------------------------------------------------------------------------

    def __str__(self):
        return "{} {} r = {}".format(self.label, self.coords, self.r)

    #---------------------------------------------------------------------------

    def __repr__(self):
        return self.__str__()

    #---------------------------------------------------------------------------

    def __enter__(self):
        return self

    #---------------------------------------------------------------------------

    def __exit__(self, type, value, traceback):
        del self

    #---------------------------------------------------------------------------

    def translate(self, vector):
        vector = np.array(vector, float)
        self.coords += vector
        self.x, self.y, self.z = self.coords[0], self.coords[1], self.coords[2]

    #---------------------------------------------------------------------------

    def rotate(self, matrix):
        self.coords = matrix @ self.coords
        self.x, self.y, self.z = self.coords[0], self.coords[1], self.coords[2]

#-------------------------------------------------------------------------------

def overlap_pbc(sphere1, sphere2, box_size):
    if not isinstance(sphere1, list): sphere1 = [sphere1]
    if not isinstance(sphere2, list): sphere2 = [sphere2]

    for s1 in sphere1:
        for s2 in sphere2:

            pointing = np.array( [s1.x - s2.x,
                                  s1.y - s2.y,
                                  s1.z - s2.z] )

            radii_sum = s1.r + s2.r
            radii_sum_pbc = box_size - radii_sum

            if ( pointing[0] > radii_sum and pointing[0] < radii_sum_pbc ) or ( pointing[0] < -radii_sum and pointing[0] > -radii_sum_pbc ):
                continue
            elif ( pointing[1] > radii_sum and pointing[1] < radii_sum_pbc ) or ( pointing[1] < -radii_sum and pointing[1] > -radii_sum_pbc ):
                continue
            elif ( pointing[2] > radii_sum and pointing[2] < radii_sum_pbc ) or ( pointing[2] < -radii_sum and pointing[2] > -radii_sum_pbc ):
                continue
            else:
                for i in range(3):
                    while pointing[i] >= box_size/2:
                        pointing[i] -= box_size
                    while pointing[i] <= -box_size/2:
                        pointing[i] += box_size

                if np.sum( pointing**2 ) <= radii_sum**2: return True

    return False

#-------------------------------------------------------------------------------