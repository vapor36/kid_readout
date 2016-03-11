from testfixtures import TempDirectory
from kid_readout.measurement import core, single, multiple
from kid_readout.measurement.test.utilities import get_measurement
from kid_readout.measurement.io import nc

def test_read_write_measurement():
    with TempDirectory(path='/home/flanigan/temp') as directory:
        io = nc.IO(directory.path)
        original = get_measurement()
        name = 'measurement'
        core.write(original, io, name)
        read = core.read(io, name)
    assert original == read


def test_read_write_stream():
    with TempDirectory() as directory:
        io = nc.IO(directory.path)
        original = single.make_stream()
        name = 'stream'
        core.write(original, io, name)
        read = core.read(io, name)
    assert original == read


def test_read_write_streamarray():
    with TempDirectory() as directory:
        io = nc.IO(directory.path)
        original = multiple.make_stream_array()
        name = 'stream_array'
        core.write(original, io, name)
        read = core.read(io, name)
    assert original == read
