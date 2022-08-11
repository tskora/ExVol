Input
==========

Input for ``ExVol`` consists of three text files:

- ``.json`` -- providing simulation parameters,
- ``.txt`` -- providing configuration of the crpwded box,
- ``.txt`` -- providing configuration of the inserted model,

Below we ellaborate on their structure and meaning.

``.txt`` files
**************

Configuration (``.txt``) files contain the information about the positions and sizes of beads. Each line follows a scheme:

``label x y z a``

The entries should be replaced with values specific to a given type of bead. Below their meanings are explained:

- ``label`` -- label (name) of the bead (``string``)
- ``x y z`` -- ``x``, ``y`` and ``z`` cartesian coordinates of the bead center (``float``)
- ``a`` -- the radius of the bead (``float``)

``.json`` file
*****************************

Simulation parameters are provided in a standard `JSON <https://www.json.org/json-en.html>`_ data format. It consists of multiple lines in a form of ``keyword: value`` pairs enclosed by a curly bracket. Some keywords are obligatory, but a majority is not -- for them default values will be loaded, if needed. ``pyBrown`` will inform you if it does not recognize some keywords in input ``.json`` file.

The complete list of keywords is provided below.

- ``"tracer_filename": string`` -- the name of the input inserted model configuration ``.txt`` file (*see above*), **required**
- ``"crowders_filename": string`` -- the name of the input crowded box configuration ``.txt`` file (*see above*), **required**
- ``"number_of_trials": int`` -- the total number of insertions, **required**
- ``"box_size": float`` -- length of the cubic simulation box, **required**
- ``"debug": boolean`` -- switching on/off the debug printout, default: ``false``
- ``"verbose": boolean`` -- switching on/off the verbose printout, default: ``false``
- ``"disable_progress_bar": boolean`` -- disabling the progress bar, default: ``false``
- ``"seed": int`` -- seed for pseudorandom number generation algorithm, default ``np.random.randint(2**32 - 1)``
- ``"omp_cores": int`` -- number of cores for parallel computation, default: all available