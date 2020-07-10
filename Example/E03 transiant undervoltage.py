"""
sshete requirment for VW216 E03

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

for i in range(1, 10):
    ps.setVolt(10.8)
    ps.delay(1)  # 10.8 V for 1 SEC
    ps.setVolt(9)
    ps.delay(.5)  # 9 v for 500mS

ps.off()
PS.close()
print("process complete")
