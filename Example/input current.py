import pyvisa as visa
from pyinstrument import PSupply

rm = visa.ResourceManager()
rm.list_resources()
print(rm.list_resources()[0])
PS = rm.open_resource(rm.list_resources()[0])   # choose the proper address for your instrument
print('Power supply detected=> ' + PS.query('*IDN?'))  # chk communication is established or NOT

ps = PSupply(PS)

maxVoltage = 10     # set max voltage limit
minVoltage = 0      # set Min voltage limit
delaySec = 2        # set delay time between on and off

# turn on Power supply
ps.on()
# set max current limit
ps.setCurr(5)

#print("Low beam")
print("High Beam")

ps.setVolt(9)
ps.delay(1)
print("Voltage ==> "+ ps.measureVolt() + "current ==>"+ ps.measureCurr() )
ps.delay(5)

ps.setVolt(13.5)
ps.delay(1)
print("Voltage ==> "+ ps.measureVolt() + "current ==>"+ ps.measureCurr() )
ps.delay(5)

ps.setVolt(16)
ps.delay(1)
print("Voltage ==> "+ ps.measureVolt() + "current ==>"+ ps.measureCurr() )
ps.delay(5)

ps.off()
PS.close()
rm.close()

print("process complete :)")
