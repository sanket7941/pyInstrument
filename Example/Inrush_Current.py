"""
insrtrument required
1) waveform generator
2) DSO
"""

import pyvisa as visa
from pyinstrument import WGenerator

# instrument address

WGen = "USB0::0x0957::0x2C07::MY52812730::INSTR"

rm = visa.ResourceManager()
rm.list_resources()
WG = rm.open_resource(WGen)  # choose the proper address for your instrument
print('instrument detected=> ' + WG.query('*IDN?'))  # chk communication is established or NOT

wg = WGenerator(WG)

wg.sqrWave(1000)
# wg.burst(1,0,1)
wg.sweep()

print("burst mode Setup successfully :) ")
