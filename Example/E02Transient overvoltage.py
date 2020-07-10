"""
E-02 Transient overvoltage
 Purpose
Switching off loads and engine revving (tip-in) may result in transient overvoltages in the
electric system. These overvoltages are simulated in this test.

"""
import pyvisa as visa
from pyinstrument import PSupply


def test(volt, delay):
    ps.setVolt(volt)
    print(ps.measureVolt())
    print(ps.measureCurr())
    ps.delay(delay)
    return "success"


rm = visa.ResourceManager()
rm.list_resources()
PS = rm.open_resource(rm.list_resources()[0])  # choose the proper address for your instrument
print('Power supply detected=> ' + PS.query('*IDN?'))  # chk communication is established or NOT

ps = PSupply(PS)

ps.on()
ps.setCurr(3)  # set current to 3 amp

ps.setVolt(0)
ps.delay(5)  # power supply off for 5 sec
ps.setVolt(16)  # UMIN
ps.delay(2)  # 16V on for 2 SEC

for i in range(1, 100):
    ps.setVolt(18)
    ps.delay(.4)  # 18 V for 400ms
    ps.setVolt(17)
    ps.delay(.6)  # 17 v for 600mS
    ps.setVolt(16)
    ps.delay(2)  # 16 V for 2 Sec

ps.off()
PS.close()
print("process complete")
