"""

sshete requirment for VW216 E09

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


for i in range(16, 7, -1):
    ps.setVolt(16)
    ps.delay(10)  # 16 V for 10 SEC
    ps.setVolt(i - 0.5)
    ps.delay(5)  # 15.5 v for 5S
    ps.setVolt(16)
    ps.delay(10)  # 16 V for 10 SEC
    ps.setVolt(i - 1)
    ps.delay(5)

ps.off()
PS.close()
print("process complete")
