import pyvisa as visa

from pyinstrument import PSupply


def test(volt, delay):
    ps.setVolt(volt)
    ps.delay(delay)
    return "success"


# instrument Setup

rm = visa.ResourceManager()
rm.list_resources()
PS = rm.open_resource(rm.list_resources()[0])  # choose the proper address for your instrument
print('Power supply detected=> ' + PS.query('*IDN?'))  # chk communication is established or NOT

ps = PSupply(PS)
ps.on()
ps.setCurr(3)  # set current to 3 amp

# step 1 => Usmax(16) to Usmin(9)

for i in range(16, 9, -1):  # set the range from 16 to 8 V
    test(i, 60)
    i -= .5
    test(i, 60)
print(ps.measureVolt())
print(ps.measureCurr())

# step 2 =>  Usmin(9V) to 0V
for i in range(9, 0, -1):  # set the range from 16 to 8 V
    test(i, 60)
    i -= .5
    test(i, 60)
print(ps.measureVolt())
print(ps.measureCurr())

# step 3 =>   Wait 1 min
ps.delay(60)
# step 4 => quick incres to 16 V

ps.setVolt(16)

ps.off()
PS.close()
print("process complete")
