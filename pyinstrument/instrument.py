"""
the file contains all instrument class
"""
import time

"""
DSO class
"""


class OScope:
    def __init__(self, IAddr):  # make local var for DSO
        self.DSO = IAddr

    def chk(self):
        self.DSO.query('*IDN?')
        print("test complete")
        return print("complete")

    # Take screenshots of the screen
    def screenShot(self, name, color="0"):  # colour value 1 = white 0 for black
        # Override the default timeout as the transfer can exceed this
        self.DSO.timeout = 10000
        # configure ink saver (black background as seen on screen)
        self.DSO.write(':HARDcopy:INKSaver %s', color)  # put 0 for black and 1 for white background
        # get screen data
        data = self.DSO.query_binary_values(':DISPlay:DATA? PNG, COLOR', datatype='B')
        # write it to file
        new_file = open(str(name) + ".PNG", 'wb')
        new_file.write(bytearray(data))
        print(' Screenshots Captured :) ')
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

    # Auto scale
    def autoscale(self):
        # This is the same as pressing the [Auto Scale] key on the front panel.
        self.DSO.write("AUToscale")
        return "done"

    # in self book CH29 Measure Commands pg:-817


"""
Power supply class N5477 and Tecktronics
"""


class PSupply:
    def __init__(self, IAddr):
        self.PS = IAddr

    def chk(self):
        self.PS.query('*IDN?')
        print("test complete")
        return print("complete")

    @staticmethod
    def delay(delay_Sec):
        time.sleep(delay_Sec)

    def on(self):  # turn ON power supply
        self.PS.write(':OUTPut:STATe %d' % 1)
        return "power supply is ON"

    def off(self):  # turn OFF power supply
        self.PS.write(':OUTPut:STATe %d' % 0)
        return "power supply is OFF"

    def setVolt(self, Volt):  # set Voltage
        self.PS.write("VOLT " + str(Volt))
        return "set voltage %d", Volt

    def setCurr(self, Current):  # set current
        self.PS.write("CURR " + str(Current))
        return " set Current %d", Current

    def measureVolt(self):  # measure voltage on Screen
        return self.PS.query("MEASure:VOLTage:DC?")

    def measureCurr(self):  # measure Current on Screen
        return self.PS.query("MEASure:CURRent:DC?")


"""
Waveform Generator class
"""


class WGenerator:
    def __init__(self, Iaddr):
        self.WG = Iaddr

    # Waveform
    '''
    all Waveform Generation
    square wave remaining 
    '''

    def sinWave(self, Freq=1000, amplitude=5, offset=0, phase=0):
        self.WG.write("VOLT:UNIT VPP")  # Set unit to VPP
        self.WG.write("APPL:SIN %d , %d , %d " % (Freq, amplitude, offset))  # set parameter
        self.WG.write("PHAS %d" % phase)  # Set phase
        self.WG.write("OUTP ON")
        print(self.WG.query("APPLy?"))
        return self.WG.query("APPLy?")

    def rampWave(self, Freq=1000, amplitude=5, offset=0):
        self.WG.write("VOLT:UNIT VPP")  # Set unit to VPP
        self.WG.write("APPL:RAMP %d ,%d , %d" % (Freq, amplitude, offset))  # set parameter
        print(self.WG.query("APPLy?"))
        return self.WG.query("APPLy?")

    def pulseWave(self, Freq=1000, amplitude=5, offset=0):
        self.WG.write("VOLT:UNIT VPP")  # Set unit to VPP
        self.WG.write("APPL:PULS %d ,%d , %d" % (Freq, amplitude, offset))  # set parameter
        print(self.WG.query("APPLy?"))
        return self.WG.query("APPLy?")

    def sqrWave(self, Freq=1000, amplitude=5, offset=0):
        self.WG.write("VOLT:UNIT VPP")  # Set unit to VPP
        self.WG.write("APPL:SQU %d ,%d , %d" % (Freq, amplitude, offset))  # set parameter
        print(self.WG.query("APPLy?"))
        return self.WG.query("APPLy?")

    # Burst
    '''
    need more improvements(add duty cycle,func selection)
    '''

    def burst(self, cycle=10, phase=0, period=1):
        self.WG.write("FUNC SQU")  # Select burst function */
        self.WG.write("BURS:STAT ON")  # Enable burst output
        self.WG.write("BURS:MODE TRIG")  # Select the burst mode
        self.WG.write("BURS:NCYC %d" % cycle)  # Set the cycle number
        self.WG.write("BURS:PHAS %d" % phase)  # Set the initial phase
        self.WG.write("BURS:INT:PER %d" % period)  # Set the period
        self.WG.write("TRIG:SOUR IMM")  # Select internal trigger source
        self.WG.write("OUTP ON")  # Enable the [Output] connector of CH1 at the front panel
        return "success"

    # Sweep

    def sweep(self, mode="LIN", start=100, stop=1000, Dtime=1):
        self.WG.write("FUNC SIN")  # set sin Wave  Select the sweep function
        self.WG.write("SWE:STATE ON")  # Enable frequency sweep
        self.WG.write("SWE:SPAC %s" % mode)  # LIN=> linear mode LOG => logarithmic mode
        self.WG.write("FREQ:STAR %d" % start)  # Set the start frequency
        self.WG.write("FREQ:STOP %d" % stop)  # Set the stop frequency
        self.WG.write("SWE:TIME %d" % Dtime)  # Set the sweep time
        self.WG.write("TRIG:SOUR IMM")  # Select internal trigger source
        self.WG.write("OUTP ON")  # Enable the [Output] connector of CH1 at the front panel
        return "sweep ON"


"""
Digital Multi Meter class
"""


class MMeter:
    def __init__(self, Iaddr):
        self.PS = Iaddr
