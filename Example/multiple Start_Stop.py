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
ps.setCurr(3)
ps.setVolt(0)

for i in range(10):
    ps.setVolt(maxVoltage)      # set max voltage
    ps.delay(delaySec)          # delay
    ps.setVolt(minVoltage)      # Set min voltage
    ps.delay(delaySec)          # delay

ps.off()
PS.close()
rm.close()

print("process complete :)")