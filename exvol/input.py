import json

import numpy as np
import multiprocessing

from exvol.sphere import Sphere

#-------------------------------------------------------------------------------

# here the list of keywords that are required for program to work is provided
REQUIRED_KEYWORDS = ["box_size", "number_of_trials", "tracer_filename", "crowders_filename"]

# here the dict of keywords:default values is provided
# if given keyword is absent in JSON, it is added with respective default value
DEFAULTS = {"float_type": 32, "verbose":False, "debug":False, "omp_cores": 0, "seed": None, "disable_progress_bar": False, "scale_tracer": 1.0}

ALL_KEYWORDS = REQUIRED_KEYWORDS + list(DEFAULTS.keys())

class InputData:

    def __init__(self, input_filename):

        self._read_input_file(input_filename)

        self._complete_with_defaults()

        self._check_for_missing_keywords()

        self._abort_if_unknown_keyword_present()

        if self.input_data["float_type"] == 32: self.input_data["float_type"] = np.float32

        elif self.input_data["float_type"] == 64: self.input_data["float_type"] = np.float64

        if self.input_data["omp_cores"] == 0:
            self.input_data["omp_cores"] = multiprocessing.cpu_count()

        if self.input_data["seed"] is None:
            self.input_data["seed"] = np.random.randint(0, 2**32 - 1, self.input_data["omp_cores"])

    #---------------------------------------------------------------------------

    def __str__(self):

        string_representation = ''

        for keyword in self.input_data.keys():
            string_representation += '{}: {}\n'.format(keyword, self.input_data[keyword])

        return string_representation

    #---------------------------------------------------------------------------

    def __repr__(self):

        return self.__str__()

    #---------------------------------------------------------------------------

    def _read_input_file(self, input_filename):

        with open(input_filename, "r") as read_file:
            self.input_data = json.load(read_file)

    #---------------------------------------------------------------------------

    def _complete_with_defaults(self):

        for default_keyword in DEFAULTS.keys():

            if default_keyword not in self.input_data.keys():

                self.input_data[default_keyword] = DEFAULTS[default_keyword]

    #---------------------------------------------------------------------------

    def _check_for_missing_keywords(self):

        for keyword in REQUIRED_KEYWORDS:
            assert keyword in self.input_data.keys(),\
                'Missing {} keyword in input JSON file.'.format(keyword)

    #---------------------------------------------------------------------------

    def _abort_if_unknown_keyword_present(self):

        for keyword in self.input_data:
            assert keyword in ALL_KEYWORDS,\
                'Unrecognized {} keyword in input JSON file.'.format(keyword)

#-------------------------------------------------------------------------------

def read_structure_filename(input_tracer_filename):

    tracer = []

    with open(input_tracer_filename, 'r') as tracer_file:

        for line in tracer_file:

            line_split = line.split()

            label = line_split[0]

            coords = [ float(line_split[i]) for i in range(1, 4) ]

            radius = float(line_split[4])

            tracer.append( Sphere(coords, radius, label) )

    return tracer

#-------------------------------------------------------------------------------