__author__ = 'gjones'

"""
None of the tests in this module should require actual hardware
"""
import kid_readout.roach.tests.mock_roach
import kid_readout.roach.tests.mock_valon
import kid_readout.roach.heterodyne
import kid_readout.roach.baseband
import kid_readout.roach.r2baseband
import kid_readout.roach.r2heterodyne
import kid_readout.roach.calculate
from kid_readout.measurement.core import StateDict
import numpy as np

def test_calc_fft_bins():
    mr = kid_readout.roach.tests.mock_roach.MockRoach('roach')
    mv = kid_readout.roach.tests.mock_valon.MockValon()
    np.random.seed(123)
    for class_ in [kid_readout.roach.heterodyne.RoachHeterodyne,
                   kid_readout.roach.baseband.RoachBaseband]:
        ri = class_(roach=mr,initialize=False, adc_valon=mv)
        for nsamp in 2**np.arange(10,18):
            max_nsamp = nsamp
            if not ri.heterodyne:
                max_nsamp = nsamp/2 # only positive bins are valid for baseband
            tone_bins = np.random.random_integers(0,max_nsamp-1,size=128) #arguments give closed interval,
            # and need to avoid max_nsamp edge
            bins = ri.calc_fft_bins(tone_bins,nsamp)
            print "testing",class_,"nsamp=2**",np.log2(nsamp)
            assert(np.all(bins>=0))
            assert(np.all(bins < ri.nfft))

def test_state():
    mr = kid_readout.roach.tests.mock_roach.MockRoach('roach')
    mv = kid_readout.roach.tests.mock_valon.MockValon()
    np.random.seed(123)
    for class_ in [kid_readout.roach.heterodyne.RoachHeterodyne,
                   kid_readout.roach.baseband.RoachBaseband,
                   kid_readout.roach.r2baseband.Roach2Baseband,
                   kid_readout.roach.r2heterodyne.Roach2Heterodyne]:
        ri = class_(roach=mr,initialize=False, adc_valon=mv)
        print "Testing:",class_,
        print "get_state",
        ri.get_state()
        _ = ri.state
        print "get_state_arrays",
        ri.get_state_arrays()
        _ = ri.state_arrays
        print "get_active_state_arrays"
        ri.get_active_state_arrays()
        _ = ri.active_state_arrays

def test_get_measurement():
    mr = kid_readout.roach.tests.mock_roach.MockRoach('roach')
    mv = kid_readout.roach.tests.mock_valon.MockValon()
    for class_ in [kid_readout.roach.heterodyne.RoachHeterodyne,
                   kid_readout.roach.baseband.RoachBaseband]:
        ri = class_(roach=mr,adc_valon=mv,initialize=False)
        ri.set_tone_baseband_freqs(np.linspace(100,120,32),nsamp=2**16)
        ri.select_fft_bins(range(32))
        blah = ri.get_measurement_blocks(2)

def test_calculate_modulation_period():
    roach_state = StateDict(modulation_rate=7, modulation_output=2)
    assert(kid_readout.roach.calculate.modulation_period_samples(roach_state)==256)

def test_precomputed_wavenorm():
    mr = kid_readout.roach.tests.mock_roach.MockRoach('roach')
    mv = kid_readout.roach.tests.mock_valon.MockValon()
    for class_ in [kid_readout.roach.heterodyne.RoachHeterodyne,
                   kid_readout.roach.baseband.RoachBaseband]:
        ri = class_(roach=mr,adc_valon=mv,initialize=False)
        for k in range(9):
            ri.set_tone_baseband_freqs(np.linspace(100,120,2**k),nsamp=2**16, preset_norm=False)
            actual_wavenorm = ri.wavenorm
            ri.set_tone_baseband_freqs(np.linspace(100,120,2**k),nsamp=2**16, phases=ri.phases, preset_norm=True)
            assert(ri.wavenorm >= 0.99*actual_wavenorm)   #guarantees the wave won't overflow

def test_get_bank():
    mr = kid_readout.roach.tests.mock_roach.MockRoach('roach')
    mv = kid_readout.roach.tests.mock_valon.MockValon()
    np.random.seed(123)
    for class_ in [kid_readout.roach.heterodyne.RoachHeterodyne,
                   kid_readout.roach.baseband.RoachBaseband,
                   kid_readout.roach.r2baseband.Roach2Baseband,
                   kid_readout.roach.r2heterodyne.Roach2Heterodyne]:
        ri = class_(roach=mr,initialize=False, adc_valon=mv)
        assert(ri.get_current_bank() is not None)
