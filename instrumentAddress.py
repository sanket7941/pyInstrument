import pyvisa as visa

rm = visa.ResourceManager()
rm.list_resources()
rm.list_resources_info()

print("process complete")
