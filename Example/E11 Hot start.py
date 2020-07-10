"""

E-11 Start pulses

Purpose
When the engine is started, the battery voltage drops to a low value for a short period in
order to then rise again slightly. Most components are briefly activated immediately
before the starting process, deactivated during the starting process, and then activated
again after the starting process once the engine is running. This test examines the
behavior of the component in the event of voltage sags caused by starting.
The starting process may be carried out under varying vehicle starting conditions: cold
start and hot start (automatic restart in the case of a start-stop system). In order to cover
both cases, two different test cases are required. A component must always run through
both sequences.

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
    ps.setVolt(11)
    ps.delay(5)  # 11 V for 5 SEC
    ps.setVolt(7)
    ps.delay()  # 15.5 v for 5S
    ps.setVolt(16)
    ps.delay(10)  # 16 V for 10 SEC
    ps.setVolt(i - 1)
    ps.delay(5)

ps.off()
PS.close()
print("process complete")
