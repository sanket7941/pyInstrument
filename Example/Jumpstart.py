
import pyvisa as visa
from heder.instr import PSupply

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
ps.setVolt(0)
ps.delay(5)
print("voltage=" + ps.measureVolt())
print("Current=" + ps.measureCurr())


ps.setVolt(26)
ps.delay(1)
print("voltage=" + ps.measureVolt())
print("Current=" + ps.measureCurr())


ps.setVolt(3)
ps.delay(.5)
print("voltage=" + ps.measureVolt())
print("Current=" + ps.measureCurr())


ps.setVolt(26)
ps.delay(5)
print("voltage=" + ps.measureVolt())
print("Current=" + ps.measureCurr())


ps.setVolt(10.8)
ps.delay(1)
print("voltage=" + ps.measureVolt())
print("Current=" + ps.measureCurr())


ps.setVolt(26)
ps.delay(60)    # need to set 60
print("voltage=" + ps.measureVolt())
print("Current=" + ps.measureCurr())


ps.setVolt(10.8)
ps.delay(5)
print("voltage=" + ps.measureVolt())
print("Current=" + ps.measureCurr())

print("process complete")
ps.delay(10)


ps.off()
PS.close()
