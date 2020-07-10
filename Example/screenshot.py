
import pyvisa as visa
from pyinstrument import OScope

# instrument address

rm = visa.ResourceManager()
rm.list_resources()
DSO = rm.open_resource(rm.list_resources()[0])   # choose the proper address for your instrument
print('DSO detected=> ' + DSO.query('*IDN?'))  # chk communication is established or NOT

scope = OScope(DSO)
# screenshot file name
scope.screenShot("test ",'0')
print("process complete")
