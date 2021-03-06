from __builtin__ import enumerate

import matplotlib

from kid_readout.roach import baseband

matplotlib.use('agg')
import numpy as np
import time
import sys
from kid_readout.utils import data_file,sweeps
from kid_readout.resonator.resonator import fit_best_resonator
from kid_readout.equipment import hittite_controller
from kid_readout.equipment import lockin_controller
from kid_readout.equipment.agilent_33220 import FunctionGenerator

fg = FunctionGenerator()

hittite = hittite_controller.hittiteController()
lockin = lockin_controller.lockinController()
print lockin.get_idn()

hittite.on()
hittite.set_power(0)
if True: #cw case:
    mmw_source_frequency = 158e9
    hittite.set_freq(mmw_source_frequency/12)
else:
    mmw_source_frequency = -1.0

source_on_freq_scale = 0.999#1.0  # nominally 1 if low-ish power

ri = baseband.RoachBaseband()
f0s = np.load('/home/gjones/kid_readout/apps/sc5x4_0813f12.npy')
f0s.sort()
f0s = f0s[[0,1,2,3,4,5,6,7,8,9,10,13,14,15,16,17]]  # remove close packed resonators to enable reading out all simultaneously

if mmw_source_frequency == -1:
    suffix = "mmwnoisestep"
else:
    suffix = "mmwcwstep"
mmw_source_modulation_freq = ri.set_modulation_output(7)
mmw_atten_turns = (6.5,6.5)

def source_on():
    ri.set_modulation_output(rate='low')

def source_off():
    ri.set_modulation_output(rate='high')

def source_modulate(rate=7):
    return ri.set_modulation_output(rate=rate)

nf = len(f0s)
atonce = 16
if nf % atonce > 0:
    print "extending list of resonators to make a multiple of ",atonce
    f0s = np.concatenate((f0s,np.arange(1,1+atonce-(nf%atonce))+f0s.max()))

nsamp = 2**18
step = 1
nstep = 80
f0binned = np.round(f0s*nsamp/512.0)*512.0/nsamp
offset_bins = np.arange(-(nstep+1),(nstep+1))*step

offsets = offset_bins*512.0/nsamp
offsets = np.concatenate(([offsets.min()-20e-3,],offsets,[offsets.max()+20e-3]))

print f0s
print offsets*1e6
print len(f0s)

if False:
    from kid_readout.equipment.parse_srs import get_all_temperature_data
    while True:
        temp = get_all_temperature_data()[1][-1]
        print "mk stage at", temp
        if temp > 0.348:
            break
        time.sleep(300)
    time.sleep(600)
start = time.time()

max_fit_error = 0.5
use_fmin = False
attenlist = [39,37,35,33,31,29]
while True:
    print "*"*40
    print "Enter mmw attenuator values as a tuple i.e.: 6.5,6.5 or type exit to stop collecting data"
    mmw_atten_str = raw_input("mmw attenuator values: ")
    if mmw_atten_str == 'exit':
        break
    else:
        mmw_atten_turns = eval(mmw_atten_str)

    nsamp = 2**18
    step = 1
    nstep = 80
    offset_bins = np.arange(-(nstep+1),(nstep+1))*step

    offsets = offset_bins*512.0/nsamp
    offsets = np.concatenate(([offsets.min()-20e-3,],offsets,[offsets.max()+20e-3]))

    source_on()
    print "setting attenuator to",attenlist[0]
    ri.set_dac_attenuator(attenlist[0])
    f0binned = np.round(f0s*nsamp/512.0)*512.0/nsamp
    f0binned = f0binned*source_on_freq_scale
    measured_freqs = sweeps.prepare_sweep(ri,f0binned,offsets,nsamp=nsamp)
    print "loaded waveforms in", (time.time()-start),"seconds"

    sweep_data = sweeps.do_prepared_sweep(ri, nchan_per_step=atonce, reads_per_step=1)
    orig_sweep_data = sweep_data
    meas_cfs = []
    idxs = []
    delays = []
    for m in range(len(f0s)):
        fr,s21,errors = sweep_data.select_by_freq(f0s[m])
        thiscf = f0s[m]*source_on_freq_scale
        res = fit_best_resonator(fr[1:-1],s21[1:-1],errors=errors[1:-1]) #Resonator(fr,s21,errors=errors)
        delay = res.delay
        delays.append(delay)
        s21 = s21*np.exp(2j*np.pi*res.delay*fr)
        res = fit_best_resonator(fr,s21,errors=errors)
        fmin = fr[np.abs(s21).argmin()]
        print "s21 fmin", fmin, "original guess",thiscf,"this fit", res.f_0, "delay",delay,"resid delay",res.delay
        if use_fmin:
            meas_cfs.append(fmin)
        else:
            if abs(res.f_0 - thiscf) > max_fit_error:
                if abs(fmin - thiscf) > max_fit_error:
                    print "using original guess"
                    meas_cfs.append(thiscf)
                else:
                    print "using fmin"
                    meas_cfs.append(fmin)
            else:
                print "using this fit"
                meas_cfs.append(res.f_0)
        idx = np.unravel_index(abs(measured_freqs - meas_cfs[-1]).argmin(),measured_freqs.shape)
        idxs.append(idx)

    delay = np.median(delays)
    print "median delay is ",delay
    nsamp = 2**22
    step = 1

    offset_bins = np.array([-8,-4,-2,-1,0,1,2,4])
    offset_bins = np.concatenate(([-40,-20],offset_bins,[20,40]))
    offsets = offset_bins*512.0/nsamp

    meas_cfs = np.array(meas_cfs)
    f0binned_meas = np.round(meas_cfs*nsamp/512.0)*512.0/nsamp
    f0s = f0binned_meas
    measured_freqs = sweeps.prepare_sweep(ri,f0binned_meas,offsets,nsamp=nsamp)
    print "loaded updated waveforms in", (time.time()-start),"seconds"



    sys.stdout.flush()
    time.sleep(1)


    df = data_file.DataFile(suffix=suffix)
    df.nc.mmw_atten_turns=mmw_atten_turns
    for k,atten in enumerate(attenlist):
        ri.set_dac_attenuator(atten)
        print "measuring at attenuation", atten
        df.log_hw_state(ri)
        if k != 0:
            orig_sweep_data = None
        sweep_data = sweeps.do_prepared_sweep(ri, nchan_per_step=atonce, reads_per_step=1, sweep_data=orig_sweep_data)
        df.add_sweep(sweep_data)
        meas_cfs = []
        idxs = []
        for m in range(len(f0s)):
            fr,s21,errors = sweep_data.select_by_freq(f0s[m])
            thiscf = f0s[m]*source_on_freq_scale
            s21 = s21*np.exp(2j*np.pi*delay*fr)
            res = fit_best_resonator(fr,s21,errors=errors) #Resonator(fr,s21,errors=errors)
            fmin = fr[np.abs(s21).argmin()]
            print "s21 fmin", fmin, "original guess",thiscf,"this fit", res.f_0
            if k != 0 or use_fmin:
                print "using fmin"
                meas_cfs.append(fmin)
            else:
                if abs(res.f_0 - thiscf) > max_fit_error:
                    if abs(fmin - thiscf) > max_fit_error:
                        print "using original guess"
                        meas_cfs.append(thiscf)
                    else:
                        print "using fmin"
                        meas_cfs.append(fmin)
                else:
                    print "using this fit"
                    meas_cfs.append(res.f_0)
            idx = np.unravel_index(abs(measured_freqs - meas_cfs[-1]).argmin(),measured_freqs.shape)
            idxs.append(idx)
        print meas_cfs
        if k == 0:
            ri.add_tone_freqs(np.array(meas_cfs))
            ri.select_bank(ri.tone_bins.shape[0]-1)
        else:
            best_bank = (np.abs((ri.tone_bins[:,0]*ri.fs/ri.tone_nsamp)-meas_cfs[0]).argmin())
            print "using bank",best_bank
            print "offsets:", ((ri.tone_bins[best_bank,:]*ri.fs/ri.tone_nsamp)-meas_cfs)
            ri.select_bank(best_bank)
        ri._sync()
        time.sleep(0.5)


        #raw_input("turn on LED take data")

        df.log_hw_state(ri)
        nsets = len(meas_cfs)/atonce
        tsg = None
        for iset in range(nsets):
            selection = range(len(meas_cfs))[iset::nsets]
            ri.select_fft_bins(selection)
            ri._sync()
            time.sleep(0.4)
            t0 = time.time()
            dmod,addr = ri.get_data_seconds(30)
            x,y,r,theta = lockin.get_data()

            tsg = df.add_timestream_data(dmod, ri, t0, tsg=tsg, mmw_source_freq=mmw_source_frequency,
                                         mmw_source_modulation_freq=mmw_source_modulation_freq,
                                         zbd_voltage=x)
            df.sync()
            print "done with sweep"

    ri.set_dac_attenuator(attenlist[0])
    mmw_source_modulation_freq = source_modulate()
    df.log_hw_state(ri)
    nsets = len(meas_cfs)/atonce
    tsg = None
    for iset in range(nsets):
        selection = range(len(meas_cfs))[iset::nsets]
        ri.select_fft_bins(selection)
        ri._sync()
        time.sleep(0.4)
        t0 = time.time()
        dmod,addr = ri.get_data_seconds(4)
        x,y,r,theta = lockin.get_data()

        tsg = df.add_timestream_data(dmod, ri, t0, tsg=tsg, mmw_source_freq=mmw_source_frequency,
                                     mmw_source_modulation_freq=mmw_source_modulation_freq,
                                     zbd_voltage=x)
        df.sync()
        print "done with sweep"


    # now do source off

    nsamp = 2**18
    step = 1
    nstep = 80
    offset_bins = np.arange(-(nstep+1),(nstep+1))*step

    offsets = offset_bins*512.0/nsamp
    offsets = np.concatenate(([offsets.min()-20e-3,],offsets,[offsets.max()+20e-3]))

    source_off()
    print "setting attenuator to",attenlist[0]
    ri.set_dac_attenuator(attenlist[0])
    f0binned = np.round(f0s*nsamp/512.0)*512.0/nsamp
    measured_freqs = sweeps.prepare_sweep(ri,f0binned,offsets,nsamp=nsamp)
    print "loaded waveforms in", (time.time()-start),"seconds"

    sweep_data = sweeps.do_prepared_sweep(ri, nchan_per_step=atonce, reads_per_step=1)
    orig_sweep_data = sweep_data
    meas_cfs = []
    idxs = []
    delays = []
    for m in range(len(f0s)):
        fr,s21,errors = sweep_data.select_by_freq(f0s[m])
        thiscf = f0s[m]
        res = fit_best_resonator(fr[1:-1],s21[1:-1],errors=errors[1:-1]) #Resonator(fr,s21,errors=errors)
        delay = res.delay
        delays.append(delay)
        s21 = s21*np.exp(2j*np.pi*res.delay*fr)
        res = fit_best_resonator(fr,s21,errors=errors)
        fmin = fr[np.abs(s21).argmin()]
        print "s21 fmin", fmin, "original guess",thiscf,"this fit", res.f_0, "delay",delay,"resid delay",res.delay
        if use_fmin:
            meas_cfs.append(fmin)
        else:
            if abs(res.f_0 - thiscf) > max_fit_error:
                if abs(fmin - thiscf) > max_fit_error:
                    print "using original guess"
                    meas_cfs.append(thiscf)
                else:
                    print "using fmin"
                    meas_cfs.append(fmin)
            else:
                print "using this fit"
                meas_cfs.append(res.f_0)
        idx = np.unravel_index(abs(measured_freqs - meas_cfs[-1]).argmin(),measured_freqs.shape)
        idxs.append(idx)

    delay = np.median(delays)
    print "median delay is ",delay
    nsamp = 2**22
    step = 1

    offset_bins = np.array([-8,-4,-2,-1,0,1,2,4])
    offset_bins = np.concatenate(([-40,-20],offset_bins,[20,40]))
    offsets = offset_bins*512.0/nsamp

    meas_cfs = np.array(meas_cfs)
    f0binned_meas = np.round(meas_cfs*nsamp/512.0)*512.0/nsamp
    f0s = f0binned_meas
    measured_freqs = sweeps.prepare_sweep(ri,f0binned_meas,offsets,nsamp=nsamp)
    print "loaded updated waveforms in", (time.time()-start),"seconds"



    sys.stdout.flush()
    time.sleep(1)


    df.log_hw_state(ri)
    sweep_data = sweeps.do_prepared_sweep(ri, nchan_per_step=atonce, reads_per_step=1, sweep_data=orig_sweep_data)
    df.add_sweep(sweep_data)
    meas_cfs = []
    idxs = []
    for m in range(len(f0s)):
        fr,s21,errors = sweep_data.select_by_freq(f0s[m])
        thiscf = f0s[m]
        s21 = s21*np.exp(2j*np.pi*delay*fr)
        res = fit_best_resonator(fr,s21,errors=errors) #Resonator(fr,s21,errors=errors)
        fmin = fr[np.abs(s21).argmin()]
        print "s21 fmin", fmin, "original guess",thiscf,"this fit", res.f_0
        if use_fmin:
            meas_cfs.append(fmin)
        else:
            if abs(res.f_0 - thiscf) > max_fit_error:
                if abs(fmin - thiscf) > max_fit_error:
                    print "using original guess"
                    meas_cfs.append(thiscf)
                else:
                    print "using fmin"
                    meas_cfs.append(fmin)
            else:
                print "using this fit"
                meas_cfs.append(res.f_0)
        idx = np.unravel_index(abs(measured_freqs - meas_cfs[-1]).argmin(),measured_freqs.shape)
        idxs.append(idx)
    print meas_cfs

    df.nc.close()

print "completed in",((time.time()-start)/60.0),"minutes"
