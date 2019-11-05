import pyvisa as visa
from heder.instr import *


def test(volt, Dtime):
    ps.SVolt(volt)
    print("voltage=" + ps.MVolt())
    print("Current=" + ps.MCurr())
    ps.delay(Dtime)
    return "success"


# instrument address
PSN5744USB = "USB0::2391::38151::US15J0384P::0::INSTR"
PSN5744Eth = "TCPIP0::169.254.57.0::inst0::INSTR"
PSTektronix = "USB0::1689::913::081001126668003045::0::INSTR"

rm = visa.ResourceManager()
rm.list_resources()
PS = rm.open_resource(PSN5744Eth)   # choose the proper address for your instrument
print('Power supply detected=> ' + PS.query('*IDN?'))  # chk communication is established or NOT

ps = PSupply(PS)

ps.SCurr(3)  # set current to 3 amp

for i in range(9, 16):  # set the range from 9 to 16 V
    test(i, 2)
    i += .5
    test(i, 2)

print("process complete")
