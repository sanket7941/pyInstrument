import pyvisa as visa

rm = visa.ResourceManager()
print("instrument id =>" + str (rm.list_resources()))

Instrument = rm.open_resource(rm.list_resources()[0])
print("instrument info => " + Instrument.query('*IDN?'))

