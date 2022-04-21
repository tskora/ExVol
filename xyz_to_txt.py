import click
import json

from exvol.messaging import timestamp

#-------------------------------------------------------------------------------

@click.command()
@click.option('-i', '--input-xyz', 'input_xyz_filename',
				required = True,
				type = click.Path( exists = True ))
@click.option('-o', '--output-txt', 'output_txt_filename',
				required = True,
				type = click.Path( exists = False ))
@click.option('-r', '--radii-json', 'radii_json_filename',
				required = True,
				type = click.Path( exists = True ))
@click.option('-t', '--time', 'snapshot_time',
				required = True,
				type = float)
def main(input_xyz_filename, output_txt_filename, radii_json_filename, snapshot_time):

	timestamp( 'Input .xyz file: {}', input_xyz_filename )
	timestamp( 'Output .txt file: {}', output_txt_filename )
	timestamp( 'Radii .json file: {}', radii_json_filename )
	timestamp( 'Snapshot time: {}', snapshot_time )

	with open(radii_json_filename, 'r') as radii_json_file:

		radii = json.load(radii_json_file)

	with open(input_xyz_filename, 'r') as input_xyz_file:

		with open(output_txt_filename, 'w') as output_txt_file:

			labels = []
			coords = []

			start_snapshot = False

			for line in input_xyz_file:
				if start_snapshot:
					if 'time' in line.split():
						start_snapshot = False
						break
					else:
						if len( line.split() ) == 4:
							labels.append( line.split()[0] )
							coords.append( [ line.split()[i] for i in range(1,4) ] )
				if 'time' in line.split():
					if float(line.split()[-1]) >= snapshot_time:
						if snapshot_time != float(line.split()[-1]):
							print('Snapshot time {} insted of {}'.format(float(line.split()[-1]), snapshot_time))
						start_snapshot = True

			for label, coord in zip(labels, coords):
				output_txt_file.write('{} {} {} {} {}\n'.format(label, *coord, radii[label]))

#-------------------------------------------------------------------------------

if __name__ == '__main__':
	main()
