"""Module providing an interface to the HP 6060B 60 V 60 A electronic load"""
from enum import Enum

class HP6060B():
    """Class to represent the HP 6060B 60 V 60 A electronic load"""
    def __init__(self, _gpib, addr):
        self.address = addr
        self.gpib = _gpib
        self.first_time = True
        self._pre_command()

    class Mode(Enum):
        """Enum with the load mode"""
        CURRENT    = 0
        VOLTAGE    = 1
        RESISTANCE = 2

    class CurrentRange(Enum):
        """Enum with the current range"""
        I6A  = 0
        I60A = 1

    def __str__(self):
        return f"HP 6060B address: {self.address}"

    def _pre_command(self):
        """Command to be executed before every other command"""
        if self.gpib.address != self.address or self.first_time:
            self.first_time = False
            self.gpib.set_address(self.address)
            self.gpib.write("++eor 2")

    def get_idn(self):
        """Return the *IDN? of the instrument"""
        return self.gpib.get_idn()

    def reset(self):
        """Reset the instrument to the default state"""
        self._pre_command()
        self.gpib.write("*CLS")

    def set_load_state(self, on):
        """Enable the load"""
        self._pre_command()
        if on:
            self.gpib.write("INP ON")
        else:
            self.gpib.write("INP OFF")

    def get_load_state(self):
        """Get the load state"""
        self._pre_command()
        self.gpib.write("INP?")
        return self.gpib.query("++read") == "1"

    def set_voltage(self, volt):
        """Set the voltage"""
        self._pre_command()
        if 0.0 <= volt <= 60.0:
            self.gpib.write(f"VOLT {volt:.3f}")
            return True
        return False

    def get_voltage(self):
        """Return the measured voltage or False in case of problem"""
        self._pre_command()
        self.gpib.write("MEAS:VOLT?")
        try:
            return float(self.gpib.query("++read"))
        except (ValueError, AttributeError):
            return False

    def set_current(self, amps):
        """Set the current"""
        self._pre_command()
        if 0.0 <= amps <= 60.0:
            self.gpib.write(f"CURR {amps:.3f}")
            return True
        return False

    def get_current(self):
        """Return the measured current or False in case of problem"""
        self._pre_command()
        self.gpib.write("MEAS:CURR?")
        try:
            return float(self.gpib.query("++read"))
        except (ValueError, AttributeError):
            return False

    def set_resistance(self, ohm):
        """Set the resistance"""
        self._pre_command()
        if 0.033 <= ohm <= 10000.0:
            self.gpib.write(f"RES {ohm:.3f}")
            return True
        return False

    def get_power(self):
        """Return the measured power or False in case of problem"""
        self._pre_command()
        self.gpib.write("MEAS:POW?")
        try:
            return float(self.gpib.query("++read"))
        except (ValueError, AttributeError):
            return False

    def set_mode(self, mode):
        """Set the load mode"""
        self._pre_command()
        if mode == self.Mode.CURRENT:
            self.gpib.write("MODE:CURR")
        if mode == self.Mode.VOLTAGE:
            self.gpib.write("MODE:VOLT")
        if mode == self.Mode.RESISTANCE:
            self.gpib.write("MODE:RES")

    def get_mode(self):
        """Get the load mode"""
        self._pre_command()
        self.gpib.write("MODE?")
        m = self.gpib.query("++read")
        if m == "CURR":
            return self.Mode.CURRENT
        if m == "VOLT":
            return self.Mode.VOLTAGE
        if m == "RES":
            return self.Mode.RESISTANCE
        return False

    def set_short_mode(self, on):
        """Set the short circuit mode"""
        self._pre_command()
        if on:
            self.gpib.write("INP:SHORT ON")
        else:
            self.gpib.write("INP:SHORT OFF")

    def get_short_mode(self):
        """Get the short circuit mode"""
        self._pre_command()
        self.gpib.write("INP:SHORT?")
        return self.gpib.query("++read") == "1"

    def set_current_range(self, curr_range):
        """Set the current range of the load"""
        self._pre_command()
        if curr_range == self.CurrentRange.I6A:
            self.gpib.write("CURR:RANG 6")
        if curr_range == self.CurrentRange.I60A:
            self.gpib.write("CURR:RANG 60")

    def get_current_range(self):
        """Get the current range of the load"""
        self._pre_command()
        self.gpib.write("CURR:RANG?")
        m = self.gpib.query("++read")
        if m == "6.0000E+0":
            return self.CurrentRange.I6A
        if m == "6.0000E+1":
            return self.CurrentRange.I60A
        return False

    def get_error(self):
        """Get the last error"""
        self._pre_command()
        self.gpib.write("SYST:ERR?")
        return self.gpib.query("++read")

    def local(self):
        """Go to local mode (Reenable the front panel control)"""
        self._pre_command()
        self.gpib.local()
