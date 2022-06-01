import click

from exvol.input import InputData, read_structure_filename
from exvol.ex_vol import ensure_tracer_is_one_pbc_replica, pin_tracer_to_surface, estimate_excluded_volume
from exvol.messaging import copyright_notice, timestamp

import multiprocessing
from multiprocessing import Pool
from functools import partial

import numpy as np

#-------------------------------------------------------------------------------

@click.command()
@click.argument('input_filename',
				type = click.Path( exists = True ))
def main(input_filename):

	timestamp( 'Reading input from {} file', input_filename )
	i = InputData(input_filename)

	timestamp( 'Input data:\n{}', i )

	print('You have {0:1d} CPUs'.format(i.input_data["omp_cores"]))

	tracer = read_structure_filename(i.input_data["tracer_filename"])

	ensure_tracer_is_one_pbc_replica(tracer, i.input_data["box_size"])

	pin_tracer_to_surface(tracer, i.input_data["box_size"], 5)

	crowders = read_structure_filename(i.input_data["crowders_filename"])
	
	pool = Pool(processes=i.input_data["omp_cores"])

	estimate_excluded_volume_partial = partial( estimate_excluded_volume, tracer = tracer, crowders = crowders, number_of_trials = i.input_data["number_of_trials"], box_size = i.input_data["box_size"], disable_progress_bar = i.input_data["disable_progress_bar"], dimension = 2 )

	excluded_volume = pool.map( estimate_excluded_volume_partial, i.input_data["seed"] )

	print(excluded_volume)
	
	exvol = np.mean(excluded_volume)
	dexvol = np.std(excluded_volume)
		
	print('fex = {} +/- {}'.format(exvol, dexvol))

#-------------------------------------------------------------------------------

if __name__ == '__main__':

	copyright_notice()
	main()
