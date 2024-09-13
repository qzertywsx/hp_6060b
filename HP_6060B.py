from enum import Enum

class HP_6060B(object):
	def __init__(self, gpib, addr):
		self.address = addr
		self.gpib = gpib
		self.firstTime = True
		self.preCommand()
	
	class Mode(Enum):
		CURRENT    = 0
		VOLTAGE    = 1
		RESISTANCE = 2
	
	class CurrentRange(Enum):
		I6A  = 0
		I60A = 1
	
	def preCommand(self):
		if self.gpib.address != self.address or self.firstTime:
			self.firstTime = False
			self.gpib.set_address(self.address)
			self.gpib.write("++eor 2")
	
	def get_IDN(self):
		return self.gpib.get_IDN()
	
	def reset(self):
		self.preCommand()
		self.gpib.write("*CLS")
	
	def setOutput(self, on):
		self.preCommand()
		if on:
			self.gpib.write("INP ON")
		else:
			self.gpib.write("INP OFF")
			
	def getOutput(self):
		self.preCommand()
		self.gpib.write("INP?")
		return self.gpib.query("++read") == "1"
	
	def setVoltage(self, volt):
		self.preCommand()
		if volt >= 0.0 and volt <= 60.0:
			self.gpib.write("VOLT {:.3f}".format(volt))
			return True
		else:
			return False
		
	def getVoltage(self):
		self.preCommand()
		self.gpib.write("MEAS:VOLT?")
		try:
			return float(self.gpib.query("++read"))
		except:
			return False
		
	def setCurrent(self, amps):
		self.preCommand()
		if amps >= 0.0 and amps <= 60.0:
			self.gpib.write("CURR {:.3f}".format(amps))
			return True
		else:
			return False
	
	def getCurrent(self):
		self.preCommand()
		self.gpib.write("MEAS:CURR?")
		try:
			return float(self.gpib.query("++read"))
		except:
			return False
	
	def setResistance(self, ohm):
		self.preCommand()
		if ohm >= 0.033 and ohm <= 10000.0:
			self.gpib.write("RES {:.3f}".format(ohm))
			return True
		else:
			return False
	
	def getPower(self):
		self.preCommand()
		self.gpib.write("MEAS:POW?")
		try:
			return float(self.gpib.query("++read"))
		except:
			return False
	
	def setVoltageCurrent(self, volt, amps):
		self.preCommand()
		self.gpib.write("VOLT {:.3f};CURR {:.3f}".format(volt, amps))
	
	def setMode(self, mode):
		self.preCommand()
		if mode == self.Mode.CURRENT:
			self.gpib.write("MODE:CURR")
		if mode == self.Mode.VOLTAGE:
			self.gpib.write("MODE:VOLT")
		if mode == self.Mode.RESISTANCE:
			self.gpib.write("MODE:RES")
			
	def getMode(self):
		self.preCommand()
		self.gpib.write("MODE?")
		m = self.gpib.query("++read")
		if m == "CURR":
			return self.Mode.CURRENT
		if m == "VOLT":
			return self.Mode.VOLTAGE
		if m == "RES":
			return self.Mode.RESISTANCE
	
	def setShortMode(self, on):
		self.preCommand()
		if on:
			self.gpib.write("INP:SHORT ON")
		else:
			self.gpib.write("INP:SHORT OFF")
			
	def getShortMode(self):
		self.preCommand()
		self.gpib.write("INP:SHORT?")
		return self.gpib.query("++read") == "1"
	
	def setCurrentRange(self, currRange):
		self.preCommand()
		if currRange == self.CurrentRange.I6A:
			self.gpib.write("CURR:RANG 6")
		if currRange == self.CurrentRange.I60A:
			self.gpib.write("CURR:RANG 60")
			
	def getCurrentRange(self):
		self.preCommand()
		self.gpib.write("CURR:RANG?")
		m = self.gpib.query("++read")
		if m == "6.0000E+0":
			return self.CurrentRange.I6A
		if m == "6.0000E+1":
			return self.CurrentRange.I60A
	
	def local(self):
		self.preCommand()
		self.gpib.local()
