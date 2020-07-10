"""

E-05 Load dump
Purpose
Dumping of an electric load, in conjunction with a battery with reduced buffering
capacity, results in a high-energy overvoltage pulse due to generator properties. This
test is meant to simulate this pulse.

"""
import pyvisa as visa
from pyinstrument import PSupply


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
    ps.setVolt(13.5)
    ps.delay(60)  # 13.5 V for 60 SEC
    ps.setVolt(27)
    ps.delay(.3)  # 27 v for 300mS

ps.off()
PS.close()
print("process complete")
