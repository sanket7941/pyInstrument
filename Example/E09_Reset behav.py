"""
E-09 Reset behavior

The reset behavior of a component in its environment is recreated and tested. General
test conditions (e.g., network, terminal, system) must be described in detail.
An arbitrary chronological sequence of repeated switch-on/switch-off processes occurs
during operation and must not result in undefined component behavior.
The reset behavior is reflected in a voltage variance and in a time-based variance. Two
different test sequences are required to simulate varying switch-off times. A component
must always run through both sequences.

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
