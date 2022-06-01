from exvol.sphere import Sphere, overlap_pbc
from exvol.messaging import timestamp

import numpy as np

from tqdm import tqdm

from scipy.spatial.transform import Rotation

#-------------------------------------------------------------------------------

def ensure_tracer_is_one_pbc_replica(tracer, box_size):

    for i in range(len(tracer)-1):

        for j in range(3):

            while tracer[i+1].coords[j] - tracer[i].coords[j] > box_size/2:
                tracer[i+1].coords[j] -= box_size

            while tracer[i+1].coords[j] - tracer[i].coords[j] < -box_size/2:
                tracer[i+1].coords[j] += box_size

#-------------------------------------------------------------------------------

def pin_tracer_to_surface(tracer, box_size, hook):

	shift = np.copy(tracer[hook].coords)

	shift2 = np.array([0.0, 0.0, tracer[hook].r])

	for i in range(len(tracer)):

		tracer[i].coords -= shift

		tracer[i].coords += shift2

#-------------------------------------------------------------------------------

def put_tracer_at_center(tracer):

	gc = np.mean([t.coords for t in tracer], axis = 0)

	for t in tracer:

		t.translate(-gc)

#-------------------------------------------------------------------------------

def initialize_pseudorandom_number_generation(seed = None):

	if seed is None:
		seed = np.random.randint(2**32 - 1)

	pseudorandom_number_generator = np.random.RandomState(seed)

	return pseudorandom_number_generator

#-------------------------------------------------------------------------------

def is_over_surface(tracer):

	for t in tracer:
		h = t.coords[-1]
		if h < t.r: return False

	return True


def estimate_excluded_volume(seed, tracer, crowders, number_of_trials, box_size, disable_progress_bar = False, dimension = 3):

	pseudorandom_number_generator = initialize_pseudorandom_number_generation(seed)
	
	count = 0

	for i in tqdm( range(number_of_trials), disable = disable_progress_bar ):

		translation_vector = pseudorandom_number_generator.rand(dimension)

		translation_vector = translation_vector * box_size - box_size / 2
		translation_vector = np.array( list(translation_vector) + (3-dimension)*[0.0] )

		# print(tracer)
		# print(translation_vector)
		# 1/0

		assert is_over_surface(tracer)
		
		for t in tracer:
			t.translate(translation_vector)

		# print(tracer)
		# 1/0

		if overlap_pbc( tracer, crowders, box_size ):

			count += 1

	return count / number_of_trials

#-------------------------------------------------------------------------------