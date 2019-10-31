"""
address of all instrument !Note:-address may change sys by sys
1)osciloscope
 DSO 1:- USB0::10893::5988::MY57452459::0::INSTR FG disabled
 DSO 2:- USB0::10893::5984::MY55280225::0::INSTR

2)function Genrator
FG 1  :- USB0::2391::11271::MY52812730::0::INSTR

3)Power Supply
USB    :-  N5744 USB0::2391::38151::US15J0384P::0::INSTR
Ethernet:- N5744 TCPIP0::169.254.57.0::inst0::INSTR
#Tektronix, PWS4323, 081001126668003045, 1.24-1.23
USB0::1689::913::081001126668003045::0::INSTR


"""

import pyvisa as visa
from heder.instr import *

# instrument address
DSO1 = "USB0::10893::5988::MY57452459::0::INSTR"  # FG Disabled
DSO2 = "USB0::10893::5984::MY55280225::0::INSTR"
FG1 = "USB0::2391::11271::MY52812730::0::INSTR"

PSN5744USB = "USB0::2391::38151::US15J0384P::0::INSTR"
PSN5744Eth = "TCPIP0::169.254.57.0::inst0::INSTR"
PSTektronix = "USB0::1689::913::081001126668003045::0::INSTR"

rm = visa.ResourceManager()
rm.list_resources()
print("RM location=> " + str(rm))
P = rm.open_resource(PSN5744Eth)
print('Power supply detected=> ' + P.query('*IDN?'))  # chk communication is established or NOT

S = rm.open_resource(DSO1)
print('DSO detected=> ' + S.query('*IDN?'))  # chk communication is established or NOT

scope = OScope(S)
ps = PSupply(P)

scope.autoscale()
ps.delay(3)
ps.SVolt(10)
ps.SCurr(.1)
ps.on_off(1)

print("voltage = "+ps.MVolt())
print("process complete")
