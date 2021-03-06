"""
This file tries to use sensible settings depending on the HOSTNAME
"""
import socket as _socket

from kid_readout.analysis.resources import experiments as _experiments

HOSTNAME = _socket.gethostname()

from kid_readout.settings._roach import *

if HOSTNAME == 'detectors':
    from kid_readout.settings._detectors import *
elif HOSTNAME == 'readout':
    from kid_readout.settings._readout import *
