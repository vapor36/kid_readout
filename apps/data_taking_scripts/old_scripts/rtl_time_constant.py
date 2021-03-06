import numpy as np

import time
#import rtlsdr
import kid_readout.equipment.rtlkid

#rtl = rtlsdr.RtlSdr()
#rtl.gain = 40.2
#rtl.center_freq = 870.840e6
#rtl.sample_rate = 1024e3

#f_ref = 871.380e6
#f_ref = 870.436e6
f_ref=991.825e6
rtl = kid_readout.equipment.rtlkid.RtlKidReadout()
rtl.rtl.gain = 40.0
rtl.rtl.sample_rate = 256e3
rtl.hittite.set_power(10.0)
rtl.hittite.on()
rtl.adjust_freq_correction()
error = rtl.measure_freq_error()
if abs(error/1e9) > 5e-6:
    print "adjusting freq correction failed!"
while True:
    start_time = time.time()
    freq,data = rtl.do_scan(freqs=np.linspace(-8e5,3e5,500)+f_ref,level=0.0)
    peak = freq[data.argmin()]#+1e3
    print "peak at",peak
    rtl.hittite.set_freq(peak)
    rtl.rtl.center_freq = peak + 10e3
    rtl.hittite.on()
    time.sleep(2)
    d = rtl.rtl.read_samples(2**21)
    d = rtl.rtl.read_samples(2**21)
    d = d[2048:]
    filename = '/home/data2/rtl/%s' % (time.strftime('%Y-%m-%d_%H-%M-%S'))
    np.savez(filename,data=d, time= time.time(), sample_rate=rtl.rtl.sample_rate, gain= rtl.rtl.gain,
             center_freq = rtl.rtl.center_freq,sweep_freq = freq, sweep_mag = data, start_time = start_time)
    print "saved in ", filename

    7/0
    time.sleep(120.0)