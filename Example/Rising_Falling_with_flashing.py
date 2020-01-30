"code for flashing 400ms"
import pyvisa as visa
from heder.instr import *


def test(volt, delay):
    ps.setVolt(volt)
    print(ps.measureVolt())
    print(ps.measureCurr())
    ps.delay(delay)
    return "success"


# instrument address
PSN5744USB = "USB0::2391::38151::US15J0384P::0::INSTR"
PSN5744Eth = "TCPIP0::169.254.57.0::inst0::INSTR"
PSTektronix = "USB0::1689::913::081001126668003045::0::INSTR"

rm = visa.ResourceManager()
rm.list_resources()
PS = rm.open_resource(PSTektronix)   # choose the proper address for your instrument
print('Power supply detected=> ' + PS.query('*IDN?'))  # chk communication is established or NOT

ps = PSupply(PS)

ps.on()
ps.setCurr(3)  # set current to 3 amp
var = 1

for i in range(16, 20):  # set the range from 9 to 16 V flashing
    test(i, .4)
    test(0, .4)
    i += .5
    test(i, .4)
    test(0, .4)
for i in range(19, 16, -1):  # set the range from 9 to 16 V flashing
    test(i, .4)
    test(0, .4)
    i -= .5
    test(i, .4)
    test(0, .4)

ps.off()
PS.close()
print("process complete")
