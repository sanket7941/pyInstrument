"""
the file contains all instrument class
"""
import time

"""
DSO class
"""


class OScope:
    def __init__(self, DSOAddr):  # make local var for DSO
        self.DSO = DSOAddr

    def chk(self):
        self.DSO.query('*IDN?')
        print("test complete")
        return print("complete")

    # Take screenshots of the screen
    def screenShot(self, name):
        # Override the default timeout as the transfer can exceed this
        self.DSO.timeout = 10000
        # configure ink saver (black background as seen on screen)
        self.DSO.write(':HARDcopy:INKSaver 0')  # put 0 for black and 1 for white background
        # get screen data
        data = self.DSO.query_binary_values(':DISPlay:DATA? PNG, COLOR', datatype='B')
        # write it to file
        new_file = open(str(name) + ".PNG", 'wb')
        new_file.write(bytearray(data))
        print(' screenshots done')
        return "success"

    # generate wave >? Need license 
    def waveGen(self, freq, type, volt):
        self.DSO.write("WGEN:FREQ " + str(freq))  # connect the wavegen to channel 1
        self.DSO.write("WGEN:FUNC " + type)  # SIN = sine SQUR=squre
        self.DSO.write("WGEN:OUTP ON")  # turn on
        self.DSO.write("WGEN:VOLT " + str(volt))  # volt P-P

    def selfSetup(self):
        self.DSO.write(":TIMebase:SCALe 3.0E-5")  # set time (horizontal Knob)
        self.DSO.write(":VDIV:SCALe 2.0E+1V")  # set amplitude (vertical knob)
        self.DSO.write(":WAVeform:SOURce CHANnel1")  # select channal

    def autoscale(self):
        # This is the same as pressing the [Auto Scale] key on the front panel.
        self.DSO.write("AUToscale")
        return "done"

    # in self book CH29 Measure Commands pg:-817


"""
Power supply class N5477 and Tecktronics
"""


class PSupply:
    def __init__(self, PSAddr):
        self.PS = PSAddr

    def chk(self):
        self.PS.query('*IDN?')
        print("test complete")
        return print("complete")

    @staticmethod
    def delay(delay_Sec):
        time.sleep(delay_Sec)

    def SVolt(self, Volt):  # NOT working
        self.PS.write("VOLT " + str(Volt))

    def SCurr(self, Current):
        self.PS.write("CURR " + str(Current))

    def MVolt(self):
        input_volt = self.PS.query("MEASure:VOLTage:DC?")
        return input_volt

    def MCurr(self):
        input_current = self.PS.query("MEASure:CURRent:DC?")
        return input_current

    def on_off(self, state):
        if state == 1:  # turn ON power supply
            self.PS.write(':OUTPut:STATe %d' % 1)
            print("power supply is ON")
        else:
            self.PS.write(':OUTPut:STATe %d' % 0)
            print("power supply is OFF")

    def test(self, volt, Dtime):
        self.PS.SVolt(volt)

        print("voltage=" + self.PS.MVolt())
        print("Current=" + self.PS.MCurr())
        self.PS.delay(Dtime)


"""
Digital Multi Meter class
"""


class MMeter:
    @staticmethod
    def test1():
        print("inside MMeter test def")
        return "success"