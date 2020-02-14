"""
insrtrument required
1) waveform generator
2) DSO
"""

import pyvisa as visa
from ..instrument import *

# instrument address


WGen = "USB0::0x0957::0x2C07::MY52812730::INSTR"

rm = visa.ResourceManager()
rm.list_resources()
WG = rm.open_resource(WGen)  # choose the proper address for your instrument
print('instrument detected=> ' + WG.query('*IDN?'))  # chk communication is established or NOT

wg = WGenerator(WGen)
