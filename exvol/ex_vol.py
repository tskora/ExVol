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

def rescale_tracer(tracer, scale_tracer):

	for t in tracer:
		t.coords *= scale_tracer
		t.r *= scale_tracer

#-------------------------------------------------------------------------------

def estimate_excluded_volume(seed, tracer, crowders, number_of_trials, box_size, scale_tracer, disable_progress_bar = False, dimension = 3):

	if scale_tracer != 1.0: rescale_tracer(tracer, scale_tracer)

	pseudorandom_number_generator = initialize_pseudorandom_number_generation(seed)
	
	count = 0

	for i in tqdm( range(number_of_trials), disable = disable_progress_bar ):

		put_tracer_at_center(tracer)

		rotation_matrix = Rotation.random(random_state = pseudorandom_number_generator).as_matrix()

		translation_vector = pseudorandom_number_generator.rand(dimension)
		translation_vector = translation_vector * box_size - box_size / 2

		for t in tracer:
			t.rotate(rotation_matrix)
			t.translate(translation_vector)

		if overlap_pbc( tracer, crowders, box_size ):

			count += 1

	return count / number_of_trials

#-------------------------------------------------------------------------------