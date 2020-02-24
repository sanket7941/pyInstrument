
import pyvisa as visa
from pyinstrument import OScope

# instrument address

rm = visa.ResourceManager()
rm.list_resources()
DSO = rm.open_resource("USB0::10893::5988::MY57452459::0::INSTR")   # choose the proper address for your instrument
print('DSO detected=> ' + DSO.query('*IDN?'))  # chk communication is established or NOT

scope = OScope(DSO)

scope.screenShot("scrren Shot")

print("process complete")
