"""
n


"""
import pyvisa as visa
from pyinstrument import PSupply

# instrument address
PSN5744USB = "USB0::2391::38151::US15J0384P::0::INSTR"
PSN5744Eth = "TCPIP0::169.254.57.0::inst0::INSTR"
PSTektronix = "USB0::1689::913::081001126668003045::0::INSTR"

rm = visa.ResourceManager()
rm.list_resources()
PS = rm.open_resource(rm.list_resources()[0])   # choose the proper address for your instrument
print('Power supply detected=> ' + PS.query('*IDN?'))  # chk communication is established or NOT

ps = PSupply(PS)

ps.on()
ps.setCurr(3)  # set current to 3 amp
print('program started')
ps.setVolt(0)
ps.delay(1)

ps.setVolt(11.8)    # umin
ps.delay(.4)    # tr = 400ms
ps.setVolt(16)  # Umax 16V
ps.delay(2)     # 2 sec
ps.setVolt(11.8)  # tf = 400ms
ps.delay(.4)
ps.setVolt(0)
ps.delay(1)


print(ps.measureVolt())
print(ps.measureCurr())
ps.delay(delay)
ps.off()
PS.close()
print("process complete")
