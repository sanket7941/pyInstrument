import pyvisa as visa
from xlwt import Workbook
from pyinstrument import PSupply


def test(volt, delay):
    ps.setVolt(volt)
    ps.delay(delay)
    return "success"


# instrument address
PSN5744USB = "USB0::2391::38151::US15J0384P::0::INSTR"
PSN5744Eth = "TCPIP0::169.254.57.0::inst0::INSTR"
PSTektronix = "USB0::1689::913::081001126668003045::0::INSTR"

# instrument Setup

rm = visa.ResourceManager()
rm.list_resources()
PS = rm.open_resource(rm.list_resources()[0])  # choose the proper address for your instrument
print('Power supply detected=> ' + PS.query('*IDN?'))  # chk communication is established or NOT

ps = PSupply(PS)
wb = Workbook()     # setup excel sheet

sheet1 = wb.add_sheet('readings')
# excel sheet templet

sheet1.write(3, 2, 'Project Name')
sheet1.write(3, 8, 'Setup No.')
sheet1.write(4, 8, 'Voltage')
sheet1.write(5, 8, 'Current')


ps.on()
ps.setCurr(3)  # set current to 3 amp

# step 1 => Usmax(16) to Usmin(8)

for i in range(1600, 700, -1):  # set the range from 16 to 8 V
    test(i / 100, 1.2)
    i -= 1
sheet1.write(3, 9, 'Step 1')
sheet1.write(4, 9, ps.measureVolt())
sheet1.write(5, 9, ps.measureCurr())


print(ps.measureVolt())
print(ps.measureCurr())

# step 2 =>  Usmin(8V) to 0V

for i in range(800, 1, -1):  # set the range from 8 to 0 V
    test(i / 100, 1.2)
    i -= 1

print(ps.measureVolt())
print(ps.measureCurr())

# step 3 =>   0V to Usmin (8V)

for i in range(1, 900):  # set the range from 0 to 8 V
    test(i / 100, 1)
    i += 1
sheet1.write(3, 10, 'Step 3')
sheet1.write(4, 10, ps.measureVolt())
sheet1.write(5, 10, ps.measureCurr())

print(ps.measureVolt())
print(ps.measureCurr())

# step 4 => Usmin(8V) to Usmax(16V)

for i in range(800, 1700):  # set the range from 9 to 16 V
    test(i / 100, 1)
    i += 1

sheet1.write(3, 11, 'Step 1')
sheet1.write(4, 11, ps.measureVolt())
sheet1.write(5, 11, ps.measureCurr())

print(ps.measureVolt())
print(ps.measureCurr())


wb.save('test_Results.xls')
print("data store excel sheet with name (test_Result) ")
ps.off()
PS.close()
print("process complete")
